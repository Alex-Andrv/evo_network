
             

task_name = "p2p-Gnutella06_uniform_1-100_const_0.75"
solver_name, run_script = ("tdg&iter_descent_v2[10000, 1]",lambda problem, seed: problem.solve_using_tdg_and_then_iter_descent_v2(None, None, tss_stop_criteria.by_iteration_count(10000), 1, seed))


             
import tss_stop_criteria
from dltm import read_dltm
from tss import TSSProblem

if __name__ == '__main__':

    tss_name, dltm = task_name, read_dltm(f'/nfs/home/aandreev/evo_network/generated_graph/{task_name}')
    tss = TSSProblem(dltm, dltm.nodes_count() * 0.75)
    with open(f'alex_exp/{solver_name}_{task_name}_stats_by_iter.csv', 'w') as f:
        solution, metadata = run_script(tss, 42)
        f.write(','.join(map(str, metadata['t_size'])))
        f.flush()

             