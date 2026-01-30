board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "SEE"


class Solution:
    def exist(self, board, word: str) -> bool:        
        rows = len(board)
        cols = len(board[0])
        visit = set()
        def dfs(r,c,i):
            if i == len(word): return True
            if r <0 or c <0 or r>=rows or c >= cols or (r,c) in visit or word[i] != board[r][c]:
                return False
            visit.add((r,c))
            # for l,m in [(1,0), (-1,0), (0,1), (0, -1)]:
            #     res = dfs(r+l, c+m) 
            res = any([dfs(a,b,i+1) for a,b in [(r+1,c+0), (r-1,c+0), (r+0,c+1), (r+0, c-1)]  ])
            visit.remove((r,c))
            return res

        for r in range(rows):
            for c in range(cols):
                if dfs(r,c,0): return True
        return False