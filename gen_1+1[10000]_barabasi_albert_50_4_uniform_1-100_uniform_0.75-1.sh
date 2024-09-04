#!/bin/bash -i
source activate evo_network
rm "gen_1+1[10000]_barabasi_albert_50_4_uniform_1-100_uniform_0.75-1.txt"
chmod +x "/nfs/home/aandreev/evo_network/gen_1+1[10000]_barabasi_albert_50_4_uniform_1-100_uniform_0.75-1.py"
python "/nfs/home/aandreev/evo_network/gen_1+1[10000]_barabasi_albert_50_4_uniform_1-100_uniform_0.75-1.py" >> "gen_1+1[10000]_barabasi_albert_50_4_uniform_1-100_uniform_0.75-1.txt" 2>&1
