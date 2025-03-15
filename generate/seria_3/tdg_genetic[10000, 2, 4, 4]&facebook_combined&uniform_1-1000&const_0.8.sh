#!/bin/bash -i
source activate evo_network
rm "/nfs/home/aandreev/evo_network/generate/seria_3/tdg_genetic[10000, 2, 4, 4]&facebook_combined&uniform_1-1000&const_0.8.txt"
chmod +x "/nfs/home/aandreev/evo_network/generate/seria_3/tdg_genetic[10000, 2, 4, 4]&facebook_combined&uniform_1-1000&const_0.8.py"
python "/nfs/home/aandreev/evo_network/generate/seria_3/tdg_genetic[10000, 2, 4, 4]&facebook_combined&uniform_1-1000&const_0.8.py" >> "/nfs/home/aandreev/evo_network/generate/seria_3/tdg_genetic[10000, 2, 4, 4]&facebook_combined&uniform_1-1000&const_0.8.txt" 2>&1
