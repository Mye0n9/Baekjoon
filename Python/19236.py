import copy
import sys

input = sys.stdin.readline

mat = [[] for _ in range(4)]

dx = [-1, -1, 0, 1, 1, 1, 0, -1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

for i in range(4):
    data = list(map(int, input().split()))
    fish = []
    for j in range(4):
        # 물고기 번호, 방향
        fish.append([data[2*j], data[2*j+1]-1])
    mat[i] = fish

max_score = 0

# for i in range(4):
#     for j in range(4):
#         print(mat[i][j],end ='')
#     print()

def dfs(sx, sy, score, mat):
    global max_score
    score += mat[sx][sy][0]
    max_score = max(max_score, score)
    mat[sx][sy][0] = 0

    # 물고기 움직임
    for f in range(1, 17):
        f_x, f_y = -1, -1
        for x in range(4):
            for y in range(4):
                if mat[x][y][0] == f: # 해당 하는 번호의 물고기 찾기
                    f_x, f_y = x, y
                    break
        if f_x == -1 and f_y == -1: # 번호의 물고기가 먹혔다면, 다음으로 넘어간다..
            continue
        f_d = mat[f_x][f_y][1] # 해당 하는 번호의 물고기가 있다면, 그 물고기의 방향을 찾는다.

        for i in range(8): 
            nd = (f_d+i) % 8 # 방향 업데이트
            nx = f_x + dx[nd]
            ny = f_y + dy[nd]
            if not (0 <= nx < 4 and 0 <= ny < 4) or (nx == sx and ny == sy):
                # 격자내에 있지 않거나, 상어의 좌표와 같다면 패스스
                continue
            # 업데이트 해주고, swap 해준다.
            mat[f_x][f_y][1] = nd
            mat[f_x][f_y], mat[nx][ny] = mat[nx][ny], mat[f_x][f_y]
            break

    # 상어 먹음
    s_d = mat[sx][sy][1] # 상어의 방향
    for i in range(1, 5):
        # 새로운 상어의 좌표
        nx = sx + dx[s_d]*i
        ny = sy + dy[s_d]*i
        if (0<= nx < 4 and 0<= ny < 4) and mat[nx][ny][0] > 0:
            dfs(nx, ny, score, copy.deepcopy(mat))

dfs(0, 0, 0, mat)
print(max_score)