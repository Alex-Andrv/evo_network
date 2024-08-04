
             

task_name = "p2p-Gnutella08_uniform_1-100_const_0.75"
solver_name, run_script = ("tdg&doerr1+1[3;10000]",lambda problem, seed: problem.solve_using_tdg_and_then_doerr_1p1(None, None, 3,tss_stop_criteria.by_iteration_count(10000),seed))


             
import tss_stop_criteria
from dltm import read_dltm
from tss import TSSProblem

if __name__ == '__main__':

    tss_name, dltm = task_name, read_dltm(f'/nfs/home/aandreev/evo_network/generated_graph/{task_name}')
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

             