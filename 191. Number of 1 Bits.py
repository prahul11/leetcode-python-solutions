# n=11

# def hammingWeight( n: int) -> int:
#     c=0
#     while n :
#         n&=(n-1)
#         c+=1
#     return c

# print(hammingWeight(n))

def h2(n):
    c =0
    while n:
        c+= n % 2
        n= n >> 1
    return c

print(h2(11))

# neetcode k comment me mila
def hg(n):
    c = 0
    while n:
        c += n &1
        n = n >>1
    return c

print(hg(11))