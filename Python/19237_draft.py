import sys

input = sys.stdin.readline

N,M,K = map(int,input().split())

sharks = [0 for _ in range(M)]
for i in range(N):
    tmp = list(map(int,input().split()))
    for j in range(N):
        if tmp[j] !=0:
            sharks[tmp[j]-1] = [i,j,-1] # r,c,dir

mat = [[[-1,0] for _ in range(N)] for _ in range(N)] # shark num, fragrance

i_directions = list(map(int,input().split())) # 초기 위치 좌표 생성
for idx, i_dir in enumerate(i_directions):
    sharks[idx][2] = i_dir-1 

shark_rule = [list(map(int,input().split())) for _ in range(4*M)] # shark_rule은 1~4로 되어있음
shark_rule = [[element - 1 for element in row] for row in shark_rule]

remove_list = []

dr = [-1,1,0,0]
dc = [0,0,-1,1]

def fragranceUpdate(r,c):
    # 향 지우기
    if mat[r][c][1] >0: 
        mat[r][c][1] -=1
        if mat[r][c][1] == 0:
            mat[r][c][0] = -1

def fragranceWholeUpdate():
    for r in range(N):
        for c in range(N):
            fragranceUpdate(r,c)

def checkBoundary(r,c):
    return True if 0<=r<N and 0<=c<N else False

def sharkMove(shark, shark_num):
    # 향을 남기고 이동
    # 현재 방향을 기준으로 새로운 방향을 찾고 그 방향으로 이동한 지점이 새로운 지점
    r,c,dir = shark
    # 현재 위치에 대해서 향을 남긴다
    mat[r][c] = [shark_num, K]

    n_dir = shark_rule[4*shark_num + dir] # 4 * (0~3) + (0~3)
    # 새로운 지점이 boundary 안에 있는가, 냄새가 없는 칸인가
    # 아니라면 이동
    # 맞다면, 우선순위에 따라 이동: 우선 순위에 따른 냄새가 없는 칸 - 자기 자신의 냄새가 있는 칸
    flag = False
    for i in range(4):
        if checkBoundary(r+dr[n_dir[i]],c+dc[n_dir[i]]) and mat[r+dr[n_dir[i]]][c+dc[n_dir[i]]][0] == -1:
                r += dr[n_dir[i]]
                c += dc[n_dir[i]]
                dir = n_dir[i]
                flag = True # 우선 순위에 따라, 주변에 비어진 칸이 있다면, 그 칸으로 이동
                break
    
    if not flag: # 비어진 칸이 없다면, 주변에 칸들 중 우선 순위에 따라, 본인의 냄새가 있는 쪽으로 이동
        for i in range(4):
            if checkBoundary(r+dr[n_dir[i]],c+dc[n_dir[i]]) and mat[r+dr[n_dir[i]]][c+dc[n_dir[i]]][0] == shark_num:
                r += dr[n_dir[i]]
                c += dc[n_dir[i]]
                dir = n_dir[i]
    return [r,c,dir]

# 이렇게 상어를 움직인 다음에, 겹치는게 있다면 비교해서 날려버리기 (날릴 때, remove list로 해버리자)

def oneMove():
    global remove_list # 날라가는 상어가 있다면 여기다가 저장
    new_sharks = []
    for shark_num, shark in enumerate(sharks):
        if shark_num not in remove_list:
            new_shark = (sharkMove(shark, shark_num))
            flag = False # 날라갔음을 나타내는 플래그그
            # direction을 제외하고 겹치는게 있는지 확인
            for big_shark in new_sharks:
                if big_shark[0:2] == new_shark[0:2]:
                    remove_list.append(shark_num) # 날라감을 표시
                    new_sharks.append([-1,-1,-1])
                    flag = True
            if not flag:
                new_sharks.append(new_shark)
        else:
            new_sharks.append([-1,-1,-1]) # 날라감을 표시하기 위한 값
    return new_sharks

itr = 0
while len(remove_list) != M-1:
    if itr >= 1000:
        print(-1)
        exit()
    fragranceWholeUpdate()
    itr+=1
    sharks = oneMove()
    print(sharks)

print(itr)