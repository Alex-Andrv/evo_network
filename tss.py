import pickle
import random
from copy import copy
from time import time

from pysat.pb import EncType
from pysat.solvers import Glucose3

import genetic
import tss_sat
import tss_tdg


def exec_with_time(executable):
    time_start = time()
    result = executable()
    time_end = time()
    return result, time_end - time_start


class TSSProblem:

    def __init__(self, dltm, threshold):
        self.dltm = dltm
        self.threshold = threshold

    def nodes_count(self):
        return self.dltm.nodes_count()

    def edges_count(self):
        return self.dltm.edges_count()

    def my_fit(self, vec):
        n = len(vec)
        if n != self.nodes_count():
            raise ValueError('vector length ({}) != agents number ({})'.format(n, self.nodes_count()))

        start_vec = [1 if a else 0 for a in vec]
        cur_vec = copy(start_vec)
        cur_infl = [0 for _ in range(n)]
        cur_indices = []
        for i in range(n):
            if cur_vec[i]:
                cur_indices.append(i)

        while True:
            new_indices = []
            for i in cur_indices:
                agent = self.dltm.ord_to_agent[i]
                for agent_to in self.dltm.graph[agent]:
                    i_to = self.dltm.agent_to_ord[agent_to]
                    cur_infl[i_to] += self.dltm.infl[(agent, agent_to)]
                    if not cur_vec[i_to] and cur_infl[i_to] >= self.dltm.agents[agent_to]:
                        new_indices.append(self.dltm.agent_to_ord[agent_to])
                        cur_vec[i_to] = 1

            if len(new_indices) == 0:
                break
            cur_indices = list(new_indices)

        return wt(cur_vec), cur_vec
    def fit(self, vec):
        n = len(vec)
        if n != self.nodes_count():
            raise ValueError('vector length ({}) != agents number ({})'.format(n, self.nodes_count()))

        start_vec = [1 if a else 0 for a in vec]
        cur_vec = copy(start_vec)
        cur_infl = [0 for _ in range(n)]
        cur_indices = []
        for i in range(n):
            if cur_vec[i]:
                cur_indices.append(i)

        while wt(cur_vec) < self.threshold:
            new_indices = []
            for i in cur_indices:
                agent = self.dltm.ord_to_agent[i]
                for agent_to in self.dltm.graph[agent]:
                    i_to = self.dltm.agent_to_ord[agent_to]
                    cur_infl[i_to] += self.dltm.infl[(agent, agent_to)]
                    if not cur_vec[i_to] and cur_infl[i_to] >= self.dltm.agents[agent_to]:
                        new_indices.append(self.dltm.agent_to_ord[agent_to])
                        cur_vec[i_to] = 1

            if len(new_indices) == 0:
                break
            cur_indices = list(new_indices)

        return wt(start_vec) if wt(cur_vec) >= self.threshold else n + 1

    def solve_abstract(self, solver, seed=None):
        random.seed(seed)
        (solution_vec, metadata), time = exec_with_time(lambda: solver())
        solution = vec_to_agents(self, solution_vec)
        metadata['time'] = time
        return solution, metadata

    def solve_using_1p1(self, stop_criteria, mutation=genetic.non_increasing_default_mutation, seed=None):
        return self.solve_abstract(lambda:  genetic.using_1p1(
            [1] * self.nodes_count(), self.fit, mutation, stop_criteria
        ), seed)

    def solve_using_genetic_algorithm(self, stop_criteria, mutation=genetic.non_increasing_default_mutation,
                                      crossover=genetic.crossover, seed=None):
        return self.solve_abstract(lambda: genetic.genetics_algorithm(
            [1] * self.nodes_count(), self.fit, mutation, crossover, stop_criteria
        ), seed)

    def solve_using_1cl(self, lmbd, stop_criteria, seed=None):
        return self.solve_abstract(lambda: genetic.using_1cl(
            [1] * self.nodes_count(), self.fit, genetic.default_mutation, lmbd, stop_criteria
        ), seed)

    def solve_using_custom_ga(self, l, h, g, stop_criteria, seed=None):
        return self.solve_abstract(lambda: genetic.using_custom_ga(
            [1] * self.nodes_count(), self.fit, genetic.default_mutation, genetic.two_point_crossover, l, h, g,
            stop_criteria
        ), seed)

    def solve_using_tdg(self, d1, d2):
        solution, solution_time = exec_with_time(lambda: tss_tdg.solve(self, d1, d2))
        return solution, {'time': solution_time}

    def solve_using_tdg_and_then_1p1(self, d1, d2, stop_criteria, seed=None):
        tdg_solution, tdg_solution_time = exec_with_time(lambda: tss_tdg.solve(self, d1, d2))
        solution, metadata = self.solve_abstract(lambda: genetic.using_1p1(
            agents_to_vec(self, tdg_solution), self.fit,
            genetic.non_increasing_default_mutation,
            stop_criteria
            ), seed)
        metadata['time'] = metadata['time'] + tdg_solution_time
        return solution, metadata


    def enhance_solution(self, solution, stop_criteria, iterations, t_size, solutions_cache):
        assert (stop_criteria.is_iteration_count())
        active_agent = copy(set(solution))
        passive_agent = copy(self.dltm.agents.keys() - active_agent)
        best_fit, curr_vector = self.my_fit(agents_to_vec(self, active_agent))

        solutions_cache[tuple(agents_to_vec(self, active_agent))] = curr_vector


        while (iterations < stop_criteria.get_iteration_count() and best_fit < self.threshold):
            drop_active_element = {el for el in active_agent if random.random() < (1 / len(active_agent))}
            r = len(drop_active_element)
            drop_passive_agent = set(random.sample(list(passive_agent), r))
            new_active_agent = (active_agent - drop_active_element) | drop_passive_agent
            new_passive_agent = (passive_agent - drop_passive_agent) | drop_active_element
            curr_fit, curr_vector = self.my_fit(agents_to_vec(self, new_active_agent))
            if tuple(agents_to_vec(self, new_active_agent)) in solutions_cache:
                # print("cache hit")
                continue

            solutions_cache[tuple(agents_to_vec(self, new_active_agent))] = curr_vector
            if (curr_fit > best_fit):
                # print(f"best_fit={best_fit}, k={len(solution)}")
                passive_agent -= drop_passive_agent
                active_agent -= drop_active_element
                active_agent = new_active_agent
                passive_agent = new_passive_agent
                best_fit = curr_fit
            t_size.append(len(active_agent))
            iterations += 1
        return (active_agent, iterations) if best_fit >= self.threshold else (set(solution), iterations)

    def iter_descent_v3(self, stop_criteria, init_solution, iter_epoch, t_size):
        solution = set(init_solution)
        iterations = 0

        assert (stop_criteria.is_iteration_count())
        inf = {}
        for agent_id in self.dltm.agents.keys():
            inf[agent_id] = 0
            for agent_id_to in self.dltm.graph[agent_id]:
                inf[agent_id] += self.dltm.infl[(agent_id, agent_id_to)]

        solutions_cache = dict()
        while len(solution) > 0 and (iterations < stop_criteria.get_iteration_count()):
            for _ in range(iter_epoch):
                min_inf = None
                del_agent_id = None
                # test_arr = []
                for agent_id in solution:
                    if (min_inf is None) or (inf[agent_id] < min_inf):
                        min_inf = inf[agent_id]
                        del_agent_id = agent_id
                    # test_arr.append((len(self.dltm.graph[agent_id]), inf[agent_id]))

                if min_inf is None:
                    raise Exception("min_inf is None")

                solution = [x for x in solution if x != del_agent_id]
                # random_element = random.choice(list(solution))
                # solution.remove(random_element)

            solution, iterations = self.enhance_solution(solution, stop_criteria, iterations, t_size, solutions_cache)

        all_solutions = [list(zip(keys, values)) for keys, values in solutions_cache.items()]
        import torch
        inverse_pairs = torch.tensor(all_solutions, dtype=torch.float32)
        adj = self.dltm.to_compress_graph()

        with open('tensor.pkl', 'wb') as f:
            pickle.dump({'adj': adj, "inverse_pairs": inverse_pairs}, f)

        return solution

    def iter_descent_v2(self, stop_criteria, init_solution, iter_epoch, t_size):
        solution = set(init_solution)
        iterations = 0

        assert (stop_criteria.is_iteration_count())
        inf = {}
        for agent_id in self.dltm.agents.keys():
            inf[agent_id] = 0
            for agent_id_to in self.dltm.graph[agent_id]:
                inf[agent_id] += self.dltm.infl[(agent_id, agent_id_to)] / self.dltm.agents[agent_id_to]

        solutions_cache = dict()

        while len(solution) > 0 and (iterations < stop_criteria.get_iteration_count()):
            for _ in range(iter_epoch):
                min_inf = None
                del_agent_id = None
                # test_arr = []
                for agent_id in solution:
                    if (min_inf is None) or (inf[agent_id] < min_inf):
                        min_inf = inf[agent_id]
                        del_agent_id = agent_id
                    # test_arr.append((len(self.dltm.graph[agent_id]), inf[agent_id]))

                if min_inf is None:
                    raise Exception("min_inf is None")

                solution = [x for x in solution if x != del_agent_id]
                # random_element = random.choice(list(solution))
                # solution.remove(random_element)

            solution, iterations = self.enhance_solution(solution, stop_criteria, iterations, t_size, solutions_cache)

        all_solutions = [[list(keys), list(values)] for keys, values in solutions_cache.items()]
        import torch
        inverse_pairs = torch.tensor(all_solutions)

        return solution

    def iter_descent(self, stop_criteria, init_solution, iter_epoch, t_size):
        solution = set(init_solution)
        iterations = 0

        assert (stop_criteria.is_iteration_count())
        inf = {}
        for agent_id in self.dltm.agents.keys():
            inf[agent_id] = tss_tdg.compute_influence(self.dltm, agent_id, self.dltm.agents.copy(), set(), 1000)

        solutions_cache = dict()

        while len(solution) > 0 and (iterations < stop_criteria.get_iteration_count()):
            for _ in range(iter_epoch):
                min_inf = None
                del_agent_id = None
                for agent_id in solution:
                    if (min_inf is None) or (len(self.dltm.graph[agent_id]) < min_inf):
                        min_inf = len(self.dltm.graph[agent_id])
                        del_agent_id = agent_id

                if min_inf is None:
                    raise Exception("min_inf is None")

                solution = [x for x in solution if x != del_agent_id]
                # random_element = random.choice(list(solution))
                # solution.remove(random_element)

            solution, iterations = self.enhance_solution(solution, stop_criteria, iterations, t_size, solutions_cache)

        all_solutions = [[list(keys), list(values)] for keys, values in solutions_cache.items()]
        import torch
        inverse_pairs = torch.tensor(all_solutions)
        # adj =

        return solution

    def solve_using_tdg_and_then_iter_descent_v3(self, d1, d2, stop_criteria, iter_epoch=1, seed=None):
        tdg_solution, tdg_solution_time = exec_with_time(lambda: tss_tdg.solve(self, d1, d2))
        random.seed(seed)
        t_size = []
        new_solution, time = exec_with_time(lambda: self.iter_descent_v3(
            stop_criteria,
            tdg_solution, iter_epoch, t_size))
        metadata = {'time': tdg_solution_time + time, "t_size": t_size}
        return new_solution, metadata

    def solve_using_tdg_and_then_iter_descent_v2(self, d1, d2, stop_criteria, iter_epoch=1, seed=None):
        tdg_solution, tdg_solution_time = exec_with_time(lambda: tss_tdg.solve(self, d1, d2))
        random.seed(seed)
        t_size = []
        new_solution, time = exec_with_time(lambda: self.iter_descent_v2(
            stop_criteria,
            tdg_solution, iter_epoch, t_size))
        metadata = {'time': tdg_solution_time + time, "t_size": t_size}
        return new_solution, metadata

    def solve_using_tdg_and_then_iter_descent(self, d1, d2, stop_criteria, iter_epoch=1, seed=None):
        tdg_solution, tdg_solution_time = exec_with_time(lambda: tss_tdg.solve(self, d1, d2))
        random.seed(seed)
        t_size = []
        new_solution, time = exec_with_time(lambda: self.iter_descent(
            stop_criteria,
            tdg_solution, iter_epoch, t_size))
        metadata = {'time': tdg_solution_time + time, "t_size": t_size}
        return new_solution, metadata

    def solve_using_tdg_and_then_doerr_1p1(self, d1, d2, beta, stop_criteria, seed=None):
        env = genetic.init_doerr_env(beta, self.nodes_count() // 2)
        tdg_solution, tdg_solution_time = exec_with_time(lambda: tss_tdg.solve(self, d1, d2))
        solution, metadata = self.solve_abstract(lambda: genetic.using_1p1(
            agents_to_vec(self, tdg_solution), self.fit,
            lambda vec: genetic.non_increasing_doerr_mutation(vec, env),
            stop_criteria
        ), seed)
        metadata['time'] = metadata['time'] + tdg_solution_time
        return solution, metadata

    # def iter_descent(self, init_solution):

    # def solve_using_tdg_and_then_doerr_1p1_iter_descent(self, d1, d2, beta, stop_criteria, seed=None):
    #     solution, metadata = self.solve_using_tdg_and_then_doerr_1p1(d1, d2, beta, stop_criteria, seed)
    #     mew_solution, time = self.iter_descent(solution)
    #     metadata['time'] += time
    #     return solution, metadata

    def solve_using_sat(self, pb_encoding=EncType.seqcounter, sat_solver=lambda cnf: Glucose3(bootstrap_with=cnf)):

        def do_solve():
            n = self.nodes_count()
            if self.fit([0] * n) != n + 1:
                return []

            left = 0
            right = self.threshold
            right_solution = None
            while left + 1 < right:
                mid = (left + right) // 2
                mid_solution = tss_sat.solve_tss(self, mid, pb_encoding, sat_solver)
                if mid_solution:
                    right = mid
                    right_solution = mid_solution
                else:
                    left = mid

            return right_solution if right_solution else tss_sat.solve_tss(self, right, pb_encoding, sat_solver)

        solution, time = exec_with_time(lambda: do_solve())
        return solution, {'time': time}

    def pair_fit(self, active_agent: set, passive_agent: set):
        n = len(active_agent) + len(passive_agent)
        if n != self.nodes_count():
            raise ValueError('vector length ({}) != agents number ({})'.format(n, self.nodes_count()))

        start_active_agent = copy(active_agent)
        start_passive_agent = copy(passive_agent)

        cur_vec = [0 for _ in range(n)]
        cur_infl = [0 for _ in range(n)]

        while wt(cur_vec) < self.threshold:
            new_indices = []
            for agent_id in start_active_agent:
                for agent_to in self.dltm.graph[agent_id]:
                    i_to = self.dltm.agent_to_ord[agent_to]
                    cur_infl[i_to] += self.dltm.infl[(agent_id, agent_to)]
                    if not cur_vec[i_to] and cur_infl[i_to] >= self.dltm.agents[agent_to]:
                        new_indices.append(agent_to)
                        cur_vec[i_to] = 1

            if len(new_indices) == 0:
                break
            start_active_agent = set(new_indices)

        return len(active_agent) if wt(cur_vec) >= self.threshold else n + 1


def wt(vec):
    return sum(vec)


def vec_to_agents(tss, vec):
    agents = []
    for i in range(tss.nodes_count()):
        if vec[i]:
            agents.append(tss.dltm.ord_to_agent[i])
    return agents


def agents_to_vec(tss, agents):
    vec = [0] * tss.nodes_count()
    for agent in agents:
        vec[tss.dltm.agent_to_ord[agent]] = 1
    return vec
