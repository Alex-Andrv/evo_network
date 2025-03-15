
             

task_name = "p2p-Gnutella06&uniform_1-1000&const_0.8"
solver_name, run_script = ("tdg_iter_descent_v4[10000, 1, 125]",lambda problem, seed: problem.solve_using_tdg_and_then_iter_descent_v4(None, None, tss_stop_criteria.by_iteration_count(10000), 1, 125, seed))
seria = "seria_5"


             

import os 
os.chdir('/nfs/home/aandreev/evo_network/')
import sys 
sys.path.append('/nfs/home/aandreev/evo_network/')
import tss_stop_criteria
from dltm import read_dltm
from tss import TSSProblem

if __name__ == '__main__':

    tss_name, dltm = task_name, read_dltm(f'/nfs/home/aandreev/evo_network/generated_graph/{seria}/{task_name}')
    tss = TSSProblem(dltm, dltm.nodes_count() * 0.8)
    with open(f'alex_exp/{seria}/{solver_name}&{task_name}.csv', 'w') as f:
        f.write(f"{solver_name}\n")
        f.write(f"time,|TSS|,sol\n")
        for i in range(20):
            solution, metadata = run_script(tss, i)
            print('TSS instance {} ({} nodes, {} edges) solved using {}:  time={}, ts_size={}, ts={}'
                      .format(tss_name, tss.nodes_count(), tss.edges_count(), solver_name, metadata['time'],
                              len(solution), solution))
            f.write(str(metadata['time']))
            f.write(",")
            f.write(str(len(solution)))
            f.write(",")
            f.write(str('&'.join(map(str, solution))))
            f.write('\n')
            f.flush()

             