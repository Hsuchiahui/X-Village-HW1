import random

from copy import deepcopy


class Matrix:

    def __init__(self, nrows, ncols):
        """Construct a (nrows X ncols) matrix"""
        self.matrix_list = [[random.randrange(10) for j in range(ncols)] for i in range(nrows)]
        self.row = nrows
        self.col = ncols



    def add(self, m):
        """return a new Matrix object after summation"""
        if self.col == m.col and self.row == m.row:
            result_matrix = Matrix(self.row, self.col)
            for i in range(self.row):
                for j in range(self.col):
                    result_matrix.matrix_list[i][j] = self.matrix_list[i][j] + m.matrix_list[i][j]
            return result_matrix

    def sub(self, m):
        """return a new Matrix object after substraction"""
        if self.col == m.col and self.row == m.row:
            result_matrix = Matrix(self.row, self.col)
            for i in range(self.row):
                for j in range(self.col):
                    result_matrix.matrix_list[i][j] = self.matrix_list[i][j] - m.matrix_list[i][j]
            return result_matrix

    def mul(self, m):
        """return a new Matrix object after multiplication"""
        if self.col == m.row :
            result_matrix = Matrix(self.row, m.col) 
            for i in range(self.row):
                for j in range(m.col):
                    tmp = 0
                    for k in range(self.col):
                        tmp += self.matrix_list[i][k] * m.matrix_list[k][j]
                    result_matrix.matrix_list[i][j] = tmp
            return result_matrix
    def transpose(self):
        """return a new Matrix object after transpose"""
        result_matrix = Matrix(self.row, self.col)
        for i in range(self.row):
            for j in range(self.col):
                result_matrix.matrix_list[j][i] = self.matrix_list[i][j] 
        return result_matrix

    
    def display(self):
        """Display the content in the matrix"""
        for i in range(self.row):
            for j in range(self.col):
                print(self.matrix_list[i][j],end=' ')
            print()


a_row = int(input("Enter a matrix's rows:"))
a_col = int(input("Enter a matrix's cols:"))
b_row = int(input("Enter a matrix's rows:"))
b_col = int(input("Enter a matrix's cols:"))
matrix_a = Matrix(a_row,a_col)
matrix_b = Matrix(b_row,b_col)
print("===== display matrix A =====")
matrix_a.display()

print("===== display matrix B =====")
matrix_b.display()

print("===== display matrix A+B =====")
matrix_a.add(matrix_b).display()

print("===== display matrix A-B =====")
matrix_a.sub(matrix_b).display()

print("===== display matrix A*B =====")
result = matrix_a.mul(matrix_b)
result.display()

print("===== display transpose matrix A*B =====")
result.transpose().display()

