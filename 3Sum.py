nums = [-1,0,1,2,-1,-4]
Output=[[-1,-1,2],[-1,0,1]]

def threesum(nums):
    nums.sort()
    res = []
    for i,a in enumerate(nums):
        if i > 0 and nums[i-1] == a:
            continue
        l=i+1
        r = len(nums) -1
        while l < r :
            print(i, l,r )
            print(nums[i], nums[l], nums[r])
            sum_ = a + nums[l] + nums[r]
            print(sum_)
            print('-----------------------')
            if sum_ > 0:
                r-=1
            elif sum_ < 0:
                l+=1
            else:
                res.append([a, nums[l],nums[r]])
                l+=1
                while nums[l] == nums[l-1] and l  < r:
                    l +=1
    return res
             
print(threesum(nums))
