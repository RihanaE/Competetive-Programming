class NumMatrix(object):
    mtrix = [[]]
    def __init__(self, matrix):
        row0 = []
        for i in range(len(matrix)):
            matrix[i] = [0] + matrix[i]
            for j in range(1, len(matrix[i])):
                matrix[i][j] = matrix[i][j] + matrix[i][j-1]
            for j in range(len(matrix[i])):
                if( i == 0):
                    row0.append(0)
                else:
                    matrix[i][j] = matrix[i][j] + matrix[i-1][j]
        
        self.mtrix  = [row0] + matrix
        

    def sumRegion(self, row1, col1, row2, col2):
        return self.mtrix[row2+1][col2+1] - self.mtrix[row2+1][col1] - self.mtrix[row1][col2+1] + self.mtrix[row1][col1]
