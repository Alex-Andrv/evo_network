import tss_stop_criteria
from tss_measurements_data import fb_data_tss

if __name__ == '__main__':
    solvers = [
        # ('tdg[1]', lambda problem: problem.solve_using_tdg(1, 1)),
        # ('tdg[2]', lambda problem: problem.solve_using_tdg(2, 2)),
        # ('tdg[3]', lambda problem: problem.solve_using_tdg(3, 3)),
        # ('tdg[5]', lambda problem: problem.solve_using_tdg(5, 5)),
        # ('tdg[8]', lambda problem: problem.solve_using_tdg(8, 8)),
        # ('tdg[1000, 1000]', lambda problem: problem.solve_using_tdg(1000, 1000)),
        # ('tdg[10000, 10000]', lambda problem: problem.solve_using_tdg(10000, 10000)),
        # ('1+1[3000]', lambda problem: problem.solve_using_1p1(tss_stop_criteria.by_iteration_count(3000))),
        # ('tdg[10000, 10000]&1+1[10000]', lambda problem, seed: problem.solve_using_tdg_and_then_1p1(10000, 10000, tss_stop_criteria.by_iteration_count(10000), seed)),
        # ('tdg[10000, 10000]&doerr1+1[1.6;3000]', lambda problem: problem.solve_using_tdg_and_then_doerr_1p1(10000, 10000, 1.6, tss_stop_criteria.by_iteration_count(3000))),
        # ('tdg[10000, 10000]&doerr1+1[2;3000]', lambda problem: problem.solve_using_tdg_and_then_doerr_1p1(10000, 10000, 2, tss_stop_criteria.by_iteration_count(3000))),
        # ('tdg[10000, 10000]&doerr1+1[2.5;10000]', lambda problem, seed: problem.solve_using_tdg_and_then_doerr_1p1(10000, 10000, 2.5, tss_stop_criteria.by_iteration_count(10000), seed)),
        # ('tdg[10000, 10000]&iter_descent[10000, 1]', lambda problem, seed: problem.solve_using_tdg_and_then_iter_descent(10000, 10000, tss_stop_criteria.by_iteration_count(10000), 1, seed)),
        # ('tdg[10000, 10000]&iter_descent[10000, 2]',
        #  lambda problem, seed: problem.solve_using_tdg_and_then_iter_descent(10000, 10000,
        #                                                                tss_stop_criteria.by_iteration_count(10000), 2, seed)),
        # ('tdg[10000, 10000]&iter_descent[10000, 3]',
        #  lambda problem, seed: problem.solve_using_tdg_and_then_iter_descent(10000, 10000,
        #                                                                tss_stop_criteria.by_iteration_count(10000), 3, seed)),
        # ('tdg[10000, 10000]&iter_descent[10000, 4]',
        #  lambda problem, seed: problem.solve_using_tdg_and_then_iter_descent(10000, 10000,
        #                                                                tss_stop_criteria.by_iteration_count(10000), 4, seed)),
        # ('tdg[10000, 10000]&iter_descent[10000, 5]',
        #  lambda problem, seed: problem.solve_using_tdg_and_then_iter_descent(10000, 10000,
        #                                                                tss_stop_criteria.by_iteration_count(10000), 5, seed)),
        # ('tdg[10000, 10000]&iter_descent[10000, 6]',
        #  lambda problem, seed: problem.solve_using_tdg_and_then_iter_descent(10000, 10000,
        #                                                                tss_stop_criteria.by_iteration_count(10000), 5, seed)),
        # ('tdg[10000, 10000]&iter_descent[10000, 7]',
        #  lambda problem, seed: problem.solve_using_tdg_and_then_iter_descent(10000, 10000,
        #                                                                tss_stop_criteria.by_iteration_count(10000), 5, seed)),
        ('tdg[10000, 10000]&iter_descent[10000, 10]',
         lambda problem, seed: problem.solve_using_tdg_and_then_iter_descent(10000, 10000,
                                                                       tss_stop_criteria.by_iteration_count(10000), 10, seed)),
        # ('tdg[10000, 10000]&iter_descent[10000, 15]',
        #  lambda problem, seed: problem.solve_using_tdg_and_then_iter_descent(10000, 10000,
        #                                                                tss_stop_criteria.by_iteration_count(10000), 15,
        #                                                                      seed)),
    ]

    with open(f'alex_exp/{solvers[0][0]}.csv', 'w') as f:
        # f.write('dltm')
        # [f.write(',{}'.format(solvers[i][0])) for i in range(len(solvers))]
        # f.write('\n')

        for tss_name, tss in fb_data_tss:
            f.write(tss_name)

            # tdg_solver_name, tdg_solver = ('tdg[1000, 1000]', lambda problem: problem.solve_using_tdg(1000, 1000))
            # tdg_solution, tdg_metadata = tdg_solver(tss)
            # print('TSS instance {} ({} nodes, {} edges) solved using {}:  time={}, ts_size={}, ts={}'
            #       .format(tss_name, tss.nodes_count(), tss.edges_count(), tdg_solver_name, tdg_metadata['time'],
            #               len(tdg_solution), tdg_solution))


            for solver_name, solver in solvers:
                node_counts = []
                times = []
                for i in range(50):
                    solution, metadata = solver(tss, i)
                    print('TSS instance {} ({} nodes, {} edges) solved using {}:  time={}, ts_size={}, ts={}'
                      .format(tss_name, tss.nodes_count(), tss.edges_count(), solver_name, metadata['time'],
                              len(solution), solution))
                    f.write('{},{:.3f} {}'.format(solver_name, metadata['time'], len(solution)))
                    f.write('\n')
                    node_counts.append(tss.nodes_count())
                    times.append(metadata['time'])
            print('AVG_{},{:.3f} {}'.format(
                solver_name, sum(times) / len(times), sum(node_counts) / len(node_counts)))
            f.write('AVG_{},{:.3f} {}'.format(
                solver_name, sum(times) / len(times), sum(node_counts) / len(node_counts)))

