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

    def test_add_matrix(self):
        sum_matrix = Matrix(3,3)
        sum_matrix.set_row(1, [2,3,4])
        sum_matrix.set_row(2, [5,6,7])
        sum_matrix.set_row(3, [8,9,10])

        self.assertEqual(self.test_matrix_1.add_matrix(self.test_matrix_2),
                         sum_matrix)

        self.assertEqual(self.test_matrix_2.add_matrix(self.test_matrix_1),
                         sum_matrix)

        sum_matrix_2 = Matrix(2,2)
        self.assertRaises(ValueError, self.test_matrix_1.add_matrix, sum_matrix_2)

    def test_multiply_by_scalar(self):
        mult_matrix_1 = Matrix(3,3)

        mult_matrix_2 = Matrix(3,3)
        mult_matrix_2.set_row(1, [2,4,6])
        mult_matrix_2.set_row(2, [8,10,12])
        mult_matrix_2.set_row(3, [14,16,18])

        mult_matrix_3 = Matrix(3,3)
        mult_matrix_3.set_row(1, [-2,-4,-6])
        mult_matrix_3.set_row(2, [-8,-10,-12])
        mult_matrix_3.set_row(3, [-14,-16,-18])

        self.assertEqual(self.test_matrix_1.multiply_by_scalar(0),
                        mult_matrix_1)
        self.assertEqual(self.test_matrix_1.multiply_by_scalar(1), 
                        self.test_matrix_1)
        self.assertEqual(self.test_matrix_1.multiply_by_scalar(2), 
                        mult_matrix_2)
        self.assertEqual(self.test_matrix_1.multiply_by_scalar(-2), 
                        mult_matrix_3)

    def test_subtract_matrix(self):
        sub_matrix_1 = Matrix(3,3)

        sub_matrix_2 = Matrix(3,3)
        sub_matrix_2.set_row(1, [0,1,2])
        sub_matrix_2.set_row(2, [3,4,5])
        sub_matrix_2.set_row(3, [6,7,8])

        self.assertEqual(self.test_matrix_1.subtract_matrix(sub_matrix_1), 
                        self.test_matrix_1)
        self.assertEqual(self.test_matrix_1.subtract_matrix(self.test_matrix_1), 
                        sub_matrix_1)
        self.assertEqual(self.test_matrix_1.subtract_matrix(self.test_matrix_2), 
                        sub_matrix_2)

    def test_multiply_matrix(self):

        identity_matrix = Matrix(3,3)
        identity_matrix.set_row(1, [1,0,0])
        identity_matrix.set_row(2, [0,1,0])
        identity_matrix.set_row(3, [0,0,1])

        matrix_mult_1 = Matrix(2,3)
        matrix_mult_1.set_row(1, [1,2,-1])
        matrix_mult_1.set_row(2, [2,0,1])

        matrix_mult_2 = Matrix(3,2)
        matrix_mult_2.set_row(1, [3,1])
        matrix_mult_2.set_row(2, [0,-1])
        matrix_mult_2.set_row(3, [-2,3])

        matrix_mult_3 = Matrix(2,2)
        matrix_mult_3.set_row(1, [5,-4])
        matrix_mult_3.set_row(2, [4,5])

        self.assertEqual(matrix_mult_1.multiply_matrix(matrix_mult_2), 
                        matrix_mult_3)
        
        error_matrix = Matrix(4,4)
        self.assertRaises(ValueError, matrix_mult_2.multiply_matrix, 
                        error_matrix)

        self.assertEqual(self.test_matrix_1.multiply_matrix(identity_matrix),
                        self.test_matrix_1)

    def test_get_determinant(self):

        identity_matrix = Matrix(3,3)
        identity_matrix.set_row(1, [1,0,0])
        identity_matrix.set_row(2, [0,1,0])
        identity_matrix.set_row(3, [0,0,1])

        self.assertEqual(identity_matrix.get_determinant(), 1)

        det_matrix_1 = Matrix(2,2)
        det_matrix_1.set_row(1, [3,8])
        det_matrix_1.set_row(2, [4,6])

        self.assertEqual(det_matrix_1.get_determinant(), -14)

        det_matrix_2 = Matrix(3,3)
        det_matrix_2.set_row(1, [4,2,6])
        det_matrix_2.set_row(2, [-1,-4,5])
        det_matrix_2.set_row(3, [3,7,2])

        self.assertEqual(det_matrix_2.get_determinant(), -108)

        det_matrix_3 = Matrix(3,3)
        det_matrix_3.set_row(1, [2,-3,5])
        det_matrix_3.set_row(2, [-3,6,2])
        det_matrix_3.set_row(3, [1,-2,5])

        self.assertEqual(det_matrix_3.get_determinant(), 17)

        det_matrix_4 = Matrix(3,3)
        det_matrix_4.set_row(1, [5,4,7])
        det_matrix_4.set_row(2, [3,-6,5])
        det_matrix_4.set_row(3, [4,2,-3])

        self.assertEqual(det_matrix_4.get_determinant(), 366)

        det_matrix_5 = Matrix(4,4)
        det_matrix_5.set_row(1, [3,2,0,1])
        det_matrix_5.set_row(2, [4,0,1,2])
        det_matrix_5.set_row(3, [3,0,2,1])
        det_matrix_5.set_row(4, [9,2,3,1])

        self.assertEqual(det_matrix_5.get_determinant(), 24)

        error_matrix = Matrix(2,3)
        self.assertRaises(ValueError, error_matrix.get_determinant)



if __name__ == '__main__':
    unittest.main()