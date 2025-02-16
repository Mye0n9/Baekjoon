import sys

# 백트래킹으로 최대 구간 수정하는 걸로 수정해보자

input = sys.stdin.readline
N,M = map(int,input().split())

target = 0
max_cover = 0

mat = []
for _ in range(N):
    row = (list(map(int,input().split())))
    target+=row.count(0)
    mat.append(row)

overlap = [[0 for _ in range(M)] for _ in range(N)]

positions = []
for i in range(N):
    for j in range(M):
        if mat[i][j] in [1,2,3,4,5]:
            positions.append([i,j])

dr = [1,-1,0,0]
dc = [0,0,1,-1]
# 0: down, 1: up, 2:right, 3: left

def checkBoundary(r,c):
    if 0<=r<N and 0<=c<M:
        return True
    return False

def countBlocks(pos, dir): # 한 방향으로 갔을 때, 감시 구간의 개수
    nr = pos[0]
    nc = pos[1]

    while True:
        nr += dr[dir]
        nc += dc[dir]

        if(not checkBoundary(nr,nc) or mat[nr][nc] == 6):
            break
        
        if mat[nr][nc] in [1,2,3,4,5]: # CCTV 이거나, overlap 구간이라면 cnt는 하지 않음
            pass
        else:
            overlap[nr][nc] += 1 # overlap에 기록

def rollBack(pos, dir): # 한 방향으로 갔을 때, 감시 구간 해제
    nr = pos[0]
    nc = pos[1]

    while True:
        nr += dr[dir]
        nc += dc[dir]

        if(not checkBoundary(nr,nc) or mat[nr][nc] == 6): # 구간 밖이라면 중지
            break
        
        if mat[nr][nc] in [1,2,3,4,5] or overlap[nr][nc] == 0: # CCTV가 있는 구간이거나, 기존에 감시 영역이 아니라면 -1 하지 않음
            pass
        else:
            overlap[nr][nc] -= 1 # overlap에 기록

def main_func(positions):
    global max_cover
    # update by backtracking
    if len(positions) == 0:
        val = 0
        for i in range(N):
            for j in range(M):
                if overlap[i][j] != 0:
                    val +=1
        if val > max_cover:
            max_cover = val
        return

    pos = positions[0]
    # print(pos, mat[pos[0]][pos[1]])
    if mat[pos[0]][pos[1]] == 1:
        for dir in range(4):
            countOne(pos,dir)
            main_func(positions[1:])
            rollBackOne(pos, dir)
    elif mat[pos[0]][pos[1]] == 2:
        for dir in range(2):
            countTwo(pos,dir)
            main_func(positions[1:])
            rollBackTwo(pos, dir)
    elif mat[pos[0]][pos[1]] == 3:
        for dir in range(4):
            countThree(pos,dir)
            main_func(positions[1:])
            rollBackThree(pos, dir)
    elif mat[pos[0]][pos[1]] == 4:
        for dir in range(4):
            countFour(pos,dir)
            main_func(positions[1:])
            rollBackFour(pos, dir)
    else: 
        # 5
        # No need to roll back
        countFive(pos)
        main_func(positions[1:])
        rollBackFive(pos)


def countOne(pos, dir):
    return countBlocks(pos,dir)

def rollBackOne(pos, dir):
    rollBack(pos, dir)

def countTwo(pos,dir):
    combination = [[0,1],[2,3]]
    countBlocks(pos,combination[dir][0]) 
    countBlocks(pos,combination[dir][1])

def rollBackTwo(pos,dir):
    combination = [[0,1],[2,3]]
    rollBack(pos,combination[dir][0])
    rollBack(pos,combination[dir][1])

def countThree(pos,dir):
    combination = [[1,2],[2,0],[0,3],[3,1]]
    countBlocks(pos,combination[dir][0])
    countBlocks(pos,combination[dir][1])

def rollBackThree(pos,dir):
    combination = [[1,2],[2,0],[0,3],[3,1]]
    rollBack(pos,combination[dir][0])
    rollBack(pos,combination[dir][1])

def countFour(pos, dir):
    combination = [[1,2,0],[2,0,3],[0,3,1],[3,1,2]]
    countBlocks(pos,combination[dir][0]) 
    countBlocks(pos,combination[dir][1]) 
    countBlocks(pos,combination[dir][2])

def rollBackFour(pos,dir):
    combination = [[1,2,0],[2,0,3],[0,3,1],[3,1,2]]
    rollBack(pos,combination[dir][0])
    rollBack(pos,combination[dir][1])
    rollBack(pos,combination[dir][2])

def countFive(pos):
    for i in range(4):
        countBlocks(pos,i)

def rollBackFive(pos):
    for i in range(4):
        rollBack(pos,i)

main_func(positions)
# print(max_cover)
print(target - max_cover)
