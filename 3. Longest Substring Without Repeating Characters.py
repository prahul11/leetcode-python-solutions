s = "abcabcbb"

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l=0
        longest =0
        lx = set()
        for r in range(len(s)):
            while s[r] in lx:
                lx.remove(s[l])
                l+=1
            w = r-l+1
            longest=max(longest, w)
            lx.add(s[r])
        return longest
    


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l =0
        longest = 0
        word = set()

        for r in range(len(s)):
            # ye baad me socho 
            while s[r] in word:
                word.remove(s[l])
                l+=1

            # ye pehle socho
            w = r-l+1
            longest= max(longest, w)
            word.add(s[r])