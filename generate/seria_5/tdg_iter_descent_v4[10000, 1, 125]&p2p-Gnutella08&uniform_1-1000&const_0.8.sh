#!/bin/bash -i
source activate evo_network
rm "/nfs/home/aandreev/evo_network/generate/seria_5/tdg_iter_descent_v4[10000, 1, 125]&p2p-Gnutella08&uniform_1-1000&const_0.8.txt"
chmod +x "/nfs/home/aandreev/evo_network/generate/seria_5/tdg_iter_descent_v4[10000, 1, 125]&p2p-Gnutella08&uniform_1-1000&const_0.8.py"
python "/nfs/home/aandreev/evo_network/generate/seria_5/tdg_iter_descent_v4[10000, 1, 125]&p2p-Gnutella08&uniform_1-1000&const_0.8.py" >> "/nfs/home/aandreev/evo_network/generate/seria_5/tdg_iter_descent_v4[10000, 1, 125]&p2p-Gnutella08&uniform_1-1000&const_0.8.txt" 2>&1
