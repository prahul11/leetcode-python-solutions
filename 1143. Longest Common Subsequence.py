
def fiundlcs(t1, t2):
    if len(t1) ==0 or len(t2) ==0:
        return 0
    for i in range(len(t1)):
        for j in range(len(t2)):
            print(i,j, len(t1), len(t2))
            print(t1[i:], t2[j:], 'next wala')
            if not t1[i:] or not t2[j:]:
                return 0
            if t1[i:] =='' or t2[j:] =="":
                return 0
            if (i<len(t1)) and (j<len(t2) ):
                if t1[i] == t2[j]:
                    print("ha barabar")
                    print(t1[i+1:], t2[j+1:],type( t2[j+1:]) ,'-------------------')
                    return 1 + fiundlcs(t1[i+1:], t2[j+1:])
                else:
                    return max(fiundlcs(t1[i:], t2[j+1:]), fiundlcs(t1[i+1:], t2[j:]))
            else:
                return 0
            
# text1="abram"
# text2="abraham"

# text1 = "abcde"
# text2 = "ace"
text1 = "ylqpejqbalahwr"
text2 = "yrkzavgdmdgtqpg"
# print(fiundlcs(text1, text2))

def lcf(t1, t2, m,n):
    if m==0 or n==0:
        return 0

    if t1[m-1] == t2[n-1]:
        return 1+ lcf(t1, t2, m-1, n-1)
    else:
        return max(lcf(t1, t2, m, n-1), lcf(t1, t2, m-1, n))
    
         
text1="abram"
text2="abraham"

# text1 = "abcde"
# text2 = "ace"
# print(lcf(text1, text2, len(text1), len(text2)))
text1 = "ylqpejqbalahwr"
text2 = "yrkzavgdmdgtqpg"
# print(lcf(text1, text2, len(text1), len(text2)))


def neetcode(text1,text2):
    dp= [[0 for _ in range(len(text2) +1)] for _ in range(len(text1) +1)]
    for i in range(len(text1) -1, -1, -1):
        for j in range(len(text2) -1, -1, -1):
            if text1[i] ==text2[j]:
                dp[i][j] = 1+dp[i+1][j+1]
            else:
                dp[i][j] = max(dp[i][j+1], dp[i+1][j])
    return dp

print(neetcode("ram","america"))