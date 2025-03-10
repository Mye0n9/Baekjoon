import sys
from copy import deepcopy

input = sys.stdin.readline

# 0은 제외하고 구현해보자

mat = [[[0,0] for _ in range(4)] for _ in range(4)]
fishes = [[-1,-1] for _ in range(17)] # index 에 따른 위치 정보를 담자

for i in range(4):
    tmp = list(map(int,input().split()))
    for j in range(4):
        fishes[tmp[2*j]] = [i,j] # 생선 위치 정보 담기
        mat[i][j] = [tmp[2*j],tmp[2*j+1]] # index랑 방향 담기

# row and column
directions = [
    [0,0], [-1,0], [-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1]
    # 0 은 패스
    # 1: 상, 2: 좌상, 3: 좌, 4: 좌하, 5: 하, 6: 우하, 7: 우 8: 우상
]

shark_loc = [0,0] # 시작은 0,0
shark_dir = mat[0][0][1]
# Init: 상어가 먼저 0,0 위치에 생선을 먹는다. 먹는 건 -1로 표기

fishes[mat[0][0][0]][0] = -1 # fishes 정보 반영
mat[0][0] = [-1,-1] # matrix 정보 반영
# 빈공간은 [0,0], 상어가 있는 공간은 [-1,-1]로 저장

max_fish = 0

def checkBoundary(r,c):
    return True if 0<=r<4 and 0<=c<4 else False

def getNewDirection(dir):
    return dir+1 if dir<8 else 1

def moveFishes(mat, fishes, shark_loc):
    # 격자 안에 있으면서 상어 위치가 아니라면 서로 자리를 바꾼다.
    # 불가능 하다면 방향을 바꾼다.
    new_mat = deepcopy(mat)
    new_fishes = deepcopy(fishes)
    for idx in range(1,17):
        # 잡아 먹힌 생선이 아니라면 진행
        if new_fishes[idx][0] != -1:
            r, c = new_fishes[idx]
            dir = new_mat[r][c][1]
            # 격자 안에 없거나 or 상어 위치라면
            while not checkBoundary(r+directions[dir][0],c+directions[dir][1]) or (r+directions[dir][0] == shark_loc[0] and c+directions[dir][1] == shark_loc[1]):
                # fishes의 정보랑 mat의 정보 둘 다 바꾸어야함
                dir = getNewDirection(dir)
            # fishes 정보
            new_fishes[idx] = [r+directions[dir][0],c+directions[dir][1]]
            new_fishes[new_mat[r+directions[dir][0]][c+directions[dir][1]][0]] = [r,c]
            # mat 정보
            new_mat[r][c] = new_mat[r+directions[dir][0]][c+directions[dir][1]]
            new_mat[r+directions[dir][0]][c+directions[dir][1]] = [idx,dir]
    return new_mat, new_fishes

# 상어가 먹을 수 있는 option 구하기
def availableFish(mat, shark):
    shark_loc, shark_dir = shark
    r,c = shark_loc
    fishes = []
    dr,dc = directions[shark_dir]
    while checkBoundary(r+dr,c+dc) and mat[r+dr][c+dc][0] != -1:
        fishes.append([r+dr,c+dc])
        r+=dr
        c+=dc
    return fishes

# def main_func(mat, fishes, shark, cumulative):
#     global max_fish

#     new_mat = deepcopy(mat)
#     new_fishes = deepcopy(fishes)

#     new_mat, new_fishes = moveFishes(new_mat, new_fishes, shark[0]) # 물고기 움직인 matrix
#     prey_list = availableFish(new_mat, shark) # 움직인 matrix에서 현재 상어 위치에서 몇개 먹을 수 있는지

#     if len(prey_list) == 0:
#         max_fish = max(max_fish, cumulative) # 상어가 먹을 수 있는 양 계산: 0 개라면 최대값과 비교
#         return
    
#     shark_loc, shark_dir = shark
    
#     for prey in prey_list:
#         # 상어 위치 조정
#         new_shark = [prey, new_mat[prey[0]][prey[1]][1]]
#         # 기존에 상어 있던 위치는 [0,0]으로 조정

#         new_mat[shark_loc[0]][shark_loc[1]] = [0,0]

#         original_fishes_info =  new_fishes[new_mat[prey[0]][prey[1]][0]][0] # 기존 먹으려고 하는 생선의 위치 정보 저장장
#         original_mat_info = new_mat[prey[0]][prey[1]] # matrix에 있는 생선의 번호와 방향 정보
        
#         new_fishes[new_mat[prey[0]][prey[1]][0]][0] = -1 # fishes 정보 반영
#         new_mat[prey[0]][prey[1]] = [-1,-1] # matrix 정보 반영

#         main_func(new_mat, new_fishes, new_shark, cumulative + original_mat_info[0])
#         # roll back 해주기
#         new_fishes[new_mat[prey[0]][prey[1]][0]][0] = original_fishes_info
#         new_mat[prey[0]][prey[1]] = original_mat_info

def main_func(mat, fishes, shark, cumulative):
    global max_fish

    # deepcopy 해서 새로운 상태 복사
    new_mat = deepcopy(mat)
    new_fishes = deepcopy(fishes)

    new_mat, new_fishes = moveFishes(new_mat, new_fishes, shark[0])
    prey_list = availableFish(new_mat, shark)

    if len(prey_list) == 0:
        max_fish = max(max_fish, cumulative)
        return

    shark_loc, shark_dir = shark

    for prey in prey_list:
        prey_num, prey_dir = new_mat[prey[0]][prey[1]]

        copied_mat = deepcopy(new_mat)
        copied_fishes = deepcopy(new_fishes)

        copied_mat[shark_loc[0]][shark_loc[1]] = [0, 0]  # 상어가 있던 자리는 빈칸
        copied_mat[prey[0]][prey[1]] = [-1, -1]  # 상어가 먹은 자리는 상어로
        copied_fishes[prey_num][0] = -1  # 먹힌 물고기 처리

        main_func(copied_mat, copied_fishes, [prey, prey_dir], cumulative + prey_num)


main_func(mat,fishes,[shark_loc, shark_dir],0)
print(max_fish)