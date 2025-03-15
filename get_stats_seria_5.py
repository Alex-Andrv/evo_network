import glob
import os
from collections import defaultdict
from dltm import read_dltm
from tss import TSSProblem, agents_to_vec
import shutil

stats_ = {}
directory_path = "alex_exp"
seria = "seria_5"
with_check = False


if os.path.exists(seria):
   shutil.rmtree(seria)

os.mkdir(seria)

def check_sol(graph_full_name, sol):
    dltm = read_dltm(f'/nfs/home/aandreev/evo_network/generated_graph/{seria}/{graph_full_name}')
    k = dltm.nodes_count() * 0.75
    tss = TSSProblem(dltm, dltm.nodes_count() * 0.75)

    res, _ = tss.my_fit(agents_to_vec(tss, sol))
    assert res >= int(k) 

all_problems = set()

for file in glob.glob('*.csv', root_dir=f"{directory_path}/{seria}"):
    print(file)
    
    bug_solvers = []
    new_file = file
    for bug_solver in bug_solvers:
        if bug_solver in file:
            new_file = file.replace('&', '_', 1)

    if file.count('&') < 3:
        os.remove(os.path.join(directory_path, seria, file))
        continue

    solver, graph, influences, threshold, *params = new_file[:-4].split('&')
    graph_full_name = '&'.join([graph, influences, threshold] + params)
    if solver not in stats_:
        stats_[solver] = dict()
    if graph_full_name not in stats_[solver]:
        stats_[solver][graph_full_name] = []

    with open(os.path.join(directory_path, seria, file), "r") as log:
        lines = log.readlines()
        if len(lines) == 0:
            continue
        real_solver = lines[0].strip()
        print(os.path.join(directory_path, seria, file))
        time, size, sol = lines[1].strip().split(',')
        assert time == "time", f"{lines[1]}"
        assert size == "|TSS|", f"{lines[1]}"
        assert sol == "sol", sol
        lines = lines[2:]
        for line in lines:
            if len(line.strip().split(',')) == 1:
                continue
            time, size, sol = line.strip().split(',')
            time, size = float(time), int(size)
            # solution_list = list(sol.split("&"))
            # assert len(solution_list) == size

            stats_[solver][graph_full_name].append([time, size])

            all_problems.add(graph_full_name)

            # if with_check:
            #     check_sol(graph_full_name, solution_list)

for problem in all_problems:
    solvers = stats_.keys()
    solver_to_results = {}
    for solver, stats in stats_.items():
        results = stats[problem]
        assert solver not in solver_to_results
        solver_to_results[solver] = results
    with open(f"{seria}/{problem}.csv", "w") as log:
            print("\n")
            print(problem)
            headers = []
            for solver in solvers:
                headers.append(f"{solver}_time")
                headers.append(f"{solver}_size")
            log.write("|".join(headers))
            print("|".join(headers))
            log.write("\n")
            max_iter = 20
            solvers_score = dict()
            for i in range(max_iter):
                line = []
                for solver in solvers:
                    if solver not in solvers_score:
                        solvers_score[solver] = (0, 0)

                    assert len(solver_to_results[solver]) <= max_iter
                    if len(solver_to_results[solver]) > i:
                        line.append(solver_to_results[solver][i][0])
                        line.append(solver_to_results[solver][i][1])
                        sum_score, cnt = solvers_score[solver]
                        solvers_score[solver] = (sum_score + solver_to_results[solver][i][1], cnt + 1)
                    else:
                        line.append("None")
                        line.append("None")
                log.write("|".join(map(str, line)))
                print("|".join(map(str, line)))
                log.write("\n")
            
            solvers_measure = dict()
            for solver, (sum_score, cnt) in solvers_score.items():
                solvers_measure[solver] = sum_score / cnt if cnt != 0 else float("inf")

            line = []
            for solver in solvers:
                line.append("None")
                line.append(solvers_measure[solver])
                
            print("|".join(map(str, line)))
            print(f"best solver is: {min(solvers_measure, key=solvers_measure.get)}")