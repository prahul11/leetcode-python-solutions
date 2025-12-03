import math


def df(m,n):
    return math.comb((m+n-2), (n-1))

def df2(m,n):
    row = [1] * n

    for i in range(m-1):
        newRow = [1] *n
        for j in range(n-2, -1,-1):
            newRow[j] = row[j] + newRow[j+1]
        row = newRow

    return row[0]