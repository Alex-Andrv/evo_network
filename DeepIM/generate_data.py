from dltm import read_dltm
from tss import TSSProblem

task_name = "p2p-Gnutella08_uniform_1-100_const_0.75"
tss_name, dltm = task_name, read_dltm(f'/nfs/home/aandreev/evo_network/generated_graph/{task_name}')
tss = TSSProblem(dltm, dltm.nodes_count() * 0.75)


if __name__ == '__main__':

    tss_name, dltm = task_name, read_dltm(f'/nfs/home/aandreev/evo_network/generated_graph/{task_name}')
    tss = TSSProblem(dltm, dltm.nodes_count() * 0.75)
    with open(f'alex_exp/{solver_name}_{task_name}.csv', 'w') as f:
        f.write(f"{solver_name}\n")
        f.write(f"time,|TSS|\n")
        for i in range(20):