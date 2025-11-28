# https://github.com/deepti-talesra/LeetCode/blob/master/Decode_Ways.py
# class Solution:
def numDecodings( s: str) -> int:
    print(s)
    if s[0] == "0":
        return 0
    dp = [1,1]
    "2101"
    for ind, num in enumerate(s[1:],2):
        print(ind, ind-2,s[ind-2], num)
        ways = 0
        print("-------")
        if num != "0":
            ways += dp[ind-1]
            print(ways)
        if 10 <= int(s[ind-2] + num) <= 26:
            ways += dp[ind-2]
            print(ways)
        dp.append(ways)
        print(dp)
    return dp[-1]
print(numDecodings("2101"))
# print(numDecodings("261105"))    # 2  -> ("AB", "L")
# print(numDecodings("26"))    # 2  -> ("AB", "L")
# print(num_decodings("226"))   # 3  -> ("BZ","VF","BBF")
# print(num_decodings("0"))     # 0
# print(num_decodings("10"))    # 1  -> ("J")
# print(num_decodings(""))      # 0
261105
111101
21211

# chatgpt
def num_decodings(s: str) -> int:
    # Return 0 for empty string (LeetCode convention)
    if not s:
        return 0
    if s[0] == '0':
        return 0
    prev, curr = 1, 1
    for i in range(1, len(s)):
        ways = 0
        if s[i] != '0':
            ways += curr
        two = int(s[i-1:i+1])
        if 10 <= two <= 26:
            ways += prev
        prev, curr = curr, ways
        if curr == 0:
            return 0
    return curr

# Quick tests
# print(num_decodings("12"))    # 2  -> ("AB", "L")
# print(num_decodings("226"))   # 3  -> ("BZ","VF","BBF")
# print(num_decodings("0"))     # 0
# print(num_decodings("10"))    # 1  -> ("J")
# print(num_decodings(""))      # 0


# https://www.youtube.com/watch?v=maqSMmG7rns&t=219s 
# 100 and 68
class Solution:
    def numDecodings(self, s: str) -> int:
        # edge cases
        if not s or s[0] == "0":
            return 0
        if len(s) == 1:
            return 1

        N = len(s)
        dp = [0] * N
        dp[0] = 1

        # initialize dp[1]
        if s[1] == "0":
            if 10 <= int(s[0:2]) <= 26:
                dp[1] = 1
            else:
                return 0
        else:
            if 10 <= int(s[0:2]) <= 26:
                dp[1] = 2
            else:
                dp[1] = 1

        # main loop
        for i in range(2, N):
            if s[i] != "0":
                if 10 <= int(s[i-1:i+1]) <= 26:
                    dp[i] = dp[i-1] + dp[i-2]
                else:
                    dp[i] = dp[i-1]
            else:
                if 10 <= int(s[i-1:i+1]) <= 26:
                    dp[i] = dp[i-2]
                else:
                    return 0

        return dp[-1]



def numDecodings( s: str) -> int:
    print(s)
    if s[0] == "0":
        return 0
    dp = [1,1]
    for ind, num in enumerate(s[1:]):
        ways = 0
        if num != "0":
            ways += dp[ind-1]
            print(dp)
        if 10 <= int(s[ind-1] + num) <= 26:
            ways += dp[ind-2]
            print(dp)
        dp.append(ways)
        print(dp)
    return dp[-1]

"261105"

[1,2]
"2101"
def mera(s):
    if s=="" or s[0] == "0":
        return 0
    # dp = [0 for _ in range(len(s) +1)]
    dp =[1]
    print(dp)
    for i, num in enumerate(s[1:],1):
        print(f"{i=}, {s[1:]=}, {num=}")
        way=0
        print("--------------")
        if num != "0":
            print(f"{i-1=}")
            print(f"{dp[i-1]=}")
            # dp[i] += dp[i-1]
            way += dp[i-1]
            print(way)
        if 10<=int(s[i-1:i+1]) <=26:
            # dp[i] += dp[i-2]
            way += dp[i-2]
            print(way)
        dp.append(way)
    print(dp)
    return dp[-1]



def mera2(s):
    if s=="" or s[0] == "0":
        return 0
    dp =[1]
    for i, num in enumerate(s[1:],1):
        way=0
        if num != "0":
            way += dp[i-1]
        if 10<=int(s[i-1:i+1]) <=26:
            way += dp[i-2]
        dp.append(way)
    return dp[-1]

print(mera("12"))
print(mera("226"))