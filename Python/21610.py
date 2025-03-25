from collections import deque

N, M = map(int,(input().split()))

board = [list(map(int,input().split())) for _ in range(N)]

moves = [list(map(int,input().split())) for _ in range(M)]

# clouds = deque([[N-1,0],[N-1,1],[N-2,0],[N-2,1]])
clouds = [[N-1,0],[N-1,1],[N-2,0],[N-2,1]]
p_clouds = [[0 for _ in range(N)] for _ in range(N)]


# 구름 이동 방향
dr = [0,-1,-1,-1,0,1,1,1]
dc = [-1,-1,0,1,1,1,0,-1]

# 대각선 방향
nr = [1,1,-1,-1]
nc = [1,-1,1,-1]

def checkBoundary(r,c):
    return True if 0<=r<N and 0<=c<N else False

def showMatrix(mat):
    for i in range(N):
        for j in range(N):
            print(mat[i][j],end=' ')
        print()

def cloudMove(clouds, move):
    direction, scale = move
    n_clouds = []
    for i in range(len(clouds)):
        r,c = clouds[i]
        nr, nc = (r+scale*dr[direction-1])%N, (c+scale*dc[direction-1])%N
        n_clouds.append([nr,nc])
        p_clouds[nr][nc] = 1 # cloud 이동했음을 나타내기 위함
    return n_clouds

def rain(clouds):
    for cloud in clouds: # 비내리기
        r,c = cloud
        board[r][c] +=1

    for cloud in clouds: # 물복사 버그는 비가 내린걸 반영한 다음에 적용
        r,c = cloud
        for direction in range(4):
            if checkBoundary(r+nr[direction],c+nc[direction]) and board[r+nr[direction]][c+nc[direction]] > 0:
                board[r][c]+=1


def updateCloud():
    i_len = len(clouds)
    n_clouds = []
    for i in range(N):
        for j in range(N):
            # in 으로 짜지 말고, visit로 해보자
            if board[i][j] >= 2 and p_clouds[i][j] == 0:
                n_clouds.append([i,j])
                board[i][j] -= 2
    return  n_clouds

for move in moves:
    clouds = cloudMove(clouds,move)
    rain(clouds)
    clouds = updateCloud()
    p_clouds = [[0 for _ in range(N)] for _ in range(N)]

ans = 0
for i in range(N):
    for j in range(N):
        ans+=board[i][j]
print(ans)