#!/bin/bash -i
source activate evo_network
rm "/nfs/home/aandreev/evo_network/generate/seria_3/tdg_1+1[10000]&ca-GrQc&uniform_1-1000&uniform_0.75-1.txt"
chmod +x "/nfs/home/aandreev/evo_network/generate/seria_3/tdg_1+1[10000]&ca-GrQc&uniform_1-1000&uniform_0.75-1.py"
python "/nfs/home/aandreev/evo_network/generate/seria_3/tdg_1+1[10000]&ca-GrQc&uniform_1-1000&uniform_0.75-1.py" >> "/nfs/home/aandreev/evo_network/generate/seria_3/tdg_1+1[10000]&ca-GrQc&uniform_1-1000&uniform_0.75-1.txt" 2>&1
