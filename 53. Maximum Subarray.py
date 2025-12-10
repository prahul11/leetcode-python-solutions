
nums = [-2,1,-3,4,-1,2,1,-5,4]

def maxSubArray( nums):
    sum_tilll_here = nums[0]
    max_sum = nums[0]

    for i in range(1, len(nums)):
        sum_tilll_here = max(sum_tilll_here + nums[i], nums[i])
        max_sum = max(max_sum, sum_tilll_here)
    return max_sum

print(maxSubArray( nums))
# maxSubArray( [1])