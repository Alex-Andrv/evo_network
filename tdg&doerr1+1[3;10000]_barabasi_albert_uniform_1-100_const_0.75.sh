#!/bin/bash -i
source activate evo_network
chmod +x "/nfs/home/aandreev/evo_network/tdg&doerr1+1[3;10000]_barabasi_albert_uniform_1-100_const_0.75.py"
"/nfs/home/aandreev/evo_network/tdg&doerr1+1[3;10000]_barabasi_albert_uniform_1-100_const_0.75.py" >> "tdg&doerr1+1[3;10000]_barabasi_albert_uniform_1-100_const_0.75.txt" 2>&1
