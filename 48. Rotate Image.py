
from typing import List

matrix = [[1,2,3],[4,5,6],[7,8,9]]

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        lm= len(matrix)
        for i in range(lm):
            for j in range(i+1, lm):
                matrix[i][j], matrix[j][i]=matrix[j][i],  matrix[i][j]
        for i in range(lm):
            for j in range(lm//2):
                matrix[i][j],matrix[i][lm-1 -j] = matrix[i][lm-1 -j],matrix[i][j]

