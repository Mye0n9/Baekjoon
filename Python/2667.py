import sys

sys.setrecursionlimit(10000)

n = int(sys.stdin.readline())
mat = []
res = []
for _ in range(n):
    mat.append(list(sys.stdin.readline().strip()))

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(x,y):
    if x< 0 or x >=n or y<0 or y>=n:
        return False
    
    if mat[x][y] == '1':
        global count
        count+=1
        mat[x][y] = '0'
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            dfs(nx, ny)
        return True
    return False

count =0

for i in range(n):
    for j in range(n):
        if dfs(i,j) == True:
            res.append(count)
            count = 0

res.sort()
print(len(res))
for i in range(len(res)):
    print(res[i])