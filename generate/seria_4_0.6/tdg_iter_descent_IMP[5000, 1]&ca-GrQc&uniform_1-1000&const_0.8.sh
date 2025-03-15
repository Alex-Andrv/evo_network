#!/bin/bash -i
source activate evo_network
rm "/nfs/home/aandreev/evo_network/generate/seria_4_0.6/tdg_iter_descent_IMP[5000, 1]&ca-GrQc&uniform_1-1000&const_0.8.txt"
chmod +x "/nfs/home/aandreev/evo_network/generate/seria_4_0.6/tdg_iter_descent_IMP[5000, 1]&ca-GrQc&uniform_1-1000&const_0.8.py"
python "/nfs/home/aandreev/evo_network/generate/seria_4_0.6/tdg_iter_descent_IMP[5000, 1]&ca-GrQc&uniform_1-1000&const_0.8.py" >> "/nfs/home/aandreev/evo_network/generate/seria_4_0.6/tdg_iter_descent_IMP[5000, 1]&ca-GrQc&uniform_1-1000&const_0.8.txt" 2>&1
