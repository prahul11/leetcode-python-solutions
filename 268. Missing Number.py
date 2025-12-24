nums = [9,6,4,2,3,5,7,0,1]


def missingNumber( nums) -> int:
    c=len(nums)
    for i,v in enumerate(nums):
        c+=i-v
    return c


def mis2(nums):
    res = len(nums)
    for i , v in enumerate(nums):
        res = res ^ i ^ v
    return res

print(mis2(nums))