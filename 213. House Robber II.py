nums = [1,2,3,1]

# nums2=[nums[i] for i in range(len(nums)) if i%2==0]
# nums3=[nums[i] for i in range(len(nums)) if i%2!=0
#     ]
# print(nums2)
# print(nums3)
# print(max(sum(nums2), sum(nums3)))

def rob(nums):

    def helper(nums):
        rob1, rob2=0,0
        for n in nums:
            temp = max(rob1+n, rob2)
            rob1= rob2
            rob2 = temp
        return rob2
    return max(nums[0], helper(nums[1:]), helper(nums[:-1]))