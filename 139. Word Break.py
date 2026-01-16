from typing import List


def wordBreak( s: str, wordDict: List[str]) -> bool:
    # dp[i] means: can s[i:] be segmented into words from wordDict
    dp = [False] * (len(s) + 1)
    dp[len(s)] = True  # Base case: empty string is always segmentable

    # Iterate backwards over the string
    for i in range(len(s) - 1, -1, -1):
        for w in wordDict:
            # Check if the word fits starting at index i
            print( w,i,  s,i+len(w), s[i:i+len(w)])
            input()
            if i + len(w) <= len(s) and s[i : i + len(w)] == w:
                dp[i] = dp[i + len(w)]  # Can break if suffix is segmentable
            if dp[i]:  # No need to check further if already True
                break
    
    return dp#dp[0]


# print(wordBreak("applepenapple", ["apple","pen"]))

def wb(s, wordDict):
    dp = [False] * (len(s) +1)
    dp[len(s)] = True

    for i in range(len(s) - 1,-1,-1):
        for w in wordDict:
            if i + len(w) <= len(s) and s[i:i+len(w)] == w:
                dp[i] = dp[i + len(w)]
            if dp[i]:
                break
    return dp[0]




def wb(s, wordDict):
    while s:
        last_length = len(s)
        for word in wordDict:
            print(word)
            print(len(s))
            print(len(word))
            print('-------------------')
            if s[0] == word[0] and len(s) >= len(word) and s[:len(word)] == word:
                s = s[len(word):]
                if len(s) ==0:
                    return True
        if len(s) == last_length:
            return False

    return False

# print(wb("applepenapple", ["apple","pen"]))

print(wb("catsandog", ["cats","dog","sand","and","cat"]))
