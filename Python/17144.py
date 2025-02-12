import sys

input = sys.stdin.readline
R,C,T = map(int,input().split())

mat = []
clean = []

for i in range(R):
    tmp = (list(map(int,input().split())))
    if tmp[0] == -1: clean.append(i)
    mat.append(tmp)

change_mat = [[0 for _ in range(C)] for _ in range(R)]

def check_boundary(r,c):
    return True if 0<=r<R and 0<=c<C else False

dr = [1,-1,0,0]
dc = [0,0,1,-1]

def check_expansion(r,c): # O(1)
    cnt = 0
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if check_boundary(nr,nc) and mat[nr][nc] != -1: 
            change_mat[nr][nc] += int(mat[r][c]/5)
            cnt+=1
    change_mat[r][c] -= cnt * int(mat[r][c]/5)

def expansion(): # O(R*C)
    for i in range(R):
        for j in range(C):
            if mat[i][j]>=5 and check_boundary(i,j):
                check_expansion(i,j)

    for i in range(R):
        for j in range(C):
            mat[i][j] += change_mat[i][j]

topDirection = [[0,1],[-1,0],[0,-1],[1,0]]
bottomDirection = [[0,1],[1,0],[0,-1],[-1,0]]

def shift(pos, directions):
    # 우, 상, 좌, 하
    idx = 0
    nr = pos
    nc = 0
    tmpOne= 0
    tmpTwo = 0
    flag = True
    while True:

        if not check_boundary(nr+directions[idx][0],nc+directions[idx][1]): # change direction
            idx = (idx+1)%4

        nr += directions[idx][0]
        nc += directions[idx][1]

        if flag == True: # 첫번째 shift
            tmpOne = mat[nr][nc]
            mat[nr][nc] = 0
            flag = False
        else: # 그 외의 shift 경우
            tmpTwo = mat[nr][nc]
            mat[nr][nc] = tmpOne
            tmpOne = tmpTwo

        if nr == pos and nc == 0: break # 기존으로 돌아오면 종료

for _ in range(T):
    expansion()
    shift(clean[0],topDirection)
    mat[clean[0]][0] = -1
    shift(clean[1],bottomDirection)
    mat[clean[1]][0] = -1
    change_mat = [[0 for _ in range(C)] for _ in range(R)]


res = 0
for i in range(R):
    for j in range(C):
        res += mat[i][j]
print(res+2)
