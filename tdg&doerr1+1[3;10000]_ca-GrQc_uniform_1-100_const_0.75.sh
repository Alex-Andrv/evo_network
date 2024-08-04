#!/bin/bash -i
source activate evo_network
chmod +x "/nfs/home/aandreev/evo_network/tdg&doerr1+1[3;10000]_ca-GrQc_uniform_1-100_const_0.75.py"
python "/nfs/home/aandreev/evo_network/tdg&doerr1+1[3;10000]_ca-GrQc_uniform_1-100_const_0.75.py" >> "tdg&doerr1+1[3;10000]_ca-GrQc_uniform_1-100_const_0.75.txt" 2>&1
