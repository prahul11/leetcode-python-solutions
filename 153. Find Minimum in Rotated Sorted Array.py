nums = [3,4,5,1,2]


# def minindin(nums):
#     l = 0
#     r = len(nums) - 1

#     while r > l :
#         m = (l + r) //2
#         if nums[m] > nums[r]:
#             l = m+1
#         else:
#             r = m 
#     return nums[l]


def minindin(nums):
    l,r= 0, len(nums) -1

    while l <= r:
        mid=(l+r)//2
        if nums[mid] >= nums[l]:
            if nums[mid] >= nums[r]:
                l = mid+1
            else:
                r  = mid
    return l
print(minindin(nums))