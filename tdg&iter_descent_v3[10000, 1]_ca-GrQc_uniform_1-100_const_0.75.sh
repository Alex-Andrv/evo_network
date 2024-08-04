#!/bin/bash -i
source activate evo_network
chmod +x "/nfs/home/aandreev/evo_network/tdg&iter_descent_v3[10000, 1]_ca-GrQc_uniform_1-100_const_0.75.py"
python "/nfs/home/aandreev/evo_network/tdg&iter_descent_v3[10000, 1]_ca-GrQc_uniform_1-100_const_0.75.py" >> "tdg&iter_descent_v3[10000, 1]_ca-GrQc_uniform_1-100_const_0.75.txt" 2>&1
