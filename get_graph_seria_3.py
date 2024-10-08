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
seria = "seria_3"
graphs = "graphs"
with_check = True


if os.path.exists(f"{graphs}/{seria}"):
   shutil.rmtree(f"{graphs}/{seria}")

os.mkdir(f"{graphs}/{seria}")

all_problems = dict()

for file in glob.glob('*.txt', root_dir=f"{directory_path}/{seria}"):
    solver, graph, influences, threshold, *params = file[:-4].split('&')
    graph_full_name = '&'.join([graph, influences, threshold] + params)

    if graph_full_name not in all_problems:
        all_problems[graph_full_name] = dict()

    with open(os.path.join(directory_path, seria, file), "r") as log:
       all_problems[graph_full_name][solver] = []
       for idx, line in enumerate(log):
            if line.startswith("best_fit"):
                # best_fit=1588, k=1588
                best_fit, k = re.findall(r'=\s*(\d+)', line)
                all_problems[graph_full_name][solver].append({'best_fit': int(best_fit), 'k': int(k)})
            else:
               break

for graph_full_name in all_problems.keys():
    dltm = read_dltm(f'/nfs/home/aandreev/evo_network/generated_graph/{seria}/{graph_full_name}')
    k = dltm.nodes_count() * 0.75
    plt.axhline(y=int(k), color='r', linestyle='--', label=f'threshold = {int(k)}')
    for solver, info in all_problems[graph_full_name].items():
        # Получаем данные
        best_fit_values = [entry['best_fit'] for entry in all_problems[graph_full_name][solver]]
        # Создаем график
        plt.plot(best_fit_values, label=f'Solver: {solver}')
        plt.title('f(TSS)')
        plt.xlabel('iteration')
        plt.ylabel('f(TSS)')
        plt.grid(True)
    plt.legend()
    plt.savefig(f"{graphs}/{seria}/{graph_full_name}_f(TSS).png")

    plt.clf()
    for solver, info in all_problems[graph_full_name].items():
        k_values = [entry['k'] for entry in all_problems[graph_full_name][solver]]
        plt.plot(k_values, label=f'Solver: {solver}')
        plt.xlabel('iteration')
        plt.ylabel('|TSS|')
        plt.grid(True)

    plt.title(f'{graph_full_name}')
    plt.legend()
    plt.savefig(f"{graphs}/{seria}/{graph_full_name}_|TSS|.png")
    plt.clf()

