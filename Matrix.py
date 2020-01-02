
class Matrix:
   
    def __init__(self, height=0, width=0):
        self.height = height
        self.width = width
        self.matrix = self.__set_matrix()

    def __set_matrix (self):
        matrix = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                row.append(0)
            matrix.append(row)
        return matrix

    def set_matrix(self, row_num, value_list):
        if (row_num > self.height or row_num <= 0):
            raise IndexError("invalid row number")

        if (not (type(value_list) is list)):
            raise ValueError("passed type must be list")

        if (len(value_list) != self.width):
            raise ValueError("list is incorrect size")

        row_num_fixed = row_num - 1
        self.matrix.pop(row_num_fixed)
        self.matrix.insert(row_num_fixed, value_list)

