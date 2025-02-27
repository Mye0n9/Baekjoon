import sys

input = sys.stdin.readline

R,C,M = map(int,input().split())

mat = [[0 for _ in range(C)] for _ in range(R)]
sharks = []

for _ in range(M):
    r,c,s,d,z = map(int,input().split())
    sharks.append([r-1,c-1,s,d,z])

def checkBoundary(r,c):
    return True if 0<=r<R and 0<=c<C else False

dr = [-1,1,0,0]
dc = [0,0,1,-1]
# 1: 위, 2: 아래, 3: 오, 4: 아래

def move(shark): # 각 한번씩 이동 할 때의 move
    r,c,s,d,z = shark
    itr = s
    while itr:
        if checkBoundary(r+dr[d-1],c+dc[d-1]): # 새로운 좌표가 격자안에 있다면
            nr = r + dr[d-1]
            nc = c + dc[d-1]
        else:
            # 방향 전환: 위 <-> 아래, 왼 <-> 오
            if d%2 == 1:
                d+=1
            else:
                d-=1
            nr = r + dr[d-1]
            nc = c + dc[d-1]
        r = nr
        c = nc
        itr -= 1
    return [r,c,s,d,z]

# 잡힌 정보, 먹힌 정보 처리
# 작은 애들부터 먼저 이동 시키면, 이동 했을 때, 크기 비교해서 가능?