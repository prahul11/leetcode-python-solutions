strs = ["eat","tea","tan","ate","nat","bat"]

# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs) :
        d = defaultdict(list)
        for w in strs:
            q= "".join(sorted(w))
            print(q)
            d[q].append(w)
        return d.values()


class Solution:
    def groupAnagrams(self, strs) :
        ek_dict = defaultdict(list)
        for s in strs:
            d = [0] *26
            for q in s:
                d[ord(q) - ord("a")] +=1
            ek_dict[tuple(d)].append(s)
        return list(ek_dict.values())

