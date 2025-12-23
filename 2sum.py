def twosumn(nums, target):
    empty_dic = {}
    for i, num in enumerate(nums):
        print(i, num)
        t = target - num
        if t in empty_dic:
            return i, empty_dic[t]
        empty_dic[num]=i


l= [2,7,11,15]
m= twosumn(l, 22)
print(m)

# --------------------------------------------------
