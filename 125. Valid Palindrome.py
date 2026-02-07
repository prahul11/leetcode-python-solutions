class Solution:
    def isPalindrome(self, s: str) -> bool:
        e =""
        for i in s:
            if i.isalnum():
                e+= i.lower()
        return e == e[::-1]
    
# "A man, a plan, a canal: Panama"



class Solution:
    def isPalindrome(self, s: str) -> bool:
        l=0
        r = len(s) -1
        while l <= r : 
            while  l<= r and not self.is_a_alnum(s[l]) :
                l+=1 
            while l<=r and not self.is_a_alnum(s[r]) :
                r-=1
            if s[l].lower() != s[r].lower():
                return False
            l +=1 
            r-= 1
        return True
        

    def is_a_alnum(self, text):
        return (ord("a") <= ord(text) <= ord("z")) or \
        (ord("A") <= ord(text) <= ord("Z")) or \
        (ord("0") <= ord(text) <= ord("9"))
 


class Solution:
    def isPalindrome(self, s: str) -> bool:
        l =0
        r= len(s) -1
        while l< r:
            while l <r and not self.is_alnum(s[l]):
                l+=1
            while l <r and not self.is_alnum(s[r]):
                r-=1
            if s[l].lower() != s[r].lower():
                return False
            l +=1
            r -= 1
        return True
    def is_alnum(self, text):
        return (
            ord("a") <= ord(text) <= ord("z")
        ) or (
            ord("A") <= ord(text) <= ord("Z")
        ) or (
            ord("0") <= ord(text) <= ord("9")
        ) 