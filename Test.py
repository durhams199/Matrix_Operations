import unittest
from Matrix import *


class TestMatrixConstruction(unittest.TestCase):
    def setUp(self):
        self.test_matrix = Matrix(3,2)
        self.blank_matrix = Matrix()
        self.test_matrix.set_row(1, [1,2])

    def test_empty_matrix(self):
        self.assertEqual(self.blank_matrix.height, 0)
        self.assertEqual(self.blank_matrix.width, 0)
        self.assertEqual(self.blank_matrix.matrix, [])

    def test_matrix_size(self):
        self.assertEqual(self.test_matrix.height, 3)
        self.assertEqual(self.test_matrix.width, 2)

    def test_default_values(self):
        self.assertEqual(self.test_matrix.matrix[1], [0,0])

    def test_set_row_values(self):
        self.assertEqual(self.test_matrix.matrix[0], [1,2])

if __name__ == '__main__':
    unittest.main()