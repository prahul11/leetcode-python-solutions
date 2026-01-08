def reverse_bit(n):
    res =0
    for i in range(32):
        res = res << 1 
        res += n &1 
        n = n>> 1
    return res


print(reverse_bit(1))

def reb(n):
    res =0
    for i in range(32):
        res = res << 1 
        res += n % 2
        n = n>> 1
    return res

print(reb(1))


def rev3(n):
    res =0
    for i in range(32):
        res = (res << 1) | n&1
        n >>= 1
    return  res

print(rev3(1))