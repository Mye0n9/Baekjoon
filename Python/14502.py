import sys
from copy import deepcopy

input = sys.stdin.readline

N,M = map(int,input().split())

mat = []
sources = []
possible_points = []

max_val = 0

dr = [1,-1,0,0]
dc = [0,0,1,-1]

for i in range(N):
    tmp = list(map(int,input().split()))
    for j in range(M):
        if tmp[j] == 0:
            possible_points.append([i,j]) # possible spot for blocks
        elif tmp[j] == 2:
            sources.append([i,j]) # location of original sources
    mat.append(tmp)

def chooseMax(points, depth, remainings):
    global max_val
    if depth == 3:
        safeZone = main_func(points,mat)
        max_val = max(max_val,safeZone)
        return
    
    for idx, remain in enumerate(remainings):
        points.append(remain)
        chooseMax(points,depth+1,remainings[idx+1:])
        points.pop()

def countSafe(mat):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if mat[i][j] == 0:
                cnt +=1
    return cnt

def checkBoundary(r,c):
    return True if 0<=r<N and 0<=c<M else False

def contaminate(r,c,tmp_mat):
    for dir in range(4):
        nr = r + dr[dir]
        nc = c + dc[dir]
        if checkBoundary(nr,nc) and tmp_mat[nr][nc] == 0:
            tmp_mat[nr][nc] = 2
            contaminate(nr,nc,tmp_mat)

def main_func(points, mat):
    tmp_mat = deepcopy(mat)
    for r,c in points: # 벽 세우기
        tmp_mat[r][c] = 1
    
    for r,c in sources:
        contaminate(r,c,tmp_mat)

    return countSafe(tmp_mat)

chooseMax([],0,possible_points)
print(max_val)