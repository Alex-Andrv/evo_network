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
                best_fit, k = re.findall(r'=\s*(\d+)', line)
                all_problems[graph_full_name][solver].append({'best_fit': int(best_fit), 'k': int(k)})
            else:
               break

filter = ["tdg_iter_descent[10000, 1]", "v2", "v4", "tdg_1+1", "tdg_doerr1+1"]
mapping = {
    "tdg_iter_descent[10000, 1]": "(1+1)-WEA_v1",
    "v2": "(1+1)-WEA_v2", 
    "v4": "(1+1)-WEA_v3", 
    "tdg_1+1": "(1+1)-EA", 
    "tdg_genetic": "GA", 
    "tdg_doerr1+1": "(1+1)-FEA"
}
# Задаем цвета для каждого алгоритма
colors = {
    "(1+1)-WEA_v1": "blue",
    "(1+1)-WEA_v2": "green",
    "(1+1)-WEA_v3": "orange",
    "(1+1)-EA": "purple",
    "(1+1)-FEA": "red"
}

# Определяем порядок отрисовки
order = ["(1+1)-EA", "(1+1)-FEA", "(1+1)-WEA_v1", "(1+1)-WEA_v2", "(1+1)-WEA_v3"]

for graph_full_name in all_problems.keys():
    dltm = read_dltm(f'/nfs/home/aandreev/evo_network/generated_graph/{seria}/{graph_full_name}')
    k = dltm.nodes_count() * 0.75
    # plt.axhline(y=int(k), color='r', linestyle='--', label=f'threshold = {int(k)}')

    # Словарь для хранения данных по каждому solver, чтобы потом рисовать их в нужном порядке
    data_by_solver = {}

    for solver, info in all_problems[graph_full_name].items():
        for pref in filter:
            if pref in solver:
                solver_name = mapping[pref]
                # Получаем данные
                best_fit_values = [entry['k'] for entry in all_problems[graph_full_name][solver]]
                data_by_solver[solver_name] = best_fit_values

    # Рисуем графики в установленном порядке и цветах
    for solver_name in order:
        if solver_name in data_by_solver:
            plt.plot(data_by_solver[solver_name], label=solver_name, color=colors[solver_name])

    plt.xlabel('Mutation')
    plt.ylabel('|TSS|')
    plt.grid(True)
    plt.legend()
    plt.xlim(0, 10000)
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

