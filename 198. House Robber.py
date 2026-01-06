nums = [1,2,3,1]

# nums2=[nums[i] for i in range(len(nums)) if i%2==0]
# nums3=[nums[i] for i in range(len(nums)) if i%2!=0
#     ]
# print(nums2)
# print(nums3)
# print(max(sum(nums2), sum(nums3)))

def rob(nums):
    rob1 , rob2 = 0,0
    for n in nums:
        # [rob1, rob2, n , n+1 ....]
        temp = max(rob1, rob2+n)
        rob1= rob2
        rob2 = temp
    return rob2
