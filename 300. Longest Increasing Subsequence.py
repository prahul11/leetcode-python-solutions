from copy import deepcopy

def ln():
    #logic 
    # originial list k har ek index se element udao, aur nye list bnao,m
    #  fir uunse udaoi and so on

    nums = [10,9,2,5,3,7,101,18]
    # nums = [1,2,3,4]
    lis = [nums]

    current_list = [nums]
    print(current_list)
    # input()
    #kitne udane hai
    while current_list:
        target_list = current_list.pop(0)
        for i in range(len(target_list)-1):
            # for j in range(len(nums)):
            t = deepcopy(target_list)
            del t[i]
            lis.append(t)
            # print(t, lis)
            current_list.append(t)
            # print(current_list)

    unique = [list(x) for x in set(tuple(sub) for sub in lis)]

    # print(nums)
    # for item in lis:
    #     print(item)
    lis = []
    l =0
    for item in unique:
        # print(sorted(item), len(item))
        if all([item[i] > item[i-1] for i in range(1, len(item))]):
            print("item ", item)
            if len(item) > l:
                l = len(item)
                # lis.append(item)
                lis = item

    print(lis)


def ls(nums):
    LIS = [1] * len(nums)
    for i in range(len(nums)-1, -1, -1):
        for j in range(i+1, len(nums)):
            if nums[i] < nums[j]:
                LIS[i] = max(LIS[i], LIS[j] +1)
    return max(LIS)





