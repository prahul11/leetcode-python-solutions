nums = [1,2,3,1]

def containsDuplicate(nums) :
    return len(nums) != len(set(nums))

def containsDuplicate(nums) :
    h = set()

    for i in nums:
        if i in h :
            return True
        h.add(i)
        return False


# def containsDuplicate(nums) :
#     if len(nums) <= 1:
#         return False
#     nums.sort()
#     print(nums)
#     for i in range(1,len(nums)):
#         if nums[i] == nums[i-1]:
#             return True
#     return False
    
print(containsDuplicate([2,14,18,22,22]))