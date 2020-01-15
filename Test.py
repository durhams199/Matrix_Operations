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

    def test_set_row_errors(self):
        self.assertRaises(IndexError, self.test_matrix.set_row, 5, [])
        self.assertRaises(IndexError, self.test_matrix.set_row, 5, [])
        self.assertRaises(ValueError, self.test_matrix.set_row, 1, 6)

class TestMatrixMethods(unittest.TestCase):
    def setUp(self):
        self.test_matrix_1 = Matrix(3,3)
        self.test_matrix_1.set_row(1, [1,2,3])
        self.test_matrix_1.set_row(2, [4,5,6])
        self.test_matrix_1.set_row(3, [7,8,9])

        self.test_matrix_2 = Matrix(3,3)
        self.test_matrix_2.set_row(1, [1,1,1])
        self.test_matrix_2.set_row(2, [1,1,1])
        self.test_matrix_2.set_row(3, [1,1,1])

    def test_matrix_addition(self):
        sum_matrix = Matrix(3,3)
        sum_matrix.set_row(1, [2,3,4])
        sum_matrix.set_row(2, [5,6,7])
        sum_matrix.set_row(3, [8,9,10])

        self.assertEqual(self.test_matrix_1.add_matrix(self.test_matrix_2).matrix,
                         sum_matrix.matrix)

        self.assertEqual(self.test_matrix_2.add_matrix(self.test_matrix_1).matrix,
                         sum_matrix.matrix)

if __name__ == '__main__':
    unittest.main()