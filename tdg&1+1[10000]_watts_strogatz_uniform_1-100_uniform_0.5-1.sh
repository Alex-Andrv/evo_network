#!/bin/bash -i
source activate evo_network
chmod +x "/nfs/home/aandreev/evo_network/tdg&1+1[10000]_watts_strogatz_uniform_1-100_uniform_0.5-1.py"
"/nfs/home/aandreev/evo_network/tdg&1+1[10000]_watts_strogatz_uniform_1-100_uniform_0.5-1.py" >> "tdg&1+1[10000]_watts_strogatz_uniform_1-100_uniform_0.5-1.txt" 2>&1
