#!/bin/bash -i
#sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&1+1[10000]_barabasi_albert_uniform_1-100_const_0.75.sh"
#sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&1+1[10000]_barabasi_albert_uniform_1-100_uniform_0.5-1.sh"

sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&1+1[10000]_facebook_combined_uniform_1-100_const_0.75.sh"
sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&1+1[10000]_facebook_combined_uniform_1-100_uniform_0.5-1.sh"

#sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&1+1[10000]_watts_strogatz_uniform_1-100_const_0.75.sh"
#sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&1+1[10000]_watts_strogatz_uniform_1-100_uniform_0.5-1.sh"

sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&1+1[10000]_Wiki-Vote_uniform_1-100_const_0.75.sh"
sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&1+1[10000]_Wiki-Vote_uniform_1-100_uniform_0.5-1.sh"

sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&1+1[10000]_ca-GrQc_uniform_1-100_const_0.75.sh"
sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&1+1[10000]_ca-GrQc_uniform_1-100_uniform_0.5-1.sh"

sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&1+1[10000]_p2p-Gnutella08_uniform_1-100_const_0.75.sh"
sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&1+1[10000]_p2p-Gnutella08_uniform_1-100_uniform_0.5-1.sh"

sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&1+1[10000]_p2p-Gnutella06_uniform_1-100_const_0.75.sh"
sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&1+1[10000]_p2p-Gnutella06_uniform_1-100_uniform_0.5-1.sh"


#sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&doerr1+1[3;10000]_barabasi_albert_uniform_1-100_const_0.75.sh"
#sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&doerr1+1[3;10000]_barabasi_albert_uniform_1-100_uniform_0.5-1.sh"

sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-1 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&doerr1+1[3;10000]_facebook_combined_uniform_1-100_const_0.75.sh"
sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-1 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&doerr1+1[3;10000]_facebook_combined_uniform_1-100_uniform_0.5-1.sh"

#sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&doerr1+1[3;10000]_watts_strogatz_uniform_1-100_const_0.75.sh"
#sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&doerr1+1[3;10000]_watts_strogatz_uniform_1-100_uniform_0.5-1.sh"

sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-1 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&doerr1+1[3;10000]_Wiki-Vote_uniform_1-100_const_0.75.sh"
sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-1 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&doerr1+1[3;10000]_Wiki-Vote_uniform_1-100_uniform_0.5-1.sh"

sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-1 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&doerr1+1[3;10000]_ca-GrQc_uniform_1-100_const_0.75.sh"
sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-1 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&doerr1+1[3;10000]_ca-GrQc_uniform_1-100_uniform_0.5-1.sh"

sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-1 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&doerr1+1[3;10000]_p2p-Gnutella08_uniform_1-100_const_0.75.sh"
sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-1 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&doerr1+1[3;10000]_p2p-Gnutella08_uniform_1-100_uniform_0.5-1.sh"

sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-1 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&doerr1+1[3;10000]_p2p-Gnutella06_uniform_1-100_const_0.75.sh"
sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-1 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&doerr1+1[3;10000]_p2p-Gnutella06_uniform_1-100_uniform_0.5-1.sh"

#sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&iter_descent[10000, 1]_barabasi_albert_uniform_1-100_const_0.75.sh"
#sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&iter_descent[10000, 1]_barabasi_albert_uniform_1-100_uniform_0.5-1.sh"

sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-1 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&iter_descent[10000, 1]_facebook_combined_uniform_1-100_const_0.75.sh"
sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-1 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&iter_descent[10000, 1]_facebook_combined_uniform_1-100_uniform_0.5-1.sh"

#sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&iter_descent[10000, 1]_watts_strogatz_uniform_1-100_const_0.75.sh"
#sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&iter_descent[10000, 1]_watts_strogatz_uniform_1-100_uniform_0.5-1.sh"

sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-1 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&iter_descent[10000, 1]_Wiki-Vote_uniform_1-100_const_0.75.sh"
sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-1 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&iter_descent[10000, 1]_Wiki-Vote_uniform_1-100_uniform_0.5-1.sh"

sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-1 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&iter_descent[10000, 1]_ca-GrQc_uniform_1-100_const_0.75.sh"
sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-1 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&iter_descent[10000, 1]_ca-GrQc_uniform_1-100_uniform_0.5-1.sh"

sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-1 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&iter_descent[10000, 1]_p2p-Gnutella08_uniform_1-100_const_0.75.sh"
sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-1 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&iter_descent[10000, 1]_p2p-Gnutella08_uniform_1-100_uniform_0.5-1.sh"

sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-1 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&iter_descent[10000, 1]_p2p-Gnutella06_uniform_1-100_const_0.75.sh"
sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-1 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&iter_descent[10000, 1]_p2p-Gnutella06_uniform_1-100_uniform_0.5-1.sh"

#sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&iter_descent[10000, 2]_barabasi_albert_uniform_1-100_const_0.75.sh"
#sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&iter_descent[10000, 2]_barabasi_albert_uniform_1-100_uniform_0.5-1.sh"

#sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&iter_descent[10000, 2]_facebook_combined_uniform_1-100_const_0.75.sh"
#sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&iter_descent[10000, 2]_facebook_combined_uniform_1-100_uniform_0.5-1.sh"

#sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&iter_descent[10000, 2]_watts_strogatz_uniform_1-100_const_0.75.sh"
#sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&iter_descent[10000, 2]_watts_strogatz_uniform_1-100_uniform_0.5-1.sh"

#sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&iter_descent[10000, 2]_Wiki-Vote_uniform_1-100_const_0.75.sh"
#sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&iter_descent[10000, 2]_Wiki-Vote_uniform_1-100_uniform_0.5-1.sh"
#
#
##
##sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-1 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&iter_descent[10000, 5]_barabasi_albert_uniform_1-100_const_0.75.sh"
##sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-1 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&iter_descent[10000, 5]_barabasi_albert_uniform_1-100_uniform_0.5-1.sh"
#
#sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-1 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&iter_descent[10000, 5]_facebook_combined_uniform_1-100_const_0.75.sh"
#sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-1 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&iter_descent[10000, 5]_facebook_combined_uniform_1-100_uniform_0.5-1.sh"
##
##sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-1 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&iter_descent[10000, 5]_watts_strogatz_uniform_1-100_const_0.75.sh"
##sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-1 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&iter_descent[10000, 5]_watts_strogatz_uniform_1-100_uniform_0.5-1.sh"
#
#sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-1 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&iter_descent[10000, 5]_Wiki-Vote_uniform_1-100_const_0.75.sh"
#sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-1 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&iter_descent[10000, 5]_Wiki-Vote_uniform_1-100_uniform_0.5-1.sh"



#sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-1 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg_barabasi_albert_uniform_1-100_const_0.75.sh"
#sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-1 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg_barabasi_albert_uniform_1-100_uniform_0.5-1.sh"

sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-1 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg_facebook_combined_uniform_1-100_const_0.75.sh"
sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-1 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg_facebook_combined_uniform_1-100_uniform_0.5-1.sh"

#sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-1 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg_watts_strogatz_uniform_1-100_const_0.75.sh"
#sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-1 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg_watts_strogatz_uniform_1-100_uniform_0.5-1.sh"

sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-1 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg_Wiki-Vote_uniform_1-100_const_0.75.sh"
sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-1 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg_Wiki-Vote_uniform_1-100_uniform_0.5-1.sh"

sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg_ca-GrQc_uniform_1-100_const_0.75.sh"
sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg_ca-GrQc_uniform_1-100_uniform_0.5-1.sh"

sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg_p2p-Gnutella08_uniform_1-100_const_0.75.sh"
sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg_p2p-Gnutella08_uniform_1-100_uniform_0.5-1.sh"

sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg_p2p-Gnutella06_uniform_1-100_const_0.75.sh"
sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg_p2p-Gnutella06_uniform_1-100_uniform_0.5-1.sh"



sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&iter_descent_v2[10000, 1]_facebook_combined_uniform_1-100_const_0.75.sh"
sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&iter_descent_v2[10000, 1]_facebook_combined_uniform_1-100_uniform_0.5-1.sh"

#sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&iter_descent[10000, 1]_watts_strogatz_uniform_1-100_const_0.75.sh"
#sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&iter_descent[10000, 1]_watts_strogatz_uniform_1-100_uniform_0.5-1.sh"

sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&iter_descent_v2[10000, 1]_Wiki-Vote_uniform_1-100_const_0.75.sh"
sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&iter_descent_v2[10000, 1]_Wiki-Vote_uniform_1-100_uniform_0.5-1.sh"

sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&iter_descent_v2[10000, 1]_ca-GrQc_uniform_1-100_const_0.75.sh"
sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&iter_descent_v2[10000, 1]_ca-GrQc_uniform_1-100_uniform_0.5-1.sh"

sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&iter_descent_v2[10000, 1]_p2p-Gnutella08_uniform_1-100_const_0.75.sh"
sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&iter_descent_v2[10000, 1]_p2p-Gnutella08_uniform_1-100_uniform_0.5-1.sh"

sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&iter_descent_v2[10000, 1]_p2p-Gnutella06_uniform_1-100_const_0.75.sh"
sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&iter_descent_v2[10000, 1]_p2p-Gnutella06_uniform_1-100_uniform_0.5-1.sh"



sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&iter_descent_v3[10000, 1]_facebook_combined_uniform_1-100_const_0.75.sh"
sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&iter_descent_v3[10000, 1]_facebook_combined_uniform_1-100_uniform_0.5-1.sh"

#sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&iter_descent[10000, 1]_watts_strogatz_uniform_1-100_const_0.75.sh"
#sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&iter_descent[10000, 1]_watts_strogatz_uniform_1-100_uniform_0.5-1.sh"

sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&iter_descent_v3[10000, 1]_Wiki-Vote_uniform_1-100_const_0.75.sh"
sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&iter_descent_v3[10000, 1]_Wiki-Vote_uniform_1-100_uniform_0.5-1.sh"

sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&iter_descent_v3[10000, 1]_ca-GrQc_uniform_1-100_const_0.75.sh"
sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&iter_descent_v3[10000, 1]_ca-GrQc_uniform_1-100_uniform_0.5-1.sh"

sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&iter_descent_v3[10000, 1]_p2p-Gnutella08_uniform_1-100_const_0.75.sh"
sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&iter_descent_v3[10000, 1]_p2p-Gnutella08_uniform_1-100_uniform_0.5-1.sh"

sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&iter_descent_v3[10000, 1]_p2p-Gnutella06_uniform_1-100_const_0.75.sh"
sbatch --cpus-per-task=2 --mem=20G --time=20:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "./tdg&iter_descent_v3[10000, 1]_p2p-Gnutella06_uniform_1-100_uniform_0.5-1.sh"

