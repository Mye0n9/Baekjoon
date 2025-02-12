import sys
from collections import deque

sys.setrecursionlimit(10000)

R,C = map(int, sys.stdin.readline().split())

mat = []
for _ in range(R):
    mat.append(list(sys.stdin.readline().strip()))

points = set(mat[0][0])
res = 1

def dfs(r, c, cnt):
    global res
    res = max(res, cnt)
    
    dr = [1,-1,0,0]
    dc = [0,0,1,-1]

    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        # boundary check and visit check
        if 0<=nr<R and 0<=nc<C:
            if mat[nr][nc] not in points:
                points.add(mat[nr][nc])
                dfs(nr,nc,cnt+1)
                points.remove(mat[nr][nc])

dfs(0,0,res)
print(res)