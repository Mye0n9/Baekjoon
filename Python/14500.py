import sys

from collections import deque

r,c = map(int,sys.stdin.readline().split())
mat = [list(map(int,sys.stdin.readline().split())) for _ in range(r)]

Q = deque()
output= 0

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def dfs(x, y):

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        
        if len(Q) == 4:
            global output
            output = max(output, sum(Q))
            Q.pop()
        
        if(nx >= 0 and nx < c, ny >= 0 and ny < r):
            Q.append(mat[x][y])
            dfs(nx,ny)

for i in range(r):
    for j in range(c):
        dfs(i,j)

print(output)


