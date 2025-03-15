#!/bin/bash -i
source activate evo_network
rm "/nfs/home/aandreev/evo_network/generate/seria_3/tdg_genetic[10000, 2, 4, 4]&ca-GrQc&uniform_1-1000&uniform_0.75-1.txt"
chmod +x "/nfs/home/aandreev/evo_network/generate/seria_3/tdg_genetic[10000, 2, 4, 4]&ca-GrQc&uniform_1-1000&uniform_0.75-1.py"
python "/nfs/home/aandreev/evo_network/generate/seria_3/tdg_genetic[10000, 2, 4, 4]&ca-GrQc&uniform_1-1000&uniform_0.75-1.py" >> "/nfs/home/aandreev/evo_network/generate/seria_3/tdg_genetic[10000, 2, 4, 4]&ca-GrQc&uniform_1-1000&uniform_0.75-1.txt" 2>&1
