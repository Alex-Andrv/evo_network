#!/bin/bash -i
source activate evo_network
chmod +x "/nfs/home/aandreev/evo_network/tdg_barabasi_albert_uniform_1-100_uniform_0.5-1.py"
"/nfs/home/aandreev/evo_network/tdg_barabasi_albert_uniform_1-100_uniform_0.5-1.py" >> "tdg_barabasi_albert_uniform_1-100_uniform_0.5-1.txt" 2>&1
