
    sbatch --cpus-per-task=2 --mem=20G -p as --time=20:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "gen_exact_sat_barabasi_albert_50_4_uniform_1-100_const_0.8.sh"

    sbatch --cpus-per-task=2 --mem=20G -p as --time=20:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "gen_exact_sat_barabasi_albert_50_4_uniform_1-100_uniform_0.75-1.sh"

    sbatch --cpus-per-task=2 --mem=20G -p as --time=20:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "gen_exact_sat_watts_strogatz_50_8_0.5_123_uniform_1-100_const_0.8.sh"

    sbatch --cpus-per-task=2 --mem=20G -p as --time=20:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "gen_exact_sat_watts_strogatz_50_8_0.5_123_uniform_1-100_uniform_0.75-1.sh"

    sbatch --cpus-per-task=2 --mem=20G -p as --time=20:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "gen_tdg_barabasi_albert_50_4_uniform_1-100_const_0.8.sh"

    sbatch --cpus-per-task=2 --mem=20G -p as --time=20:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "gen_tdg_barabasi_albert_50_4_uniform_1-100_uniform_0.75-1.sh"

    sbatch --cpus-per-task=2 --mem=20G -p as --time=20:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "gen_tdg_watts_strogatz_50_8_0.5_123_uniform_1-100_const_0.8.sh"

    sbatch --cpus-per-task=2 --mem=20G -p as --time=20:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "gen_tdg_watts_strogatz_50_8_0.5_123_uniform_1-100_uniform_0.75-1.sh"

    sbatch --cpus-per-task=2 --mem=20G -p as --time=20:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "gen_1+1[10000]_barabasi_albert_50_4_uniform_1-100_const_0.8.sh"

    sbatch --cpus-per-task=2 --mem=20G -p as --time=20:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "gen_1+1[10000]_barabasi_albert_50_4_uniform_1-100_uniform_0.75-1.sh"

    sbatch --cpus-per-task=2 --mem=20G -p as --time=20:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "gen_1+1[10000]_watts_strogatz_50_8_0.5_123_uniform_1-100_const_0.8.sh"

    sbatch --cpus-per-task=2 --mem=20G -p as --time=20:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "gen_1+1[10000]_watts_strogatz_50_8_0.5_123_uniform_1-100_uniform_0.75-1.sh"

    sbatch --cpus-per-task=2 --mem=20G -p as --time=20:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "gen_tdg&1+1[10000]_barabasi_albert_50_4_uniform_1-100_const_0.8.sh"

    sbatch --cpus-per-task=2 --mem=20G -p as --time=20:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "gen_tdg&1+1[10000]_barabasi_albert_50_4_uniform_1-100_uniform_0.75-1.sh"

    sbatch --cpus-per-task=2 --mem=20G -p as --time=20:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "gen_tdg&1+1[10000]_watts_strogatz_50_8_0.5_123_uniform_1-100_const_0.8.sh"

    sbatch --cpus-per-task=2 --mem=20G -p as --time=20:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "gen_tdg&1+1[10000]_watts_strogatz_50_8_0.5_123_uniform_1-100_uniform_0.75-1.sh"
