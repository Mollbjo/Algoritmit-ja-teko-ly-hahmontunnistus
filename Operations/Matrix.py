class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.data = [[0.0 for i in range (columns)] for j in range(rows)]


    def add(self, matrix):
        if isinstance(matrix, Matrix):
            if self.rowns != matrix.rows or self.columns != matrix.columns:
                raise ValueError("Matriisien oltava samankokoisia")
            result = Matrix(self.rows, self.columns)
        for i in range(self.rows):
            for j in range(self.columns):
                result.data[i][j] = self.data[i][j] + matrix.data[i][j]
        else:
            result = Matrix(self.rows, self.columns)
            for i in range(self.rows):
                for j in range(self.columns):
                    result.data[i][j] = self.data[i][j] + matrix 
        
        return result
    
    def subtract(self, matrix):
        if isinstance(matrix, Matrix):
            if self.rowns != matrix.rows or self.columns != matrix.columns:
                raise ValueError("Matriisien oltava samankokoisia")
            result = Matrix(self.rows, self.columns)
        for i in range(self.rows):
            for j in range(self.columns):
                result.data[i][j] = self.data[i][j] - matrix.data[i][j]
        else:
            result = Matrix(self.rows, self.columns)
            for i in range(self.rows):
                for j in range(self.columns):
                    result.data[i][j] = self.data[i][j] - matrix 
        
        return result

    def dot(self, matrix):
        if isinstance(matrix, Matrix):
            if self.columns != matrix.rows:
                raise ValueError("Matriisien koot eivät ole sopivia")
            result = Matrix(self.rows, matrix.columns)
            for i in range(result.rows):
                for j in range(result.columns):
                    for k in range(self.columns):
                        result.data[i][j] += self.data[i][k] * matrix.data[k][j]
            return result
        else:
            raise TypeError("Argumentti ei ole Matrix-luokan olio")
        
