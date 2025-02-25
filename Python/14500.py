import sys

input = sys.stdin.readline

N,M = map(int, input().split())

mat = [list(map(int,input().split()))for _ in range(N)]
visit = [[0 for _ in range(M)] for _ in range(N)]

max_val = 0

dr = [1,-1,0,0]
dc = [0,0,1,-1]

def checkBoundary(r,c):
    return True if 0<=r<N and 0<=c<M else False

def speicalBoundary(positions):
    for pos in positions:
        if not checkBoundary(pos[0],pos[1]):
            return False
    return True

def bfs(depth, val, r,c):
    global max_val, visit
    if depth == 4:
        max_val = max(val, max_val)
        # print(visit)
        return

    visit[r][c] = 1
    for dir in range(4):
        nr = r + dr[dir]
        nc = c + dc[dir]
        if checkBoundary(nr,nc) and visit[nr][nc] != 1:
            bfs(depth+1, val+mat[r][c],nr,nc)
    visit[r][c] = 0

def pronged(r,c):
    global max_val
    shapes = [
        [(0, 0), (-1, 0), (1, 0), (0, 1)],  # ㅜ
        [(0, 0), (-1, 0), (1, 0), (0, -1)], # ㅗ
        [(0, 0), (0, -1), (0, 1), (1, 0)],  # ㅏ
        [(0, 0), (0, -1), (0, 1), (-1, 0)]  # ㅓ
    ]

    for shape in shapes:
        val = 0
        valid = True
        for dr, dc in shape:
            nr, nc = r+dr, c+dc
            if not checkBoundary(nr,nc):
                valid = False
                break
            val += mat[nr][nc]
        if valid:
            max_val = max(val, max_val)

for i in range(N):
    for j in range(M):
        bfs(0,0,i,j)
        pronged(i,j)

print(max_val)
