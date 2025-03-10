import sys
from copy import deepcopy
from collections import deque

input = sys.stdin.readline

N, Q = map(int, input().split())
mat = []

for _ in range(2**N):
    mat.append(list(map(int,input().split())))

visit = [[0 for _ in range(2**N)] for _ in range(2**N)]

Ls = list(map(int,input().split()))
dr, dc = [1,-1,0,0], [0,0,1,-1]

# 파이어 스톰 실행:
# 1. 격자를 2^L x 2^L로 나눈다.
# 2. 격자 내에서 90도로 돌린다.
# 3. 인접하는 얼음의 개수가 3미만이라면, 그 칸의 값 1 다운
# 4. Q 번 진행
# 5. 남아있는 얼음의 합 + 덩어리 크기 확인 (visit 활용한 bfs로 진행)

# 격자 내에 있는 얼음 90도로 돌리기
def rotateRegion(section, L):
    n_section = [[0 for _ in range(2**L)] for _ in range(2**L)]
    for i in range(2**L):
        for j in range(2**L):
            n_section[j][2**L-1-i] = section[i][j]
    return n_section

def rotateMat(L):
    for i in range(2**(N-L)):
        for j in range(2**(N-L)):
            # section 저장
            tmp = []
            # 시작점: 2**L*i, 2**L*j
            for row in (mat[2**L*i:2**(L)*(i+1)]):
                tmp.append(row[2**L*j:2**(L)*(j+1)])
            # section 내의 rotate 시키기기
            tmp = rotateRegion(tmp,L)
            # 시작점 기준으로 새롭게 채워넣기
            for k in range(2**L):
                for l in range(2**L):
                    r, c = 2**L*i+k, 2**L*j+l
                    mat[r][c] = tmp[k][l]

# 격자 내에서 인접하는게 2개 이하면 1줄이기

def checkBoundary(r,c):
    return True if 0<=r<2**N and 0<=c<2**N else False

def melt(mat):
    new_mat = deepcopy(mat)
    for r in range(2**N):
        for c in range(2**N):
            cnt = 0
            
            for dir in range(4):
                if checkBoundary(r+dr[dir],c+dc[dir]) and mat[r+dr[dir]][c+dc[dir]] != 0:
                    cnt+=1
            if cnt < 3:
                if mat[r][c] > 0: new_mat[r][c]-=1
    return new_mat
                
# 연결된 덩어리 크기 확인인
def getChunkSize(pos):
    global visit, max_chunk
    Q = deque([])
    Q.append(pos)
    visit[pos[0]][pos[1]] = 1
    cnt = 0

    while Q:
        r,c = Q.popleft()
        cnt+=1
        for dir in range(4):
            if checkBoundary(r+dr[dir],c+dc[dir]) and mat[r+dr[dir]][c+dc[dir]]>0 and visit[r+dr[dir]][c+dc[dir]] == 0:
                Q.append([r+dr[dir],c+dc[dir]])
                visit[r+dr[dir]][c+dc[dir]] = 1
    
    max_chunk = max(max_chunk,cnt)


for L in Ls:
    rotateMat(L)
    mat = melt(mat)

value = 0
max_chunk = 0
# print()
for i in range(2**N):
    for j in range(2**N):
        value+=mat[i][j]
        if visit[i][j] == 0 and mat[i][j] > 0:
            getChunkSize([i,j])
        # print(mat[i][j],end=' ')
    # print()
# print()
print(value)
print(max_chunk)