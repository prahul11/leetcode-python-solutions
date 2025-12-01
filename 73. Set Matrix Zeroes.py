# https://www.youtube.com/watch?v=IJ24FVsgPFU
from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        row_flag = False
        col_flag = False
        for c in range(cols):
            for r in range(rows):
                if matrix[r][c] == 0:
                    if r == 0:
                        row_flag = True
                    if c == 0:
                        col_flag = True
                    if r != 0 and c != 0:
                        matrix[r][0] = 0
                        matrix[0][c] = 0
        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] =0
        if row_flag:
            matrix[0] = [0]* cols
        if col_flag:
            for i in range( rows):
                matrix[i][0] =0


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        row_flag = col_flag = False

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    if r == 0:
                        row_flag = True
                    if c == 0:
                        col_flag = True
                    elif r!= 0 and c!= 0:
                        matrix[r][0] = 0
                        matrix[0][c] = 0

        for r in range(1, rows):
            for c in range(1, cols):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0
        if row_flag :
            matrix[0] = [0]*cols
        if col_flag:
            for r in range(rows) :
                matrix[r][0] = 0
                
