import random
import numpy as np

class Matrix():
    def __init__(self):
        self.matrix = []
        
    def generate_matrix(self, row, column):
        self.row = row
        self.column = column
        self.row_data = []
        for r in range(self.row):
            row_data = []
            for c in range(self.column):
                row_data.append(random.randint(1, 100))
            self.matrix.append(row_data)
            
    def sum_all(self):
        self.sum_matrix = 0
        for r in self.matrix:
            for c in r:
                self.sum_matrix += c
        print(f'Sum of all elements: {self.sum_matrix}')
        return self.sum_matrix
    
    def max_element(self):
        self.max_num = self.matrix[0][0]
        for r in self.matrix:
            for c in r:
                if self.max_num < c: self.max_num = c
        print(f'Maximun element: {self.max_num}')
        return self.max_num
        
    def min_element(self):
        self.min_num = self.matrix[0][0]
        for r in self.matrix:
            for c in r:
                if self.min_num > c: self.min_num = c
        print(f'Minimun element: {self.min_num}')
        return self.min_num
    
    def sum_row(self):
        row_sum = 0
        row_num = 0
        for r in self.matrix:
            for c in r:
                row_sum += c
            print(f'Sum of row {row_num + 1}: {row_sum}')
            row_num += 1
            row_sum = 0
            
    def sum_columns(self):
        column_sum = 0
        column_num = 0
        for x in range(len(self.matrix[0])):
            for r in self.matrix:
                column_sum += r[column_num]
            print(f'Sum of column {column_num + 1}: {column_sum}')
            column_num += 1
            column_sum = 0
            
    def transpose(self):
        self.transpose_matrix = []
        num = 0
        row = []
        for x in range(len(self.matrix[0])):
            for r in self.matrix:
                row.append(r[num])
            num += 1
            self.transpose_matrix.append(row)
            row = []
        print(f'Transpose:\n {np.array(self.transpose_matrix)}')
    
    def display(self):
        print(np.array(self.matrix))
        #print(self.matrix[0][0])
    
    
matrix = Matrix()

matrix.generate_matrix(3,2)
matrix.display()
matrix.sum_all()
matrix.max_element()
matrix.min_element()
matrix.sum_row()
matrix.sum_columns()
matrix.transpose()