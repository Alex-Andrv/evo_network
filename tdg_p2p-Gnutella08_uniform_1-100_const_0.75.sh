#!/bin/bash -i
source activate evo_network
chmod +x "/nfs/home/aandreev/evo_network/tdg_p2p-Gnutella08_uniform_1-100_const_0.75.py"
python "/nfs/home/aandreev/evo_network/tdg_p2p-Gnutella08_uniform_1-100_const_0.75.py" >> "tdg_p2p-Gnutella08_uniform_1-100_const_0.75.txt" 2>&1
