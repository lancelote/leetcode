from src.design_graph_with_shortest_path_calculator import Graph


def test_graph():
    g = Graph(4, [[0, 2, 5], [0, 1, 2], [1, 2, 1], [3, 0, 3]])

    assert g.shortestPath(3, 2) == 6
    assert g.shortestPath(0, 3) == -1

    g.addEdge([1, 3, 4])

    assert g.shortestPath(0, 3) == 6
