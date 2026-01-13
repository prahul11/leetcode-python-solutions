nums = [2,3,-2,4]

def maxPro(nums):
    currmin = nums[0]
    currmax = nums[0]
    maxProd = nums[0]

    for i in range(1, len(nums)):
        tmp = max(nums[i], nums[i] * currmax, nums[i]* currmin)
        currmin = min(nums[i], nums[i] * currmax, nums[i]* currmin)
        currmax = tmp
        maxProd = max(currmax, maxProd)
    return maxProd

print(maxPro(nums))


    