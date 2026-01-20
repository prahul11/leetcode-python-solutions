nums = [100,4,200,1,3,2]

def this_(nums):
    longest = 0
    nums = set(nums)
    for n in nums:
        if n-1 not in nums:
            length = 1
            curr = n
            while (curr + 1) in nums:
                curr+=1  
                length+=1

            longest = max(length, longest)
    return longest

print(this_(nums))

# redo 
def this_2(nums):
    nums = set(nums)
    longest = 0
    for n in nums:
        if n-1 not in nums:
            curr = n
            length = 1
            while (curr+1) in nums:
                curr+=1
                length+=1
            longest = max(length, longest)

    return longest


