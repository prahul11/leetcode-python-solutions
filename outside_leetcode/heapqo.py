import heapq

messages = [
    ("msgA", 2),
    ("msgB", 5),
    ("msgC", 2),
    ("msgD", 5),
]

heap = []
order = 0

for msg, priority in messages:
    # negative priority because heapq is min-heap
    heapq.heappush(heap, (-priority, order, msg))
    # print(heap)
    order += 1

# while heap:
#     print(heapq.heappop(heap)[2])



print(heap)

messages = [
    ("msgA", 2),
    ("msgB", 5),
    ("msgC", 2),
    ("msgD", 5),
]

# l = {c:[] for _,c in messages }

def set_priority(messages):
    l = sorted([(-p, i, msg) for i,(msg,p) in enumerate(messages) ]) 
    return [(-p, msg) for p, _, msg in l]
    

def set_priority2(messages):
    l = {p:[] for (_,p) in messages }
    for i in messages:
        l[i[1]].append(i[0])
    data = []
    print(l)
    for key in l:
        for value_ in l[key]:
            data.append((value_, key))
    data.sort(key = lambda x : x[1] ,reverse=True) 
    return  data

def set_p(mesg) :
    return [(b,-a) for a,_,b in sorted([(-p, i, msg) for i, (msg, p) in enumerate(mesg)])]