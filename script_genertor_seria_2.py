import os
run_script = "run_script_seria_1.sh"

if os.path.exists(run_script):
   os.remove(run_script)

run_script_template = """
    sbatch --cpus-per-task=2 --mem=20G -p as --time=20:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "{}"
"""

python_script_template_head = """

task_name = "{}"
solver_name, run_script = ("{}",{})

"""

python_script_template_body = """
import tss_stop_criteria
from dltm import read_dltm
from tss import TSSProblem

if __name__ == '__main__':

    tss_name, dltm = task_name, read_dltm(f'/nfs/home/aandreev/evo_network/generated_graph/seria-1/{task_name}')
    tss = TSSProblem(dltm, dltm.nodes_count() * 0.75)
    with open(f'alex_exp/{solver_name}_{task_name}.csv', 'w') as f:
        f.write(f"{solver_name}\\n")
        f.write(f"time,|TSS|\\n")
        for i in range(20):
            solution, metadata = run_script(tss, i)
            print('TSS instance {} ({} nodes, {} edges) solved using {}:  time={}, ts_size={}, ts={}'
                      .format(tss_name, tss.nodes_count(), tss.edges_count(), solver_name, metadata['time'],
                              len(solution), solution))
            f.write(str(metadata['time']))
            f.write(",")
            f.write(str(len(solution)))
            f.write('\\n')
            f.flush()
"""

sh_script_template = """#!/bin/bash -i
source activate evo_network
rm {}
chmod +x "/nfs/home/aandreev/evo_network/{}"
python "/nfs/home/aandreev/evo_network/{}" >> "{}" 2>&1
"""

if __name__ == '__main__':
 solvers = [
     ('gen_exact_sat', "lambda problem, seed: problem.solve_using_sat()"),
     ('gen_tdg', "lambda problem, seed: problem.solve_using_tdg(None, None)"),
     ('gen_1+1[10000]',
      "lambda problem, seed: problem.solve_using_1p1(tss_stop_criteria.by_iteration_count(10000), seed=seed)"),
     ('tdg&1+1[10000]',
      "lambda problem, seed: problem.solve_using_tdg_and_then_1p1(None, None,tss_stop_criteria.by_iteration_count(10000), seed)"),
     ]
 tasks = [
     "barabasi_albert_50_4_uniform_1-100_const_0.8",
     "barabasi_albert_50_4_uniform_1-100_uniform_0.75-1",
     "watts_strogatz_50_8_0.5_123_uniform_1-100_const_0.8", 
     "watts_strogatz_50_8_0.5_123_uniform_1-100_uniform_0.75-1"
 ]
 for solver_name, run_scrip in solvers:
     for task in tasks:
         with open(f"{solver_name}_{task}.py", "w") as python_script:
             script = f"""
             {python_script_template_head.format(task, solver_name, run_scrip)}
             {python_script_template_body}
             """
             python_script.write(script)
         with open(f"{solver_name}_{task}.sh", "w") as python_script:
             python_script.write(sh_script_template.format(f"{solver_name}_{task}.txt", f"{solver_name}_{task}.py", f"{solver_name}_{task}.py", f"{solver_name}_{task}.txt"))
         with open(run_script, 'a') as run_script_file:
             run_script_file.write(run_script_template.format(f"{solver_name}_{task}.sh"))
         
