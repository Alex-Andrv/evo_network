#!/bin/bash -i
source activate evo_network
rm "gen_tdg_barabasi_albert_50_4_uniform_1-100_const_0.8.txt"
chmod +x "/nfs/home/aandreev/evo_network/gen_tdg_barabasi_albert_50_4_uniform_1-100_const_0.8.py"
python "/nfs/home/aandreev/evo_network/gen_tdg_barabasi_albert_50_4_uniform_1-100_const_0.8.py" >> "gen_tdg_barabasi_albert_50_4_uniform_1-100_const_0.8.txt" 2>&1
