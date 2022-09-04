
# Link: https://leetcode.com/explore/interview/card/top-interview-questions-medium/103/array-and-strings/777/



class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        n = len(matrix)
        m = len(matrix[-1])

        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    matrix[i][j] = float('inf')

        for i_1 in range(n):
            for j_1 in range(m):
                if matrix[i_1][j_1] == float('inf'):
                    # for i in range(n):
                    for j in range(m):
                        matrix[i_1][j] = 0 if matrix[i_1][j] != float('inf') else matrix[i_1][j]
                    
                    for i in range(n):
                        matrix[i][j_1] = 0 if matrix[i][j_1] != float('inf') else matrix[i][j_1]

                    matrix[i_1][j_1] = 0



