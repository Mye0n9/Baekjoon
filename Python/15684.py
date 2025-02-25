import sys
input = sys.stdin.readline

N, M, H = map(int, input().split())

mat = [[0] * N for _ in range(H)]
positions = []

for _ in range(M):
    i, j = map(int, input().split())
    mat[i-1][j-1] = 1  # 오른쪽으로 가라
    mat[i-1][j] = 2  # 왼쪽으로 가라

def checkOverlap(candidates):
    return any((candidates[i][0] == candidates[i+1][0] and abs(candidates[i][1] - candidates[i+1][1]) == 1)
               for i in range(len(candidates) - 1))

def checkBoundary(r, c):
    return 0 <= r < H and 0 <= c < N

for i in range(H):
    for j in range(N-1):  # 오른쪽을 봐야 하므로 N-1까지 탐색
        if mat[i][j] == 0 and mat[i][j+1] == 0:
            positions.append([i, j])

def path(start):
    r, c = start
    while r < H:
        if mat[r][c] == 1:
            c += 1
        elif mat[r][c] == 2:
            c -= 1
        r += 1
    return c

def check(): # 재귀가 아니라 반복문으로 최적화
    return all(i == path([0, i]) for i in range(N))

def dfs(depth, index, length, combination): # 전역 변수로 저장하는게 아니라 함수 내에서 저장해서 나오게 하는 식으로 설정
    if depth >= length:
        return [combination[:]]
    result = []
    for s in range(index, len(positions)):
        combination.append(s)
        result.extend(dfs(depth+1, s+1, length, combination))
        combination.pop()
    return result

def main_func(): # deepcopy 사용 대신, 원래값으로 변경하는 식으로 작성
    if check():
        return 0

    # 1개 추가
    for i, j in positions:
        mat[i][j], mat[i][j+1] = 1, 2
        if check():
            return 1
        mat[i][j], mat[i][j+1] = 0, 0

    # 2개 추가
    for comb in dfs(0, 0, 2, []):
        tmp = [positions[comb[0]], positions[comb[1]]]
        if not checkOverlap(tmp):
            for i, j in tmp:
                mat[i][j], mat[i][j+1] = 1, 2
            if check():
                return 2
            for i, j in tmp:
                mat[i][j], mat[i][j+1] = 0, 0

    # 3개 추가
    for comb in dfs(0, 0, 3, []):
        tmp = [positions[comb[0]], positions[comb[1]], positions[comb[2]]]
        if not checkOverlap(tmp):
            for i, j in tmp:
                mat[i][j], mat[i][j+1] = 1, 2
            if check():
                return 3
            for i, j in tmp:
                mat[i][j], mat[i][j+1] = 0, 0

    return -1

print(main_func())



# 시간 초과 나온다. 다른 방법으로 풀 수 있나?
# import sys
# from copy import deepcopy
# Pypy3 
# input= sys.stdin.readline

# N,M,H = map(int,input().split())

# mat = [[0 for _ in range(N)]for _ in range(H)]
# positions = []
# combinations = []

# for _ in range(M):
#     i,j = map(int,input().split())
#     mat[i-1][j-1] = 1 # 오른쪽으로 가라
#     mat[i-1][j] = 2 # 왼쪽으로 가라

# def checkOverlap(candidates):
#     itr = len(candidates)
#     condition = False
#     for i in range(itr):
#         # 같은 행에 1 column 차이면 안됨
#         if (candidates[i%itr][0] == candidates[(i+1)%itr][0]) and (abs(candidates[i%itr][1] - candidates[(i+1)%itr][1]) == 1):
#             return True
#     return condition


# def checkBoundary(r,c):
#     return True if 0<=r<H and 0<=c<N else False

# # 다리 놓을 수 있는 position 찾기
# # 두 가로선이 연속하거나 서로 접하면 안 된다
# for i in range(H):
#     for j in range(N):
#         if mat[i][j] == 0: # 연결된 지점이 아니고
#             if (checkBoundary(i,j+1) and mat[i][j+1] == 0):
#             # if (checkBoundary(i,j-1) and mat[i][j-1] == 0) and (checkBoundary(i,j+1) and mat[i][j+1] == 0):
#                 # 양 옆에 값이 1 혹은 2 (연결됨을 의미)가 아니라면
#                 positions.append([i,j]) # 해당 지점을 positions에 넣는다.

# # 신경써야할점: position 들 중에서 넣게 되면 같이 넣을 수 없는 position도 생김

# def path(start, n_mat): # 하나의 시작 지점에서 마지막에 도착하는 지점
#     r,c = start

#     if n_mat[r][c] == 1:
#         nc = c+1
#     elif n_mat[r][c] == 2:
#         nc = c-1
#     else:
#         nc = c
#     nr = r+1
#     if checkBoundary(nr,nc):
#         return path([nr,nc], n_mat)
#     else:
#         return nc

# def check(n_mat): # 전부 제대로 i -> i 로 가는지 확인
#     cnt = 0
#     for i in range(N):
#         if i == path([0,i],n_mat):
#             cnt+=1
    
#     return cnt == N

# def dfs(depth, index, length, combination):
#     if depth >= length:
#         combinations.append(combination[:])
#         return

#     for s in range(index, len(positions)):
#         combination.append(s)
#         dfs(depth+1, s+1, length, combination)
#         combination.pop()

# # 1개만 넣을때는 그냥 positions 순회하면서 진행
# # len(positions) C 2
# # len(positions) C 3

# def main_func():
#     global combinations
#     # 초기 상태에서 가능한지
#     if check(mat):
#         return 0
#     # 1개만 추가했을때, 순회 돌면서 새로운 matrix 생성
#     n_mat = deepcopy(mat)
#     for i,j in positions:
#         n_mat[i][j] = 1
#         n_mat[i][j+1] = 2
#         if check(n_mat):
#             return 1
#         n_mat = deepcopy(mat)
#     # 2개 추가 했을 시, 2개일때의 조합 구한 다음에 진행
#     dfs(0,0,2,[])
#     for comb in combinations:
#         tmp = [positions[comb[0]],positions[comb[1]]]
#         if not checkOverlap(tmp):
#             for i,j in tmp:
#                 n_mat[i][j] = 1
#                 n_mat[i][j+1] = 2
#             if check(n_mat): return 2
#         n_mat = deepcopy(mat)
    
#     combinations=[]
#     # 3개 추가 했을 시, 3개일때의 조합 구한 다음에 진행
#     dfs(0,0,3,[])
#     for comb in combinations: # 각각의 3개씩 있는 조합에 대해서
#         tmp = [positions[comb[0]],positions[comb[1]],positions[comb[2]]]
#         if not checkOverlap(tmp): # 경로가 접하지 않는다면
#             for i,j in tmp: # 각각의 위치 정보를 꺼내서
#                 n_mat[i][j] = 1 # 업데이트를 해준다.
#                 n_mat[i][j+1] = 2
#             if check(n_mat): return 3 # 업데이트 된게 같다면 결과 출력
#         n_mat = deepcopy(mat) # 다시 경로 정보 되돌리기
#     return -1

# print(main_func())