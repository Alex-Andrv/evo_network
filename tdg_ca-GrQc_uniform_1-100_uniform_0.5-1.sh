#!/bin/bash -i
source activate evo_network
chmod +x "/nfs/home/aandreev/evo_network/tdg_ca-GrQc_uniform_1-100_uniform_0.5-1.py"
python "/nfs/home/aandreev/evo_network/tdg_ca-GrQc_uniform_1-100_uniform_0.5-1.py" >> "tdg_ca-GrQc_uniform_1-100_uniform_0.5-1.txt" 2>&1