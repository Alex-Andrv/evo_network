#!/bin/bash -i
source activate evo_network
rm "/nfs/home/aandreev/evo_network/generate/seria_1/1+1[10000]&barabasi_albert&uniform_1-5&const_0.8&50&4.txt"
chmod +x "/nfs/home/aandreev/evo_network/generate/seria_1/1+1[10000]&barabasi_albert&uniform_1-5&const_0.8&50&4.py"
python "/nfs/home/aandreev/evo_network/generate/seria_1/1+1[10000]&barabasi_albert&uniform_1-5&const_0.8&50&4.py" >> "/nfs/home/aandreev/evo_network/generate/seria_1/1+1[10000]&barabasi_albert&uniform_1-5&const_0.8&50&4.txt" 2>&1
