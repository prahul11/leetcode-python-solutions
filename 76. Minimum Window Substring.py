from collections import defaultdict

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d = defaultdict(int)
        for i in t:
            d[i] += 1
        l = r = 0
        len_ans = float("inf")
        formed , total = 0, len(d)
        ls , rs = 0, 0
        while r < len(s):
            char = s[r]
            if char in d:
                d[char] -=1
                if d[char] ==0:
                    formed += 1
            while l <= r  and total == formed:
                wind = r - l + 1
                if wind < len_ans:
                    len_ans = wind
                    ls , rs = l,r
                char = s[l]
                if char in d:
                    if d[char] == 0:
                        formed -= 1
                    d[char] +=1
                l+=1
            r += 1
        if len_ans == float("inf"):
            return ""
        else:
            return s[ls: rs+1]


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        d = defaultdict(int)
        l = r = 0
        ls = 0
        rs = 0
        for i in t :
            d[i] += 1
        len_ans = float("inf")
        total = len(d)
        formed  = 0
        while r < len(s) :
            char = s[r]
            if char in d:
                d[char] -= 1
                if d[char] == 0:
                    formed += 1
            while l <=r and formed == total:
                window = r - l + 1
                if window < len_ans:
                    len_ans = window
                    ls, rs = l, r + 1
                char = s[l]
                if char in d:
                    if d[char] == 0:
                        formed -= 1
                    d[char] += 1
                l+=1
            r+=1
        return "" if len_ans == float("inf") else s[ls:rs]
