nums = [1,2,3,4]

def productExceptSelf(nums):
    left_l = [1] * len(nums)
    right_l = [1] * len(nums)
    # print(left_l)
    # print(right_l)
    r_m = 1
    for i in range(1,len(nums)):
        left_l[i] = left_l[i-1] * nums[i-1]

    for j in range(len(nums) -2 , -1,-1):
        right_l[j] = nums[j+1] * right_l[j+1]
        # or directly
        # left_l[j] *= right_l[j] 

    print(left_l)  
    print(right_l)
    return list(x*y for x, y in list(zip(left_l, right_l)))
print(productExceptSelf(nums))

def productExceptSelf(nums):
    left_l = [1] * len(nums)
    right_l = [1] * len(nums)
    # print(left_l)
    # print(right_l)
    r_m = 1
    for i in range(1,len(nums)):
        left_l[i] = left_l[i-1] * nums[i-1]

    right =1
    for j in range(len(nums) -1 , -1,-1):
        left_l[j] *= right
        right *= nums[j]
        # or directly
        # left_l[j] *= right_l[j] 

    # print(left_l)  
    # print(right_l)
    # return list(x*y for x, y in list(zip(left_l, right_l)))

        
print(productExceptSelf(nums))

def productExceptSelf(nums):
    lm= 1
    ll= [1]*len(nums)
    for i in range(1, len(nums)):
        ll[i] = ll[i-1] * nums[i-1] 
    print(ll)

    righ =1
    for j in range(len(nums)-1,-1, -1):
        ll[j] *= righ
        righ *= nums[j]
    return ll
     

print(productExceptSelf(nums))
