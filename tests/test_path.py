import unittest
from ..algorithms import does_path_exist


class TestPath(unittest.TestCase):
    def setUp(self):
        self.graph = {
            "A": set(["B", "C"]),
            "B": set("D"),
            "C": set(["A", "B", "E"]),
            "D": set("F"),
            "E": set(["G", "H"]),
            "F": set(["A"]),
            "G": set(),
            "H": set()
        }
        """
        ⦧-> A <-> C -> E -> H
       /    |    /     |   /
      |     v  ⩗       v ⩗
      |     B          G
      |     |
      |     v
      F <-- D
        """

    def test_does_path_exist_to_itself(self):
        self.assertTrue(does_path_exist(self.graph, "A", "A"))

    def test_does_path_exist_to_adjecent_node(self):
        self.assertTrue(does_path_exist(self.graph, "A", "C"))

    def test_does_path_exist_one_step_away(self):
        self.assertTrue(does_path_exist(self.graph, "A", "D"))

    def test_does_path_exist_more_than_one_step_away(self):
        self.assertTrue(does_path_exist(self.graph, "A", "F"))
        self.assertTrue(does_path_exist(self.graph, "B", "G"))

    def test_does_path_not_exist(self):
        self.assertFalse(does_path_exist(self.graph, "G", "F"))
