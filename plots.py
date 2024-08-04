import glob
import os
import matplotlib as mpl

import matplotlib.pyplot as plt

directory_path = "alex_exp"
stats = {}
for file in glob.glob('*stats_by_iter.csv', root_dir=directory_path):
    if "tdg&1+1[10000]" in file:
        solver = "(1+1)-EA"
    elif "tdg&doerr1+1" in file:
        solver = "(1+1)-FEA"
    elif "tdg&iter_descent[10000, 1]" in file:
        solver = "(1+1)-WEA-v1"
    elif "tdg&iter_descent_v2" in file:
        solver = "(1+1)-WEA-v3"
    elif "tdg&iter_descent_v3" in file:
        solver = "(1+1)-WEA-v2"
    with open(os.path.join(directory_path, file), 'r') as log:
        stats[solver] = list(map(int, log.readline().split(',')))
plt.rc('font', size=9)
fig, ax = plt.subplots(figsize=(5, 5))
  # Размер шрифта
# for (solver_name, data), ax in zip(stats.items(), axs):
#     ax.plot(range(10000), data)
#     ax.set_title(solver_name)


for solver_name in ["(1+1)-WEA-v2", "(1+1)-WEA-v1", "(1+1)-WEA-v3", "(1+1)-FEA", "(1+1)-EA"]:
    data = stats[solver_name]
    ax.plot(range(10000), data, label=solver_name)

ax.plot(range(10000), [549] * 10000, label="greedy", linestyle='--')

ax.legend()
ax.set_xlabel('Iteration')
ax.set_ylabel('TS size')
plt.tight_layout()
# plt.rc('font', size=40)
# plt.rcParams['font.size'] = '30'

# plt.rcParams.update({'font.size': 30})

# Сохранение графика в файл PNG
plt.savefig('plots.pdf')
plt.show()