from typing import List
from DiGraph import DiGraph
import json

from GraphAlgoInterface import GraphAlgoInterface


class GraphAlgo(GraphAlgoInterface):

    def __init__(self, g: DiGraph = None):
        self.graph = g

    def get_graph(self) -> DiGraph:
        return self.graph

    def load_from_json(self, file_name: str) -> bool:
        with open(file_name, 'r') as json_path:
            graph = json.load(json_path)
            print(graph)

    def save_to_json(self, file_name: str) -> bool:
        dict = {}
        edgeload = []
        vertices = []
        for edgeKey in self.graph.edges:
            temp = {}
            srcDest = edgeKey.split("-->")
            temp["src"] = int(srcDest[0])
            temp["w"] = self.graph.edges[edgeKey]
            temp["dest"] = int(srcDest[1])
            edgeload.append(temp)

        for nodeKey in self.graph.nodes:
            temp = {"id": nodeKey, "pos": self.graph.getNode(nodeKey).pos}
            vertices.append(temp)

        dict["Edges"] = edgeload
        dict["Nodes"] = vertices

        with open(file_name, 'w') as json_path:
            json.dump(dict, json_path)
        return True

    def shortest_path(self, id1: int, id2: int) -> (float, list):
        pass

    def connected_component(self, id1: int) -> list:
        pass

    def connected_components(self) -> List[list]:
        pass

    def plot_graph(self) -> None:
        pass
