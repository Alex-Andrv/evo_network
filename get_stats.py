import glob
import os
from collections import defaultdict

stats_ = {}
directory_path = "alex_exp"
for file in glob.glob('*.csv', root_dir=directory_path):
    solver, suff = file.split('_', 1)
    if "tdg&iter" in solver:
        solver_1, solver_2, suff = file.split('_', 2)
        solver = f"{solver_1}_{solver_2}"
        if "tdg&iter_descent_v" in file:
            solver_1, solver_2, solver_3, suff = file.split('_', 3)
            solver = f"{solver_1}_{solver_2}_{solver_3}"
    problem = suff[:-4]
    if problem not in stats_:
        stats_[problem] = {}
    with open(os.path.join(directory_path, file), "r") as log:
        for line in log:
            if solver in line:
                continue
            if 'time' in line:
                continue
            time, result = map(float, line.split(","))
            if solver not in stats_[problem]:
                stats_[problem][solver] = []
            stats_[problem][solver].append([time, result])

for problem, stats in stats_.items():
    with open(f"{problem}.csv", "w") as log:
        solvers = stats.keys()
        solvers = ["tdg", "tdg&1+1[10000]", "tdg&doerr1+1[3;10000]",
                   "tdg&iter_descent[10000, 1]", "tdg&iter_descent_v2[10000, 1]",
                   "tdg&iter_descent_v3[10000, 1]"]
        print(problem)
        headers = []
        for solver in solvers:
            headers.append(f"{solver}_time")
            headers.append(f"{solver}_res")
        log.write("|".join(headers))
        log.write("\n")
        max_iter = 20
        for i in range(max_iter):
            line = []
            for solver in solvers:
                if len(stats[solver]) > i:
                    line.append(stats[solver][i][0])
                    line.append(stats[solver][i][1])
                else:
                    line.append("None")
                    line.append("None")
            log.write(",".join(map(str, line)))
            log.write("\n")


