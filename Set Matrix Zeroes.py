def setZeroes(self, matrix: List[List[int]]) -> None:
        rows=[0]*len(matrix)                 
        coumns=[0]*len(matrix[0])
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    rows[i]=1
                    columns[j]=1
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if rows[i]==1 or columns[j]==1:
                    matrix[i][j]=0
        return matrix
