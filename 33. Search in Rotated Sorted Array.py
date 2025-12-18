# idea not exact = https://github.com/qiyuangong/leetcode/blob/master/python/033_Search_in_Rotated_Sorted_Array.py

nums = [4,5,6,7,0,1,2]
[]
target = 0

def find_in_array(nums, target):
    l =0
    r= len(nums)-1
    while l <= r:
        mid = (l+r)//2
        if target == nums[mid]:
            return mid
        if nums[mid] >= nums[l]:
            if target >= nums[l] and target < nums[mid]:
                r = mid - 1 
            else:
                l = mid +1
        elif nums[mid] <= nums[r]:
            if target > nums[mid] and target <= nums[r]:
                l = mid +1
            else:
                r = mid -1

    return -1


print(find_in_array(nums, target))