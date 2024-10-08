from dltm import DLTM, write_dltm


def generate():
    # ca-GrQc
    (write_dltm(DLTM()
                .read_graph_as_edge_list('samples/ca-GrQc.txt', True)
                .generate_uniformly_random_influences(1, 1000, seed=123)
                .generate_proportional_thresholds(0.8), "generated_graph/seria_3/ca-GrQc&uniform_1-1000&const_0.8"))
    (write_dltm(DLTM()
                .read_graph_as_edge_list('samples/ca-GrQc.txt', True)
                .generate_uniformly_random_influences(1, 1000, seed=123)
                .generate_uniformly_random_thresholds(0.75, 1, seed=123),
                "generated_graph/seria_3/ca-GrQc&uniform_1-1000&uniform_0.75-1"))

    # p2p-Gnutella06.txt
    (write_dltm(DLTM()
                .read_graph_as_edge_list('samples/p2p-Gnutella06.txt', True)
                .generate_uniformly_random_influences(1, 1000, seed=123)
                .generate_proportional_thresholds(0.8), "generated_graph/seria_3/p2p-Gnutella06&uniform_1-1000&const_0.8"))
    (write_dltm(DLTM()
                .read_graph_as_edge_list('samples/p2p-Gnutella06.txt', True)
                .generate_uniformly_random_influences(1, 1000, seed=123)
                .generate_uniformly_random_thresholds(0.75, 1, seed=123),
                "generated_graph/seria_3/p2p-Gnutella06&uniform_1-1000&uniform_0.75-1"))

    # p2p-Gnutella08.txt
    (write_dltm(DLTM()
                .read_graph_as_edge_list('samples/p2p-Gnutella08.txt', True)
                .generate_uniformly_random_influences(1, 1000, seed=123)
                .generate_proportional_thresholds(0.8), "generated_graph/seria_3/p2p-Gnutella08&uniform_1-1000&const_0.8"))
    (write_dltm(DLTM()
                .read_graph_as_edge_list('samples/p2p-Gnutella08.txt', True)
                .generate_uniformly_random_influences(1, 1000, seed=123)
                .generate_uniformly_random_thresholds(0.75, 1, seed=123),
                "generated_graph/seria_3/p2p-Gnutella08&uniform_1-1000&uniform_0.75-1"))

    # FACEBOOK
    (write_dltm(DLTM()
                .read_graph_as_edge_list('samples/facebook_combined.txt', False)
                .generate_uniformly_random_influences(1, 1000, seed=123)
                .generate_proportional_thresholds(0.8), "generated_graph/seria_3/facebook_combined&uniform_1-1000&const_0.8"))

    (write_dltm(DLTM()
                .read_graph_as_edge_list('samples/facebook_combined.txt', False)
                .generate_uniformly_random_influences(1, 1000, seed=123)
                .generate_uniformly_random_thresholds(0.75, 1, seed=123),
                "generated_graph/seria_3/facebook_combined&uniform_1-1000&uniform_0.75-1"))

    # WIKI
    (write_dltm(DLTM()
                .read_graph_as_edge_list('samples/Wiki-Vote.txt', True)
                .generate_uniformly_random_influences(1, 1000, seed=123)
                .generate_proportional_thresholds(0.8), "generated_graph/seria_3/Wiki-Vote&uniform_1-1000&const_0.8"))

    (write_dltm(DLTM()
                .read_graph_as_edge_list('samples/Wiki-Vote.txt', True)
                .generate_uniformly_random_influences(1, 1000, seed=123)
                .generate_uniformly_random_thresholds(0.75, 1, seed=123),
                "generated_graph/seria_3/Wiki-Vote&uniform_1-1000&uniform_0.75-1"))

    for tr in ["0.5", "0.75", "0.9"]:

        # ca-GrQc
        (write_dltm(DLTM()
                    .read_graph_as_edge_list('samples/ca-GrQc.txt', True)
                    .generate_uniformly_random_influences(1, 1000, seed=123)
                    .generate_proportional_thresholds(0.8), f"generated_graph/seria_2_{tr}/ca-GrQc&uniform_1-1000&const_0.8"))
        (write_dltm(DLTM()
                    .read_graph_as_edge_list('samples/ca-GrQc.txt', True)
                    .generate_uniformly_random_influences(1, 1000, seed=123)
                    .generate_uniformly_random_thresholds(0.75, 1, seed=123),
                    f"generated_graph/seria_2_{tr}/ca-GrQc&uniform_1-1000&uniform_0.75-1"))

        # p2p-Gnutella06.txt
        (write_dltm(DLTM()
                    .read_graph_as_edge_list('samples/p2p-Gnutella06.txt', True)
                    .generate_uniformly_random_influences(1, 1000, seed=123)
                    .generate_proportional_thresholds(0.8), f"generated_graph/seria_2_{tr}/p2p-Gnutella06&uniform_1-1000&const_0.8"))
        (write_dltm(DLTM()
                    .read_graph_as_edge_list('samples/p2p-Gnutella06.txt', True)
                    .generate_uniformly_random_influences(1, 1000, seed=123)
                    .generate_uniformly_random_thresholds(0.75, 1, seed=123),
                    f"generated_graph/seria_2_{tr}/p2p-Gnutella06&uniform_1-1000&uniform_0.75-1"))

        # p2p-Gnutella08.txt
        (write_dltm(DLTM()
                    .read_graph_as_edge_list('samples/p2p-Gnutella08.txt', True)
                    .generate_uniformly_random_influences(1, 1000, seed=123)
                    .generate_proportional_thresholds(0.8), f"generated_graph/seria_2_{tr}/p2p-Gnutella08&uniform_1-1000&const_0.8"))
        (write_dltm(DLTM()
                    .read_graph_as_edge_list('samples/p2p-Gnutella08.txt', True)
                    .generate_uniformly_random_influences(1, 1000, seed=123)
                    .generate_uniformly_random_thresholds(0.75, 1, seed=123),
                    f"generated_graph/seria_2_{tr}/p2p-Gnutella08&uniform_1-1000&uniform_0.75-1"))

        # FACEBOOK
        (write_dltm(DLTM()
                    .read_graph_as_edge_list('samples/facebook_combined.txt', False)
                    .generate_uniformly_random_influences(1, 1000, seed=123)
                    .generate_proportional_thresholds(0.8), f"generated_graph/seria_2_{tr}/facebook_combined&uniform_1-1000&const_0.8"))

        (write_dltm(DLTM()
                    .read_graph_as_edge_list('samples/facebook_combined.txt', False)
                    .generate_uniformly_random_influences(1, 1000, seed=123)
                    .generate_uniformly_random_thresholds(0.75, 1, seed=123),
                   f"generated_graph/seria_2_{tr}/facebook_combined&uniform_1-1000&uniform_0.75-1"))

        # WIKI
        (write_dltm(DLTM()
                    .read_graph_as_edge_list('samples/Wiki-Vote.txt', True)
                    .generate_uniformly_random_influences(1, 1000, seed=123)
                    .generate_proportional_thresholds(0.8), f"generated_graph/seria_2_{tr}/Wiki-Vote&uniform_1-1000&const_0.8"))

        (write_dltm(DLTM()
                    .read_graph_as_edge_list('samples/Wiki-Vote.txt', True)
                    .generate_uniformly_random_influences(1, 1000, seed=123)
                    .generate_uniformly_random_thresholds(0.75, 1, seed=123),
                    f"generated_graph/seria_2_{tr}/Wiki-Vote&uniform_1-1000&uniform_0.75-1"))


        # WIKI
        (write_dltm(DLTM()
                    .read_graph_as_edge_list('samples/Wiki-Vote.txt', True)
                    .generate_uniformly_random_influences(1, 1000, seed=123)
                    .generate_proportional_thresholds(0.8), f"generated_graph/seria_2_{tr}/Wiki-Vote&uniform_1-1000&const_0.8"))

        (write_dltm(DLTM()
                    .read_graph_as_edge_list('samples/Wiki-Vote.txt', True)
                    .generate_uniformly_random_influences(1, 1000, seed=123)
                    .generate_uniformly_random_thresholds(0.75, 1, seed=123),
                    f"generated_graph/seria_2_{tr}/Wiki-Vote&uniform_1-1000&uniform_0.75-1"))



        # WS
        (write_dltm(DLTM()
                    .generate_watts_strogatz_graph(40, 8, 0.5, seed=123)
                    .generate_uniformly_random_influences(1, 2, seed=123)
                    .generate_proportional_thresholds(0.8), 
                    f"generated_graph/seria_1/watts_strogatz&uniform_1-2&const_0.8&40&8&0.5&123"))
        
        (write_dltm(DLTM()
                    .generate_watts_strogatz_graph(40, 8, 0.5, seed=123)
                    .generate_uniformly_random_influences(1, 2, seed=123)
                    .generate_uniformly_random_thresholds(0.75, 1, seed=123), 
                    f"generated_graph/seria_1/watts_strogatz&uniform_1-2&uniform_0.75-1&40&8&0.5&123"))

    # # (write_dltm(DLTM()
    # #             .generate_watts_strogatz_graph(10000, 20, 0.5, seed=123)
    # #             .generate_uniformly_random_influences(1, 100, seed=123)
    # #             .generate_uniformly_random_thresholds(0.75, 1, seed=123),
    # #             "generated_graph/watts_strogatz_uniform_1-100_uniform_0.5-1"))

    # BA
    (write_dltm(DLTM()
                .generate_barabasi_albert_graph(50, 4, seed=123)
                .generate_uniformly_random_influences(1, 5, seed=123)
                .generate_proportional_thresholds(0.8), 
                "generated_graph/seria_1/barabasi_albert&uniform_1-5&const_0.8&50&4"))
    
    (write_dltm(DLTM()
                .generate_barabasi_albert_graph(50, 4, seed=123)
                .generate_uniformly_random_influences(1, 5, seed=123)
                .generate_uniformly_random_thresholds(0.75, 1, seed=123), 
                "generated_graph/seria_1/barabasi_albert&uniform_1-5&uniform_0.75-1&50&4"))

    # (write_dltm(DLTM()
    #             .generate_barabasi_albert_graph(10000, 20, seed=123)
    #             .generate_uniformly_random_influences(1, 100, seed=123)
    #             .generate_uniformly_random_thresholds(0.75, 1, seed=123),
    #             "generated_graph/barabasi_albert_uniform_1-100_uniform_0.5-1"))


if __name__ == '__main__':
    generate()
