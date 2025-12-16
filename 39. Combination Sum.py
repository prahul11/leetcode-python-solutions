candidates = [2,3,6,7] 
target = 7
candidates = [2,3,5]
target = 8

# https://youtu.be/AUIfTelAGVc?si=fcHdQDb891aGe8y0
def combinationSum(candidates, target):
    dp = [[] for _ in range(target + 1)]
    for c in candidates:
        for i in range(target +1):
            if c > i : continue
            if c == i:
                dp[i].append([c])
                print(dp)
            if i > c:
                for a_list in dp[i-c]:
                    dp[i].append(a_list+[c])
                print("if waals")
                print(dp)
    return dp[-1]




print(combinationSum(candidates, target))
            