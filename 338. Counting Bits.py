from copy import deepcopy
# https://github.com/qiyuangong/leetcode/blob/master/python/338_Counting_Bits.py

# own code
def coou(nums):
    a =[0]
    for i in range(1, nums+1):
        print(i)
        c =0
        n = i
        print(n)
        while n >0:
            print("inside ")
            c+= n%2 
            n=n >> 1
        a.append(c)
    return a

# print(coou(4))

def co2(nums):
    res = [0] * (nums + 1)
    for i in range(1, nums+1):
        res[i] = res[i >> 1] + (i&1)
    return res


print(coou(4))
print(co2(4))
         