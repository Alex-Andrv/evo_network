
             

task_name = "barabasi_albert&uniform_1-5&uniform_0.75-1&50&4"
solver_name, run_script = ("exact_sat",lambda problem, seed: problem.solve_using_sat())
seria = "seria_1"


             

import os 
os.chdir('/nfs/home/aandreev/evo_network/')
import sys 
sys.path.append('/nfs/home/aandreev/evo_network/')
import tss_stop_criteria
from dltm import read_dltm
from tss import TSSProblem

if __name__ == '__main__':

    tss_name, dltm = task_name, read_dltm(f'/nfs/home/aandreev/evo_network/generated_graph/{seria}/{task_name}')
    tss = TSSProblem(dltm, dltm.nodes_count() * 0.75)
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

             