#!/bin/bash -i
source activate evo_network
rm "/nfs/home/aandreev/evo_network/generate/seria_2_0.9/tdg_iter_descent_v3[5000, 1]&Wiki-Vote&uniform_1-1000&const_0.8.txt"
chmod +x "/nfs/home/aandreev/evo_network/generate/seria_2_0.9/tdg_iter_descent_v3[5000, 1]&Wiki-Vote&uniform_1-1000&const_0.8.py"
python "/nfs/home/aandreev/evo_network/generate/seria_2_0.9/tdg_iter_descent_v3[5000, 1]&Wiki-Vote&uniform_1-1000&const_0.8.py" >> "/nfs/home/aandreev/evo_network/generate/seria_2_0.9/tdg_iter_descent_v3[5000, 1]&Wiki-Vote&uniform_1-1000&const_0.8.txt" 2>&1
