import unittest
from Matrix import *

# tests for constructing a matrix instance
class TestMatrixConstruction(unittest.TestCase):
    def setUp(self):
        self.test_matrix = Matrix(3,2)
        self.blank_matrix = Matrix()
        self.test_matrix.set_row(1, [1,2])

    # tests that a matrix instance defaults to an empty matrix
    def test_empty_matrix(self):
        self.assertEqual(self.blank_matrix.height, 0)
        self.assertEqual(self.blank_matrix.width, 0)
        self.assertEqual(self.blank_matrix.matrix, [])

    # tests that height and width of matrix are set correctly
    def test_matrix_size(self):
        self.assertEqual(self.test_matrix.height, 3)
        self.assertEqual(self.test_matrix.width, 2)

    # tests that a values in matrix default to zero
    def test_default_values(self):
        self.assertEqual(self.test_matrix.matrix[1], [0,0])

    # tests that rows are set correctly when set_row() is used
    def test_set_row_values(self):
        self.assertEqual(self.test_matrix.matrix[0], [1,2])

    # tests that errors function correctly when:
    #       - row index is out of bounds
    #       - list size doesn't match width of matrix
    #       - passed type isn't a list
    def test_set_row_errors(self):
        self.assertRaises(IndexError, self.test_matrix.set_row, 5, [1,2])
        self.assertRaises(ValueError, self.test_matrix.set_row, 1, [])
        self.assertRaises(ValueError, self.test_matrix.set_row, 1, 6)

