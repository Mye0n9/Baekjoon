import sys

sys.setrecursionlimit(10**5)

def dfs(i,j):
    for k in range(4):

        nx = dx[k]+i
        ny = dy[k]+j

        if 0<=nx<n and 0<=ny<m and vist[nx][ny]:
            vist[nx][ny]=False
            if s[nx][ny]!=0:
                dfs(nx,ny)
            

input = sys.stdin.readline

n,m = map(int,input().split())

s=[list(map(int,input().split())) for _ in range(n)]

dx = [1,-1,0,0]
dy = [0,0,1,-1]

vist = [[0]*m for _ in range(n)]
t = 0

while True:
    t+=1
    for i in range(n):
        for j in range(m):
            if s[i][j]!=0:
                vist[i][j] = 1
                c=s[i][j]
                for k in range(4):
                    nx = dx[k]+i
                    ny = dy[k]+j
                    if 0<=nx<n and 0<=ny<m and not vist[nx][ny]:
                        if s[nx][ny]==0:
                            c-=1
                            if c==0:
                                break
                s[i][j]=c
                
    ch=0
    for i in range(n):
        for j in range(m):
            if s[i][j]!=0 and vist[i][j]:
                dfs(i,j)
                ch+=1
            elif s[i][j]==0 and vist[i][j]:
                vist[i][j]=0
                
    if ch>=2:
        print(t)
        break
    elif ch==0:
        print(0)
        break