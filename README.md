# Matrix_Operations
 This is a Python implementation of matrices. This class includes:
 1. Creating a matrix
 2. Basic matrix operations such as:
 - addition
 - subtraction
 - multplying by a constant
 - multiplying matrices
 3. Determining if a matrix is invertible
 4. Inverting matrices
 5. Calculating the determinant of a matrix

## Installation
  \>= Python 3.6.4 is the only requirement

## Usage
 In order to run tests of class constructor and methods use:
> py Test.py
### Creating a Matrix:
 In order to create a matrix you can assign it in the following way:
> matrix_1 = Matrix(a,b)
 
 where "a" is the height of the matrix and "y" is the width.
 This will create an a x b matrix where all values are "0"
### Editing values:
 You can change values by using the set_row method in the following way:
> matrix_1.set_row(a, [x, y, z])
 
 where a is the row number (from 1 to the height), and [x,y,z] is a list of values where size of list = width

### List of all current methods in Matrix class (note: these methods can only be called from a matrix instance):

---
> set_row(self, row_num, value_list)
- sets the matrix's row at row_num with the values listed in value_list, where value_list is a list of numbers
---
> add_matrix(self, matrix_other)
- returns the result of adding matrix to matrix_other
- (note: matrices must be the same size)
---
> is_addable(self, matrix_other)
- used by add_matrix(), tests to see if matrices are addable by comparing sizes
- returns true or false
---
> multiply_by_scalar(self, scalar)
- returns result of multiplying matrix by "scalar", where scalar is a valid number
---
> subtract_matrix(self, matrix_other)
- returns result of subtracting matrix_other from matrix
---
> multiply_matrix(self, matrix_other)
- returns result of multiplying matrix by matrix_other 
- (note: width of matrix must equal height of matrix_other)
---
> is_invertible(self)
- checks that matrix is invertible by determining if determinant of matrix != 0
- returns true or false
---
> get_determinant(self)
- returns determinant value for matrix.
- (note: can only be called on square matrices)
---
> get_inverse(self)
- returns inverse of matrix such that (matrix * inverse = inverse * matrix = identity matrix)
- (note: matrix must be invertible to use this method)
---
> get_matrix_of_minors(self)
- returns matrix of minors for matrix method is called from
- (note: matrix must be invertible)
---
> get_matrix_of_cofactors(self)
- returns matrix of cofactors for matrix method is called from 
---
> get_transposition(self)
- returns transposition of matrix 
- (note: matrix must be square)
---

 This class will be used in a online calculator used to visualize all of these operations

