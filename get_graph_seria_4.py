import glob
import os
from collections import defaultdict
from dltm import read_dltm
from tss import TSSProblem, agents_to_vec
import shutil
import re
import matplotlib.pyplot as plt

stats_ = {}
directory_path = "generate"
seria = "seria_4"
thresholds = [0.5, 0.6, 0.7, 0.8]
graphs = "graphs"
with_check = True


if os.path.exists(f"{graphs}/{seria}"):
   shutil.rmtree(f"{graphs}/{seria}")

os.mkdir(f"{graphs}/{seria}")

all_problems = dict()

for threshold_ in thresholds:
    for file in glob.glob('*.txt', root_dir=f"{directory_path}/{seria}_{threshold_}"):
        solver, graph, influences, threshold, *params = file[:-4].split('&')
        graph_full_name = '&'.join([graph, influences, threshold] + params)

        if graph_full_name not in all_problems:
            all_problems[graph_full_name] = dict()

        with open(os.path.join(directory_path, f"{seria}_{threshold_}", file), "r") as log:
            if "tdg" != solver:
                all_problems[graph_full_name][threshold_] = []
            for idx, line in enumerate(log):
                if "tdg" != solver:
                    if line.startswith("best_fit"):
                        # best_fit=1588, k=1588
                        best_fit, k = re.findall(r'=\s*(\d+)', line)
                        all_problems[graph_full_name][threshold_].append({'best_fit': int(best_fit), 'k': int(k)})
                    else:
                        break
                else:
                    continue
                    if line.startswith("TSS"):
                        all_problems[graph_full_name][threshold_].append({'tss': line.split()[11].split('=')[1]})
                        

for graph_full_name in all_problems.keys():
    dltm = read_dltm(f'/nfs/home/aandreev/evo_network/generated_graph/{seria}/{graph_full_name}')
    k = dltm.nodes_count() * 0.75
    minimum = float("inf")
    for solver, info in all_problems[graph_full_name].items():

        # if "tdg " in  solver:
        #     # plt.axhline(y=int(info[0]['tss'].replace(",", "")),  linestyle='--', label=f'{solver}')
        #     continue
        # Получаем данные
        print(solver)
        best_fit_values = [entry['best_fit'] for entry in all_problems[graph_full_name][solver]]
        minimum = min(minimum, info[0]['best_fit'])

        # Создаем график
        plt.plot(best_fit_values, label=f'(1+1)-WEA, k={info[0]["k"]}')
        # plt.title(graph_full_name)
        plt.xlabel('Mutation')
        plt.ylabel('Influence')
        plt.grid(True)
    plt.legend()
    plt.ylim(minimum - minimum * 0.2)
    plt.xlim(0, 5000)

    plt.savefig(f"{graphs}/{seria}/{graph_full_name}_f(TSS).pdf")

    plt.clf()
    # for solver, info in all_problems[graph_full_name].items():
    #     k_values = [entry['k'] for entry in all_problems[graph_full_name][solver]]
    #     plt.plot(k_values, label=f'Solver: {solver}')
    #     plt.xlabel('iteration')
    #     plt.ylabel('|TSS|')
    #     plt.grid(True)

    # plt.title(f'{graph_full_name}')
    # plt.legend()
    # plt.savefig(f"{graphs}/{seria}/{graph_full_name}_|TSS|.png")
    # plt.clf()

