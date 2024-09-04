#!/bin/bash -i
source activate evo_network
rm "gen_exact_sat_watts_strogatz_50_8_0.5_123_uniform_1-100_uniform_0.75-1.txt"
chmod +x "/nfs/home/aandreev/evo_network/gen_exact_sat_watts_strogatz_50_8_0.5_123_uniform_1-100_uniform_0.75-1.py"
python "/nfs/home/aandreev/evo_network/gen_exact_sat_watts_strogatz_50_8_0.5_123_uniform_1-100_uniform_0.75-1.py" >> "gen_exact_sat_watts_strogatz_50_8_0.5_123_uniform_1-100_uniform_0.75-1.txt" 2>&1
