import sys
from collections import deque

sys.setrecursionlimit(100000)

itr = int(input())

dx = [1,-1,0,0]
dy = [0,0,1,-1]

def bfs(x,y,n):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        # check boundary
        if 0<=nx<n and 0<=ny<n:
            # check size
            if res[nx][ny]> int(mat[x][y]) + int(mat[nx][ny]):
                res[nx][ny] = int(mat[x][y])+int(mat[nx][ny])
            bfs(nx,ny,n)

for _ in range(itr):
    n = int(sys.stdin.readline())
    mat = [list(sys.stdin.readline().strip()) for _ in range(n)]
    res = [[float('inf') for _ in range(n)] for _ in range(n)]

    bfs(0,0,n)
    print(res[n-1][n-1])







# Can't solve this problem with DP since it should move up, down, left, and right.
# Should solve with BFS and other methods

# itr = int(input())

# def dp():
#     n = int(input())

#     mat = [list(input().strip()) for _ in range(n)]
#     res = [[0 for _ in range(n)] for _ in range(n)]
#     for i in range(n):
#         for j in range(n):
#             if i==0 and j == 0: res[i][j] = int(mat[i][j])
#             elif i == 0: res[i][j] = int(mat[i][j]) + res[i][j-1]
#             elif j == 0: res[i][j] = int(mat[i][j]) + res[i-1][j]
#             else: res[i][j] = min(res[i][j-1],res[i-1][j]) + int(mat[i][j])
    
#     return(res[n-1][n-1])

# for i in range(itr):
#     print(f"#{i+1} {dp()}")