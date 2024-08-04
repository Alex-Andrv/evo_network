from dltm import DLTM, write_dltm


def generate():
    # ca-GrQc
    (write_dltm(DLTM()
                .read_graph_as_edge_list('samples/ca-GrQc.txt', True)
                .generate_uniformly_random_influences(1, 100, seed=123)
                .generate_proportional_thresholds(0.8), "generated_graph/ca-GrQc_uniform_1-100_const_0.75"))
    (write_dltm(DLTM()
                .read_graph_as_edge_list('samples/ca-GrQc.txt', True)
                .generate_uniformly_random_influences(1, 100, seed=123)
                .generate_uniformly_random_thresholds(0.75, 1, seed=123),
                "generated_graph/ca-GrQc_uniform_1-100_uniform_0.5-1"))

    # p2p-Gnutella06.txt
    (write_dltm(DLTM()
                .read_graph_as_edge_list('samples/p2p-Gnutella06.txt', True)
                .generate_uniformly_random_influences(1, 100, seed=123)
                .generate_proportional_thresholds(0.8), "generated_graph/p2p-Gnutella06_uniform_1-100_const_0.75"))
    (write_dltm(DLTM()
                .read_graph_as_edge_list('samples/p2p-Gnutella06.txt', True)
                .generate_uniformly_random_influences(1, 100, seed=123)
                .generate_uniformly_random_thresholds(0.75, 1, seed=123),
                "generated_graph/p2p-Gnutella06_uniform_1-100_uniform_0.5-1"))

    # p2p-Gnutella08.txt
    (write_dltm(DLTM()
                .read_graph_as_edge_list('samples/p2p-Gnutella08.txt', True)
                .generate_uniformly_random_influences(1, 100, seed=123)
                .generate_proportional_thresholds(0.8), "generated_graph/p2p-Gnutella08_uniform_1-100_const_0.75"))
    (write_dltm(DLTM()
                .read_graph_as_edge_list('samples/p2p-Gnutella08.txt', True)
                .generate_uniformly_random_influences(1, 100, seed=123)
                .generate_uniformly_random_thresholds(0.75, 1, seed=123),
                "generated_graph/p2p-Gnutella08_uniform_1-100_uniform_0.5-1"))

    # FACEBOOK

    (write_dltm(DLTM()
                .read_graph_as_edge_list('samples/facebook_combined.txt', False)
                .generate_uniformly_random_influences(1, 100, seed=123)
                .generate_proportional_thresholds(0.8), "generated_graph/facebook_combined_uniform_1-100_const_0.75"))

    (write_dltm(DLTM()
                .read_graph_as_edge_list('samples/facebook_combined.txt', False)
                .generate_uniformly_random_influences(1, 100, seed=123)
                .generate_uniformly_random_thresholds(0.75, 1, seed=123),
                "generated_graph/facebook_combined_uniform_1-100_uniform_0.5-1"))

    # WIKI
    (write_dltm(DLTM()
                .read_graph_as_edge_list('samples/Wiki-Vote.txt', True)
                .generate_uniformly_random_influences(1, 100, seed=123)
                .generate_proportional_thresholds(0.8), "generated_graph/Wiki-Vote_uniform_1-100_const_0.75"))

    (write_dltm(DLTM()
                .read_graph_as_edge_list('samples/Wiki-Vote.txt', True)
                .generate_uniformly_random_influences(1, 100, seed=123)
                .generate_uniformly_random_thresholds(0.75, 1, seed=123),
                "generated_graph/Wiki-Vote_uniform_1-100_uniform_0.5-1"))
    # WS
    (write_dltm(DLTM()
                .generate_watts_strogatz_graph(10000, 20, 0.5, seed=123)
                .generate_uniformly_random_influences(1, 100, seed=123)
                .generate_proportional_thresholds(0.8), "generated_graph/watts_strogatz_uniform_1-100_const_0.75"))

    (write_dltm(DLTM()
                .generate_watts_strogatz_graph(10000, 20, 0.5, seed=123)
                .generate_uniformly_random_influences(1, 100, seed=123)
                .generate_uniformly_random_thresholds(0.75, 1, seed=123),
                "generated_graph/watts_strogatz_uniform_1-100_uniform_0.5-1"))

    # BA
    (write_dltm(DLTM()
                .generate_barabasi_albert_graph(10000, 20, seed=123)
                .generate_uniformly_random_influences(1, 100, seed=123)
                .generate_proportional_thresholds(0.8), "generated_graph/barabasi_albert_uniform_1-100_const_0.75"))

    (write_dltm(DLTM()
                .generate_barabasi_albert_graph(10000, 20, seed=123)
                .generate_uniformly_random_influences(1, 100, seed=123)
                .generate_uniformly_random_thresholds(0.75, 1, seed=123),
                "generated_graph/barabasi_albert_uniform_1-100_uniform_0.5-1"))


if __name__ == '__main__':
    generate()
