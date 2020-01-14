
class Matrix:
    
    # constructors
    # Postcondition: new matrix instance is created
    # Parameters: height - height of the matrix to be created
    #             width - width of the matrix 
    def __init__(self, height=0, width=0):
        self.height = height
        self.width = width
        self.matrix = self.__set_matrix()

    # private instance methods
    # Postcondition: matrix is instantiated with all values set to 0
    # Returns: matrix of zeroes with given height and width
    def __set_matrix (self):
        matrix = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(0)
            matrix.append(row)
        return matrix

    # public instance methods

    # Preconditions: row number must be valid (raises IndexError otherwise)
    #                value_list must be a list with correct number of entries
    #                   (raises ValueError otherwise)
    # Parameters: row_num - row to be replaced
    #             value_list - list of values to replace row in matrix
    # Postcondition: requested row is replaced with new row of values
    # Errors: raises IndexError if row number is out of bounds
    #         raises ValueError if list isn't passed or 
    #         list is incorrect size
    def set_row(self, row_num, value_list):
        if (row_num > self.height or row_num <= 0):
            raise IndexError("invalid row number")

        if (not (type(value_list) is list)):
            raise ValueError("passed type must be list")

        if (len(value_list) != self.width):
            raise ValueError("list is incorrect size")

        row_num_fixed = row_num - 1
        self.matrix.pop(row_num_fixed)
        self.matrix.insert(row_num_fixed, value_list)

    # Precondition: matrix_other must have same dimensions 
    #               as matrix add_matrix is called from
    #               (ValueError is raised otherwise)
    # Parameters: matrix_other - matrix to be added
    # Returns: matrix that is the sum of the two matrices
    # Errors: raises ValueError if matrices aren't equal in dimension
    def add_matrix(self, matrix_other):
        if (not self.is_addable(matrix_other)):
            raise ValueError("matrices must have equal dimensions to be added")
        
        sum_matrix = Matrix(self.height, self.width)
        for i in range(self.height):
            
            row_sum = []
            for j in range(self.width):
                sum = self.matrix[i][j] + matrix_other.matrix[i][j]
                row_sum.append(sum)
            sum_matrix.set_row(i + 1, row_sum)

        return sum_matrix

    # Returns: True if matrices has same dimensions
    #          False otherwise
    def is_addable(self, matrix_other):
        if (self.height != matrix_other.height or self.width != matrix_other.width):
            return False
        else:
            return True

    # Parameter: scalar - number to be multipled with matrix
    # Returns: Matrix that represents product of original matrix and scalar
    def multiply_by_scalar(self, scalar):
        scalar_matrix = Matrix(self.height, self.width)

        for i in range(self.height):
            
            row_product = []
            for j in range(self.width):
                product = self.matrix[i][j] * scalar
                row_product.append(product)
            scalar_matrix.set_row(i + 1, row_product)

        return scalar_matrix

    # Parameter: matrix_other - matrix to be subtracted
    # Returns: matrix that is a result of subtracting the two matrices
    def subtract_matrix(self, matrix_other):
        return self.add_matrix(matrix_other.multiply_by_scalar(-1))

    # Precondition: width of first matrix must equal height of second matrix
    #               raised ValueError otherwise
    # Parameter: matrix_other - matrix to be multiplied with original matrix
    # Returns: matrix that represents product of the two matrices
    # Errors: raises ValueError if width of first matrix != height of other matrix
    def multiply_matrix(self, matrix_other):
        if (self.width != matrix_other.height):
            raise ValueError("width of first matrix must equal height of second matrix")

        product_matrix = Matrix(self.height, matrix_other.width)
        for i in range(product_matrix.height):
            row_product = []
            for j in range(product_matrix.width):
                sum_of_products = 0
                for k in range(self.width):
                    sum_of_products += (self.matrix[i][k] *
                                        matrix_other.matrix[k][j])
                row_product.append(sum_of_products)
            product_matrix.set_row(i + 1, row_product)
        return product_matrix

    # Returns: true if matrix is invertible, false otherwise
    # Errors: Allows ValueError for self.get_determinant()
    def is_invertible(self):
        try:
            self.get_determinant()
        except:
            return False
        else:
            return (self.get_determinant() != 0)

    # Returns: determinant for matrix
    # Errors: raises ValueError is matrix isn't n x n
    def get_determinant(self):
        if (self.height != self.width):
            raise ValueError("determinant can only be" + 
                             " calcuated for square matrices")

        if (self.height == 2):
            return ((self.matrix[0][0] * self.matrix[1][1]) - 
                     (self.matrix[0][1] * self.matrix[1][0]))
        
        determinant = 0
        sign = 1
        for i in range(self.width):
            
            reduced_matrix = Matrix(self.width - 1, self.height - 1)
            for j in range(1, self.height):

                matrix_row = []
                for k in range(self.width):
                    if (k != i):
                        matrix_row.append(self.matrix[j][k])     
                reduced_matrix.set_row(j, matrix_row)
            determinant += sign*self.matrix[0][i] * reduced_matrix.get_determinant()
            sign *= -1
        return determinant

    # Precondition: matrix get_inverse is called on must be invertible
    # Returns: inverse of original matrix
    # Errors: raises ValueError if matrix is not invertible
    def get_inverse(self):

        if (not self.is_invertible()):
            raise ValueError("Matrix is not invertible")

        # first we find the matrix of minors
        matrix_of_minors = self.get_matrix_of_minors()

        # next we find the matrix of cofactors from the matrix of minors
        matrix_of_cofactors = matrix_of_minors.get_matrix_of_cofactors()

        # now we must find the adjugate matrix by transposing cofactor matrix
        adjugate_matrix = matrix_of_cofactors.get_transposition()

        # lastly we must multiply by the reciprocal of the determinant 
        # of the original matrix
        inverse_matrix = adjugate_matrix.multiply_by_scalar(1/self.get_determinant())
        return inverse_matrix

    # Precondition: matrix get_matrix_of_minors is called on must be invertible
    # Returns: matrix of minors of original matrix
    # Errors: raises ValueError if matrix is not invertible
    def get_matrix_of_minors(self):
        if (not self.is_invertible()):
            raise ValueError("Matrix must be invertible")       

        matrix_of_minors = Matrix(self.height, self.width)
        for i in range(self.height):

            minor_matrix_row = []
            for j in range(self.width):
            
                temp_matrix = Matrix(self.height-1, self.width-1)
                for k in range(self.height):
                    if (k != i):

                        temp_matrix_row = []
                        for h in range(self.width):
                            if (h != j):
                                temp_matrix_row.append(self.matrix[k][h])
                        if (k < i):
                            temp_matrix.set_row(k+1, temp_matrix_row)
                        else:
                            temp_matrix.set_row(k, temp_matrix_row)
                minor_matrix_row.append(temp_matrix.get_determinant())
            matrix_of_minors.set_row(i+1, minor_matrix_row)
        return matrix_of_minors

    # Returns: matrix of cofactors of original matrix
    def get_matrix_of_cofactors(self):
        sign = 1
        matrix_of_cofactors = Matrix(self.height, self.width)
        for i in range(self.height):
            cofactor_row = []
            for j in range(self.width):
                cofactor_row.append(sign*self.matrix[i][j])
                sign *= -1
            matrix_of_cofactors.set_row(i+1, cofactor_row)
        return matrix_of_cofactors

    # Precondition: Matrix must be a square to be transposed
    # (This isn't always true and transposition for other matrices will be added later)
    # Returns: transposition of original matrix
    # Errors: raises ValueError if matrix is not square
    def get_transposition(self):
        if (self.height != self.width):
            raise ValueError("must be a square matrix")

        transposition_matrix = Matrix(self.height, self.width)
        for i in range(self.height):
            transposition_row = []

            for j in range(self.width):
                transposition_row.append(self.matrix[j][i])
            transposition_matrix.set_row(i+1, transposition_row)
        return transposition_matrix