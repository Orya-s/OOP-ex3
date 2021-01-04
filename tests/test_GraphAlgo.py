from unittest import TestCase

from DiGraph import DiGraph

from GraphAlgo import GraphAlgo


class TestGraphAlgo(TestCase):
    def test_load_and_save_from_json(self):
        graph = self.createGraph()
        ga = GraphAlgo(graph)
        fileName = "graph.json"
        ga.save_to_json(fileName)
        ga.load_from_json(fileName)
        self.assertEqual(graph, ga.graph)
        self.assertEqual(graph.edges, ga.graph.edges)

    def test_shortest_path(self):
        graph = self.createGraph()
        ga = GraphAlgo(graph)
        self.assertEqual((2.0, [4, 1, 2]), ga.shortest_path(4, 2))
        self.assertEqual((0.5, [0, 1]), ga.shortest_path(0, 1))
        self.assertEqual((3.5, [0, 1, 2, 3]), ga.shortest_path(0, 3))

    def test_connected_component(self):
        graph = self.createGraph()
        ga = GraphAlgo(graph)
        print(ga.connected_component(3))
    # def test_connected_components(self):
    #     self.fail()
    #
    # def test_plot_graph(self):
    #     self.fail()

    def createGraph(self):
        g = DiGraph()
        g.add_node(0)
        g.add_node(1)
        g.add_node(2)
        g.add_node(3)
        g.add_node(4)
        g.add_node(5)
        g.add_node(6)
        g.add_edge(0, 1, 0.5)
        g.add_edge(5, 1, 0.5)
        g.add_edge(1, 0, 0.5)
        g.add_edge(5, 4, 0.5)
        g.add_edge(2, 1, 1.5)
        g.add_edge(2, 3, 2.5)
        g.add_edge(4, 1, 1.5)
        g.add_edge(5, 3, 3.5)
        g.add_edge(3, 5, 4)
        g.add_edge(4, 2, 6)
        g.add_edge(1, 2, 0.5)

        return g
