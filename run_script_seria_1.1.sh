
    sbatch --cpus-per-task=2 --mem=20G -p as --time=60:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "generate/seria_1.1/exact_sat&watts_strogatz&uniform_1-2&uniform_0.75-1&40&8&0.5&123.sh"

    sbatch --cpus-per-task=2 --mem=20G -p as --time=60:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "generate/seria_1.1/exact_sat&barabasi_albert&uniform_1-5&uniform_0.75-1&50&4.sh"

    sbatch --cpus-per-task=2 --mem=20G -p as --time=60:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "generate/seria_1.1/exact_sat&watts_strogatz&uniform_1-2&const_0.8&40&8&0.5&123.sh"

    sbatch --cpus-per-task=2 --mem=20G -p as --time=60:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "generate/seria_1.1/exact_sat&barabasi_albert&uniform_1-5&const_0.8&50&4.sh"

    sbatch --cpus-per-task=2 --mem=20G -p as --time=60:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "generate/seria_1.1/exact_sat_with_enhance_solution[10000]&watts_strogatz&uniform_1-2&uniform_0.75-1&40&8&0.5&123.sh"

    sbatch --cpus-per-task=2 --mem=20G -p as --time=60:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "generate/seria_1.1/exact_sat_with_enhance_solution[10000]&barabasi_albert&uniform_1-5&uniform_0.75-1&50&4.sh"

    sbatch --cpus-per-task=2 --mem=20G -p as --time=60:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "generate/seria_1.1/exact_sat_with_enhance_solution[10000]&watts_strogatz&uniform_1-2&const_0.8&40&8&0.5&123.sh"

    sbatch --cpus-per-task=2 --mem=20G -p as --time=60:00:00 -w orthrus-2 --qos=high_cpu --qos=high_mem --qos=unlim_cpu "generate/seria_1.1/exact_sat_with_enhance_solution[10000]&barabasi_albert&uniform_1-5&const_0.8&50&4.sh"
