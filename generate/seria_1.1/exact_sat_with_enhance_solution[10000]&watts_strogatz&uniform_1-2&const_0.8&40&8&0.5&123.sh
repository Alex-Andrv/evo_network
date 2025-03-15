#!/bin/bash -i
source activate evo_network
rm "/nfs/home/aandreev/evo_network/generate/seria_1.1/exact_sat_with_enhance_solution[10000]&watts_strogatz&uniform_1-2&const_0.8&40&8&0.5&123.txt"
chmod +x "/nfs/home/aandreev/evo_network/generate/seria_1.1/exact_sat_with_enhance_solution[10000]&watts_strogatz&uniform_1-2&const_0.8&40&8&0.5&123.py"
python "/nfs/home/aandreev/evo_network/generate/seria_1.1/exact_sat_with_enhance_solution[10000]&watts_strogatz&uniform_1-2&const_0.8&40&8&0.5&123.py" >> "/nfs/home/aandreev/evo_network/generate/seria_1.1/exact_sat_with_enhance_solution[10000]&watts_strogatz&uniform_1-2&const_0.8&40&8&0.5&123.txt" 2>&1
