def climbStairs(n: int) -> int:
    if n ==1: return 1
    if n==2 : return 2

    return climbStairs(n-1) + climbStairs(n-2)
 
# print(stairsCount(44))

def st(n, memo =None):
    if memo is None:
        memo = {1:1, 2:2}
    if n in memo:
        return memo[n]
    memo[n] = st(n-1,memo) + st(n-2, memo)
    return memo[n]

print(st(44))
 

def st2(n):
    dp= [0] *n
    dp[0] = 1
    dp[1] =2
    for i in range(2, n):
        dp[i] = dp[i-1] + dp[i-2]
        print(dp)
    return dp[-1]

print(st2(5))

def st3(n):
    if n==1: return 1

    prev = 1
    curr =2
    for i in range(3, n+1):
        prev , curr = curr, curr + prev
    return curr

print(st3(5))