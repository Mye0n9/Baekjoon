import sys

input = sys.stdin.readline

N,M,K = map(int,input().split())

mat = [[[-1,0] for _ in range(N)] for _ in range(N)] # 냄새 주인, 냄새 남아있는 시간

sharks = [0 for _ in range(M)]

for i in range(N):
    tmp = list(map(int,input().split()))
    for j in range(N):
        if tmp[j] != 0:
            sharks[tmp[j]-1] = [i,j]

i_directions = list(map(int,input().split()))
for idx, i_direction in enumerate(i_directions):
    sharks[idx].append(i_direction-1)

def leaveSmell():
    for shark_idx, shark in enumerate(sharks): 
        r,c,_ = shark
        if r != -1:
            mat[r][c] = [shark_idx,K]

leaveSmell() # 초기 값으로 세팅

moveRule = []
for _ in range(4*M):
    moveRule.append(list(map(int,input().split())))

turns = [[-1,0],[1,0],[0,-1],[0,1]]
shark_num = M

def checkBoundary(r,c):
    return True if 0<=r<N and 0<=c<N else False

def sharkMove(shark_idx):
    r,c,i_dir = sharks[shark_idx]
    # i_dir 기반으로 다음 위치 정보 찾기
    if r != -1: # 죽은 상어가 아니라면
        n_directions = moveRule[4*shark_idx + i_dir]

        for dir in range(4): # 비어있는 공간 찾기
            dr, dc = turns[n_directions[dir]-1]
            if checkBoundary(r+dr,c+dc) and mat[r+dr][c+dc] == [-1,0]:
                sharks[shark_idx] = [r+dr,c+dc,n_directions[dir]-1]
                return
        
        for dir in range(4): # 자기 냄새 있는 공간 찾기기
            dr, dc = turns[n_directions[dir]-1]
            if checkBoundary(r+dr,c+dc) and mat[r+dr][c+dc][0] == shark_idx:
                sharks[shark_idx] = [r+dr,c+dc,n_directions[dir]-1]
                return

def check_dead_shark():
    dead_num = 0
    for i in range(M):
        if sharks[i][0] == -1:
            continue

        for j in range(i+1,M):
            if sharks[j][0] == -1:
                continue

            if sharks[i][0] == sharks[j][0] and sharks[i][1] == sharks[j][1]:
                dead = max(i,j)
                sharks[dead][0] = -1 # 죽은거 표시하기 위해서 -1로 표기
                dead_num += 1
    return dead_num


def everySharksMove():
    global shark_num
    for shark_idx in range(M):
        sharkMove(shark_idx)
    # 움직였을 때, 같은 공간에 있는가
    dead_num = check_dead_shark() # 삭제해 주는 함수
    shark_num-=dead_num

def updateSmell():
    for i in range(N):
        for j in range(N):
            if mat[i][j][1] > 0:
                mat[i][j][1] -= 1
                if mat[i][j][1] == 0:
                    mat[i][j][0] = -1

def main_func():
    everySharksMove() # 상어가 다음 움직였을때의 위치 정보 저장
    updateSmell()
    leaveSmell() # 변경된 위치에 상어가 냄새를 남긴다.


itr = 0
while shark_num > 1:
    if itr >= 1000:
        print(-1)
        exit()
    itr+=1
    main_func()

print(itr)
# for i in range(N):
#     for j in range(N):
#         print(mat[i][j],end='')
#     print()