#!/bin/bash -i
source activate evo_network
chmod +x "/nfs/home/aandreev/evo_network/tdg&1+1[10000]_Wiki-Vote_uniform_1-100_uniform_0.5-1.py"
python "/nfs/home/aandreev/evo_network/tdg&1+1[10000]_Wiki-Vote_uniform_1-100_uniform_0.5-1.py" >> "tdg&1+1[10000]_Wiki-Vote_uniform_1-100_uniform_0.5-1.txt" 2>&1
