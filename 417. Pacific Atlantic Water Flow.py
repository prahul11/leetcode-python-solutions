l=[[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]

# # def px(l):
# col = len(l[0])
# row = len(l)
# pac = set()
# atl= set()
# # pac = {(0,i) for i in range(col)}
# # pac.update({(i, 0) for i in range(row)})
# # atl = {(i, col-1) for i in range(row)}
# # atl.update({(row-1, i) for i in range(col)})

# for i in range(col):
#     for j in range(row):
#         if i ==0 or j== 0:
#             pac.add((i, j))
#         if j == col-1 or j == row-1:
#             atl.add((i, j))
        


from collections import deque

class Solution:
    def pacificAtlantic(self, heights):
        ROWS, COLS = len(heights), len(heights[0])

        def bfs(starts):
            q = deque(starts)
            visit = set(starts)

            while q:
                r, c = q.popleft()
                for dr, dc in [(1,0), (-1,0), (0,1), (0,-1)]:
                    nr, nc = r + dr, c + dc
                    if (
                        0 <= nr < ROWS and
                        0 <= nc < COLS and
                        (nr, nc) not in visit and
                        heights[nr][nc] >= heights[r][c]
                    ):
                        visit.add((nr, nc))
                        q.append((nr, nc))
            return visit

        pacific = [(0, c) for c in range(COLS)] + [(r, 0) for r in range(ROWS)]
        atlantic = [(ROWS-1, c) for c in range(COLS)] + [(r, COLS-1) for r in range(ROWS)]

        pac = bfs(pacific)
        atl = bfs(atlantic)

        return list(pac & atl)

# print(Solution().pacificAtlantic(l))



def pac(heights):
    rows  = len(heights)
    cols = len(heights[0])

    def bfs(starts):
        q= deque(starts)
        visit = set(starts)
        while q:
            r,c = q.popleft()
            for dr, dc in [(-1,0),(0,-1),(1,0),(0, 1)]: # dr , dc means directional row , column
                nr, nc = r + dr, c+dc           # nr, nc means neighbours 
                if ((nr, nc) not in visit 
                    and  0 <= nr < rows 
                    and  0 <= nc < cols
                    and heights[nr][nc] >=heights[r][c] ):
                    visit.add((nr,nc))
                    q.append((nr,nc))
        return visit

    pacific = []
    pacific.extend([(0, c) for c in range(cols)])
    pacific.extend([(r, 0) for r in range(rows)])
    # print(atlantic)
    atlantic = []
    atlantic.extend([(r, cols-1) for r in range(rows)])
    atlantic.extend([(rows-1, c) for c in range(cols)])
    print(pacific, atlantic)
    return list(bfs(atlantic) & bfs(pacific))


print(pac([[1]]))


# again same code 
# https://chatgpt.com/share/695491a3-db28-800d-8125-8b27fdb5ae05
def pac(heights):
    rows = len(heights)
    col  = len(heights[0])
    def bfs(starts):
        q=deque(starts)
        visit = set(starts)
        while q:
            r,c = q.popleft()
            for dr, dc in [(0,-1), (-1,0),(0,1), (1,0)]:
                nr, nc = r +dr,c +dc
                if (0<=nr< rows and 0<=nc<col and (nr,nc) not in visit and heights[nr][nc] >= heights[r][c]):
                    visit.add((nr,nc))
                    q.append((nr,nc))
        return visit
    pacific = [(0, c) for c in range(col)] 
    pacific.extend((r,0) for r in range(rows))
    atlantic = [(rows-1, c) for c in range(col)]
    atlantic.extend([(r,col-1) for r in range(rows)])
    return list(bfs(atlantic) & bfs(pacific))