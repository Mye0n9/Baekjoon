import sys
from collections import deque

input = sys.stdin.readline

N,L,R = map(int,input().split())

mat = []
for _ in range(N):
    mat.append(list(map(int,input().split())))

dr = [1,-1,0,0]
dc = [0,0,1,-1]
# 0: down, 1: up, 2: right, 3: left

visit = [[0 for _ in range(N)] for _ in range(N)]
Q = deque([])


def checkBoundary(pos):
    if 0<=pos[0]<N and 0<=pos[1]<N:
        return True
    return False

def checkPopulation(pos): #인구 이동여부를 판단하는 첫번째 칸 인지 확인
    r = pos[0]
    c = pos[1]
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if checkBoundary([nr,nc]) and visit[nr][nc] == 0 and L<=abs(mat[nr][nc] - mat[r][c]) <= R:
            return True
    return False


groupInfo = []

def update():
    groupByCnt = 0
    groupByVal = 0
    groupByPositions = []
    for i in range(N):
        for j in range(N):
            visit[i][j] = 1
            if checkPopulation([i,j]): # 인구 이동을 해야하는 첫번째 칸이라면
                Q.append([i,j]) # Queue에다가 넣고
                while Q: # Queue가 비워질때까지
                    r,c = Q.popleft() 
                    groupByCnt +=1
                    groupByVal += mat[r][c]
                    groupByPositions.append([r,c])
                    visit[r][c] = 1
                    for k in range(4):
                        nr = r + dr[k]
                        nc = c + dc[k]
                        if checkBoundary([nr,nc]) and visit[nr][nc] == 0 and L<=abs(mat[nr][nc] - mat[r][c]) <= R:
                            Q.append([nr,nc]) # 중복해서 넣는 경우가 발생
                            visit[nr][nc] = 1
                
                groupInfo.append([groupByVal//groupByCnt,groupByPositions]) # 정보 저장
            # 초기화
            groupByCnt = 0
            groupByVal = 0
            groupByPositions = []

    for val, positions in groupInfo:
        for pos in positions:
            mat[pos[0]][pos[1]] = val
cnt = 0
while True:
    update()

    # for k in range(N):
    #     print(mat[k])

    if len(groupInfo) == 0:
        break
    cnt+=1
    groupInfo = []
    visit = [[0 for _ in range(N)] for _ in range(N)]

print(cnt)