# tests for individual matrix classes
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

    # tests matrix addition
    def test_add_matrix(self):
        # this matrix is the sum of test_matrix_1 and test_matrix_2
        sum_matrix = Matrix(3,3)
        sum_matrix.set_row(1, [2,3,4])
        sum_matrix.set_row(2, [5,6,7])
        sum_matrix.set_row(3, [8,9,10])

        # tests that test_matrix_1 + test_matrix_2 = sum_matrix
        self.assertEqual(self.test_matrix_1.add_matrix(self.test_matrix_2),
                         sum_matrix)

        # tests commutativity (test_matrix_2 + test_matrix_1 = sum_matrix)
        self.assertEqual(self.test_matrix_2.add_matrix(self.test_matrix_1),
                         sum_matrix)

        # tests that matrices of different sizes CANNOT be added
        sum_matrix_2 = Matrix(2,2)
        self.assertRaises(ValueError, self.test_matrix_1.add_matrix, sum_matrix_2)

    # tests scalar multiplication of matrices
    def test_multiply_by_scalar(self):
        # this is a matrix of only zeroes
        mult_matrix_1 = Matrix(3,3)

        # this matrix represents 2*test_matrix_1
        mult_matrix_2 = Matrix(3,3)
        mult_matrix_2.set_row(1, [2,4,6])
        mult_matrix_2.set_row(2, [8,10,12])
        mult_matrix_2.set_row(3, [14,16,18])

        # this matrix represents -2*test_matrix_1
        mult_matrix_3 = Matrix(3,3)
        mult_matrix_3.set_row(1, [-2,-4,-6])
        mult_matrix_3.set_row(2, [-8,-10,-12])
        mult_matrix_3.set_row(3, [-14,-16,-18])

        # tests that 0*test_matrix_1 = mult_matrix_1 (matrix of zeroes)
        self.assertEqual(self.test_matrix_1.multiply_by_scalar(0),
                        mult_matrix_1)
        # tests that 1*test_matrix_1 = test_matrix_1
        self.assertEqual(self.test_matrix_1.multiply_by_scalar(1), 
                        self.test_matrix_1)
        # tests that 2*test_matrix_1 = mult_matrix_2
        self.assertEqual(self.test_matrix_1.multiply_by_scalar(2), 
                        mult_matrix_2)
        # tests that -2*test_matrix_1 = mult_matrix_3
        self.assertEqual(self.test_matrix_1.multiply_by_scalar(-2), 
                        mult_matrix_3)

    # tests matrix subtraction
    def test_subtract_matrix(self):
        # this is a matrix of zeroes
        sub_matrix_1 = Matrix(3,3)

        # this represents test_matrix_1 - test_matrix_2
        sub_matrix_2 = Matrix(3,3)
        sub_matrix_2.set_row(1, [0,1,2])
        sub_matrix_2.set_row(2, [3,4,5])
        sub_matrix_2.set_row(3, [6,7,8])

        # tests that test_matrix_1 - sub_matrix_1 = test_matrix_1
        self.assertEqual(self.test_matrix_1.subtract_matrix(sub_matrix_1), 
                        self.test_matrix_1)
        # tests that test_matrix_1 - test_matrix_1 = sub_matrix_1
        self.assertEqual(self.test_matrix_1.subtract_matrix(self.test_matrix_1), 
                        sub_matrix_1)
        # tests that test_matrix_1 - test_matrix_2 = sub_matrix_1
        self.assertEqual(self.test_matrix_1.subtract_matrix(self.test_matrix_2), 
                        sub_matrix_2)

    # test matrix multiplication
    def test_multiply_matrix(self):

        # this is the identity matrix
        identity_matrix = Matrix(3,3)
        identity_matrix.set_row(1, [1,0,0])
        identity_matrix.set_row(2, [0,1,0])
        identity_matrix.set_row(3, [0,0,1])

        # test problem
        matrix_mult_1 = Matrix(2,3)
        matrix_mult_1.set_row(1, [1,2,-1])
        matrix_mult_1.set_row(2, [2,0,1])

        matrix_mult_2 = Matrix(3,2)
        matrix_mult_2.set_row(1, [3,1])
        matrix_mult_2.set_row(2, [0,-1])
        matrix_mult_2.set_row(3, [-2,3])

        # this matrix represents matrix_mult_2 * matrix_mult_3
        matrix_mult_3 = Matrix(2,2)
        matrix_mult_3.set_row(1, [5,-4])
        matrix_mult_3.set_row(2, [4,5])

        # tests if matrix_mult_1 * matrix_mult_2 = matrix_mult_3
        self.assertEqual(matrix_mult_1.multiply_matrix(matrix_mult_2), 
                        matrix_mult_3)
        
        # tests that matrices cannot be multiplied if width of first matrix
        # != height of second matrix
        error_matrix = Matrix(4,4)
        self.assertRaises(ValueError, matrix_mult_2.multiply_matrix, 
                        error_matrix)

        # tests that multiplying matrix by the identity returns original matrix
        self.assertEqual(self.test_matrix_1.multiply_matrix(identity_matrix),
                        self.test_matrix_1)

    # tests getting determinant of matrix
    def test_get_determinant(self):
        # represents identity matrix
        identity_matrix = Matrix(3,3)
        identity_matrix.set_row(1, [1,0,0])
        identity_matrix.set_row(2, [0,1,0])
        identity_matrix.set_row(3, [0,0,1])

        # tests that determinant of identity matrix is 1
        self.assertEqual(identity_matrix.get_determinant(), 1)

        # determinant test for 2x2 matrix
        det_matrix_1 = Matrix(2,2)
        det_matrix_1.set_row(1, [3,8])
        det_matrix_1.set_row(2, [4,6])

        self.assertEqual(det_matrix_1.get_determinant(), -14)

        # first determinant test for 3x3 matrix
        det_matrix_2 = Matrix(3,3)
        det_matrix_2.set_row(1, [4,2,6])
        det_matrix_2.set_row(2, [-1,-4,5])
        det_matrix_2.set_row(3, [3,7,2])

        self.assertEqual(det_matrix_2.get_determinant(), -108)

        # second determinant test for 3x3 matrix
        det_matrix_3 = Matrix(3,3)
        det_matrix_3.set_row(1, [2,-3,5])
        det_matrix_3.set_row(2, [-3,6,2])
        det_matrix_3.set_row(3, [1,-2,5])

        self.assertEqual(det_matrix_3.get_determinant(), 17)

        # third determinant test for 3x3 matrix
        det_matrix_4 = Matrix(3,3)
        det_matrix_4.set_row(1, [5,4,7])
        det_matrix_4.set_row(2, [3,-6,5])
        det_matrix_4.set_row(3, [4,2,-3])

        self.assertEqual(det_matrix_4.get_determinant(), 366)

        # determinant test for 4x4 matrix
        det_matrix_5 = Matrix(4,4)
        det_matrix_5.set_row(1, [3,2,0,1])
        det_matrix_5.set_row(2, [4,0,1,2])
        det_matrix_5.set_row(3, [3,0,2,1])
        det_matrix_5.set_row(4, [9,2,3,1])

        self.assertEqual(det_matrix_5.get_determinant(), 24)

        # tests that matrix must be square to find determinant
        error_matrix = Matrix(2,3)
        self.assertRaises(ValueError, error_matrix.get_determinant)

    # tests finding inverse of matrix
    def test_get_inverse(self):

        # represents identity matrix
        identity_matrix = Matrix(3,3)
        identity_matrix.set_row(1, [1,0,0])
        identity_matrix.set_row(2, [0,1,0])
        identity_matrix.set_row(3, [0,0,1])

        # first matrix inverse test
        test_matrix_1 = Matrix(3,3)
        test_matrix_1.set_row(1,[3,0,2])
        test_matrix_1.set_row(2,[2,0,-2])
        test_matrix_1.set_row(3,[0,1,1])

        # result of finding inverse
        test_inv_1 = test_matrix_1.get_inverse()

        # tests that test_inv_1 is the valid inverse of test_matrix_1
        self.assertEqual(test_inv_1.multiply_matrix(test_matrix_1),
                        identity_matrix)
        
        # test commutativity of inverse
        self.assertEqual(test_matrix_1.multiply_matrix(test_inv_1),
                        identity_matrix)

        # second matrix inverse test
        test_matrix_2 = Matrix(3,3)
        test_matrix_2.set_row(1,[1,0,4])
        test_matrix_2.set_row(2,[1,1,6])
        test_matrix_2.set_row(3,[-3,0,-10])

        # result of finding inverse
        test_inv_2 = test_matrix_2.get_inverse()

        # tests that test_inv_2 is the valid inverse of test_matrix_2    
        self.assertEqual(test_inv_2.multiply_matrix(test_matrix_2),
                        identity_matrix)

        # test commutativity of inverse
        self.assertEqual(test_matrix_2.multiply_matrix(test_inv_2),
                        identity_matrix)

        # tests that finding inverse of non square matrice raises error
        error_matrix = Matrix(2,3)
        self.assertRaises(ValueError, error_matrix.get_inverse)


if __name__ == '__main__':
    unittest.main()