
             

task_name = "watts_strogatz_50_8_0.5_123_uniform_1-100_uniform_0.75-1"
solver_name, run_script = ("gen_exact_sat",lambda problem, seed: problem.solve_using_sat())


             
import tss_stop_criteria
from dltm import read_dltm
from tss import TSSProblem

if __name__ == '__main__':

    tss_name, dltm = task_name, read_dltm(f'/nfs/home/aandreev/evo_network/generated_graph/seria-1/{task_name}')
    tss = TSSProblem(dltm, dltm.nodes_count() * 0.75)
    with open(f'alex_exp/{solver_name}_{task_name}.csv', 'w') as f:
        f.write(f"{solver_name}\n")
        f.write(f"time,|TSS|\n")
        for i in range(20):
            solution, metadata = run_script(tss, i)
            print('TSS instance {} ({} nodes, {} edges) solved using {}:  time={}, ts_size={}, ts={}'
                      .format(tss_name, tss.nodes_count(), tss.edges_count(), solver_name, metadata['time'],
                              len(solution), solution))
            f.write(str(metadata['time']))
            f.write(",")
            f.write(str(len(solution)))
            f.write('\n')
            f.flush()

             