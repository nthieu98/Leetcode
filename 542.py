class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        n = len(matrix)
        m = len(matrix[0])
        # matrix = [[100000 for x in range(m)] for y in range(n)]
        p = [-1, 1]
        for i in range(n):
            for j in range(m):
                if matrix[i][j] != 0
                    if i > 0:
                        matrix[i][j] = min(matrix[i][j], matrix[i - 1][j] + 1)
                    if j > 0:
                        matrix[i][j] = min(matrix[i][j], matrix[i][j - 1] + 1)
        for i in reversed(range(n)):
            for j in reversed(range(m)):
                if matrix[i][j] != 0:
                    if i < n-1:
                        matrix[i][j] = min(matrix[i][j], matrix[i+1][j] + 1)
                    if j < m - 1:
                        matrix[i][j] = min(matrix[i][j], matrix[i][j+1] + 1)
        return matrix