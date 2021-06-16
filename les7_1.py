class Matrix:
  
    row = None
    column = None
    list_matrix = []

    def __init__(self, list_matrix):
        self.row = len(list_matrix)
        self.column = len(list_matrix[0])
        self.list_matrix = list_matrix
        
        
    def __str__(self):
      rows = ""
      for el in self.list_matrix:
        for elem in el:
          rows += f"{elem} "
        rows += "\n"
      return rows
      
    def __add__(self, other):
      sum_matrix = []
      for i in range(0,self.row):
        summ = []
        for index in range(0,self.column):
          summ.append(self.list_matrix[i][index] + other.list_matrix[i][index])
        sum_matrix.append(summ)
      return Matrix(sum_matrix)


matrix_1 = Matrix([[1,2,3,4,5], [2,3,4,5,1]])
print(matrix_1)
matrix_2 = Matrix([[1,2,3,4,5], [2,3,4,5,1]])
print(matrix_2)
print(matrix_1 + matrix_2)
