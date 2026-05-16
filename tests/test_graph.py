import unittest
from dsa_logic import GRAPH, bfs, dfs


class TestGraphTraversal(unittest.TestCase):

    def test_bfs_from_a(self):
        result = bfs(GRAPH, "A")
        self.assertEqual(result, ["A", "B", "C", "D", "E", "F"])

    def test_dfs_from_a(self):
        result = dfs(GRAPH, "A")
        self.assertEqual(result, ["A", "B", "D", "E", "F", "C"])

    def test_all_nodes_visited_bfs(self):
        result = bfs(GRAPH, "C")
        self.assertEqual(set(result), set(GRAPH.keys()))


if __name__ == "__main__":
    unittest.main()
