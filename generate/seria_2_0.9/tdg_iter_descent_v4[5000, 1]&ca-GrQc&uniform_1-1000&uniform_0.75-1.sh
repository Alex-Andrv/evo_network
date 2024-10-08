#!/bin/bash -i
source activate evo_network
rm "/nfs/home/aandreev/evo_network/generate/seria_2_0.9/tdg_iter_descent_v4[5000, 1]&ca-GrQc&uniform_1-1000&uniform_0.75-1.txt"
chmod +x "/nfs/home/aandreev/evo_network/generate/seria_2_0.9/tdg_iter_descent_v4[5000, 1]&ca-GrQc&uniform_1-1000&uniform_0.75-1.py"
python "/nfs/home/aandreev/evo_network/generate/seria_2_0.9/tdg_iter_descent_v4[5000, 1]&ca-GrQc&uniform_1-1000&uniform_0.75-1.py" >> "/nfs/home/aandreev/evo_network/generate/seria_2_0.9/tdg_iter_descent_v4[5000, 1]&ca-GrQc&uniform_1-1000&uniform_0.75-1.txt" 2>&1
