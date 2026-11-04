import unittest
from src.tsp_reference import solve

class ReferenceTests(unittest.TestCase):
    def test_known_instance(self):
        matrix = [[0, 10, 15, 20], [10, 0, 35, 25], [15, 35, 0, 30], [20, 25, 30, 0]]
        found = solve(matrix)
        self.assertEqual(found["cost"], 80)
        self.assertEqual(found["route"][0], 0)
        self.assertEqual(found["route"][-1], 0)

    def test_invalid_shape(self):
        with self.assertRaises(ValueError):
            solve([[0, 1], [1]])

    def test_limit(self):
        with self.assertRaises(ValueError):
            solve([[0] * 11 for _ in range(11)])

if __name__ == "__main__":
    unittest.main()
