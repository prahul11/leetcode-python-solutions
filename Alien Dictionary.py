from collections import defaultdict, deque

def alienOrder(words):
    graph = defaultdict(set)
    indegree = {c: 0 for word in words for c in word}

    # build graph
    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i + 1]
        min_len = min(len(w1), len(w2))

        if w1[:min_len] == w2[:min_len] and len(w1) > len(w2):
            return ""

        for j in range(min_len):
            if w1[j] != w2[j]:
                print("------------------------")
                print(w2[j])
                print(graph[w1[j]])
                print(graph)
                print(indegree)
                if w2[j] not in graph[w1[j]]:
                    graph[w1[j]].add(w2[j])
                    indegree[w2[j]] += 1
                break

    # BFS
    q = deque([c for c in indegree if indegree[c] == 0])
    print(q)
    order = []

    while q:
        ch = q.popleft()
        order.append(ch)
        for nei in graph[ch]:
            indegree[nei] -= 1
            if indegree[nei] == 0:
                q.append(nei)

    return "".join(order) if len(order) == len(indegree) else ""


# print(alienOrder(["wrt","wrf","er","ett","rftt"]))

def gh(words):
    graph = defaultdict(set)
    indegrees = {c:0 for word in words for c in word }

    for i in range(len(words) - 1):
        w1, w2 = words[i], words[i+1]
        minlen = min(len(w1), len(w2))
        if w1[:minlen] == w2[:minlen] and len(w1) > len(w2):
            return ""

        for j in range(minlen):
            if w1[j] != w2[j]:
                graph[w1[j]].add(w2[j])
                indegrees[w2[j]]+=1

    q= deque([c for c in indegrees if indegrees[c] == 0])
    l =[]
    while q:
        ch = q.poplefch()
        l.append(ch)
        for nei in graph[ch]:
            indegrees[nei] -=1
            if indegrees ==0: 
                l.append(nei)
    return ",".join(l) if len(l) == len(indegrees) else ""


def alien(words):
    graph = defaultdict(set)
    indegrees = {c:0 for word in words for c in word}
    for i in range(len(words) -1):
        w1, w2 = words[i], words[i+1]
        minlen = min(len(w1), len(w2))
        if w1[:minlen] == w2[:minlen] and len(w1) > len(w2):
            return ""
        for j in range(minlen):
            if w1[j] != w2[j]:
                graph[w1[j]].add(w2[j])
                indegrees[w2[j]] +=1
                break
    q = deque([c for c in indegrees if indegrees[c] == 0])
    while q:
        ch = q.popleft()
        for nei in graph[ch]:
            indegrees[nei]-=1
            if indegrees[nei] == 0:
                q.append(nei)
    return "".join(q) if len(indegrees) == q else ""


def alien(words):
    graph = defaultdict(set)
    indegrees = {c:0 for word in words for c in word}

    for i in range(len(words) -1):
        w1, w2 = words[i], words[i+1]
        minlen = min(len(w1), len(w2))
        if w1[:minlen] == w2[:minlen] and len(w1)> len(w2):
            return "" 
        for j in range(minlen):
            if w1[j] != w2[j]:
                if w2[j] not in graph[w1[j]]:
                    graph[w1[j]].add(w2[j])
                    indegrees[w2[j]]+=1
                break
    q = deque([c for c in indegrees if indegrees[c] ==0])
    order = []
    while q:
        ch = q.popleft()
        order.append(ch)
        for nei in graph[ch]:
            indegrees[nei] -= 1
            if indegrees[nei] == 0:
                q.append(nei)
    return "".join(order) if len(indegrees) == len(order) else ""



def alien(words):
    graph = defaultdict(set)
    indegrees = {c:0 for word in words for c in word}

    for i in range(len(words) -1):
        w1, w2 = words[i], words[i+1]
        minlen = min(len(w1), len(w2))
        if w1[:minlen] == w2[:minlen] and len(w1) > len(w2):
            return ""
        for j in range(minlen):
            if w1[j] != w2[j]:
                if w2[j] not in graph[w1[j]]:
                    graph[w1[j]].add(w2[j])
                    indegrees[w2[j]]+=1
                break
    q = deque([c for c in indegrees if indegrees[c] ==0])
    order = []
    while q:
        ch = q.popleft()
        order.append(ch)
        for nei in graph[ch]:
            indegrees[nei]-=1
            if indegrees[nei] ==0:
                q.append(nei)
    return "".join(order) if len(indegrees) == len(order) else ""