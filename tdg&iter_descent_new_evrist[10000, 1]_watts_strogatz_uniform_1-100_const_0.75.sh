#!/bin/bash -i
source activate evo_network
chmod +x "/nfs/home/aandreev/evo_network/tdg&iter_descent_new_evrist[10000, 1]_watts_strogatz_uniform_1-100_const_0.75.py"
"/nfs/home/aandreev/evo_network/tdg&iter_descent_new_evrist[10000, 1]_watts_strogatz_uniform_1-100_const_0.75.py" >> "tdg&iter_descent_new_evrist[10000, 1]_watts_strogatz_uniform_1-100_const_0.75.txt" 2>&1
