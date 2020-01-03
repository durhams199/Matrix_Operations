
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
                print(sum_of_products)
                row_product.append(sum_of_products)
            product_matrix.set_row(i + 1, row_product)
        return product_matrix