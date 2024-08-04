#!/bin/bash -i
source activate evo_network
chmod +x "/nfs/home/aandreev/evo_network/tdg&1+1[10000]_watts_strogatz_uniform_1-100_const_0.75.py"
"/nfs/home/aandreev/evo_network/tdg&1+1[10000]_watts_strogatz_uniform_1-100_const_0.75.py" >> "tdg&1+1[10000]_watts_strogatz_uniform_1-100_const_0.75.txt" 2>&1
