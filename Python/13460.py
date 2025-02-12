from collections import deque
import sys
input = sys.stdin.readline 
 
N, M = map(int, input().split())
mat = []

for r in range(N):
    tmp = (list(input().strip()))
    if 'R' in tmp:
        rx = r
        ry = tmp.index('R')
    if 'B' in tmp:
        bx = r
        by = tmp.index('B')
    mat.append(tmp)
    
dx = [-1, 1, 0, 0]
dy = [0, 0, -1 ,1]
 
def bfs(rx, ry, bx, by):
    q = deque()
    q.append((rx, ry, bx, by))
    visited = []
    visited.append((rx, ry, bx, by))
    count = 0
    while q:
        for _ in range(len(q)):
            rx, ry, bx, by = q.popleft()
            if count > 10:
                print(-1)
                return
            if mat[rx][ry] == 'O':
                print(count)
                return 
            for i in range(4):
                nrx, nry = rx, ry
                while True:
                    nrx += dx[i]
                    nry += dy[i]
                    if mat[nrx][nry] == '#':
                        nrx -= dx[i]
                        nry -= dy[i]
                        break
                    if mat[nrx][nry] == 'O':
                        break
                nbx, nby = bx, by
                while True: 
                    nbx += dx[i]
                    nby += dy[i]
                    if mat[nbx][nby] == '#': 
                        nbx -= dx[i]
                        nby -= dy[i]
                        break
                    if mat[nbx][nby] == 'O':
                        break
                if mat[nbx][nby] == 'O':
                    continue
                if nrx == nbx and nry == nby:
                    if abs(nrx - rx) + abs(nry - ry) > abs(nbx - bx) + abs(nby - by):
                        nrx -= dx[i]
                        nry -= dy[i]
                    else:
                        nbx -= dx[i]
                        nby -= dy[i]
                if (nrx, nry, nbx, nby) not in visited: 
                    q.append((nrx, nry, nbx, nby))
                    visited.append((nrx, nry, nbx, nby))
        count += 1
    print(-1)
bfs(rx, ry, bx, by)


# import sys
# from collections import deque

# input = sys.stdin.readline

# N,M = map(int,input().split())

# mat = []
# B_QUEUE= deque()
# b_info = [0 for _ in range(5)]
# O = []
# r_cnt, b_cnt = 0,0

# # dir (0: down, 1: up, 2: right, 3: left)
# dr = [1,-1,0,0]
# dc = [0,0,1,-1]

# for r in range(N):
#     tmp = (list(input().strip()))
#     if 'R' in tmp:
#         b_info[0] = r
#         b_info[1] = tmp.index('R')
#     if 'B' in tmp:
#         b_info[2] = r
#         b_info[3] = tmp.index('B')
#     if 'O' in tmp:
#         O = [r,tmp.index('O')]
#     mat.append(tmp)

# B_QUEUE.append(b_info)

# def move(r,c, dir, b_type):
#     # b_type: 0 = R, 1 = B
#     nr = r
#     nc = c
#     distance = 0

#     while mat[nr][nc] != '#' and checkBoundary(nr,nc):
#         if mat[nr][nc] == 'O':
#             break

#         if mat[nr+dr[dir]][nc+dc[dir]] != '#':
#             nr += dr[dir]
#             nc += dc[dir]
#             distance+=1
#         else: break

#     return [nr, nc, distance]

# def checkBoundary(r,c):
#     if(0<=r<N and 0<=c<M): return True
#     else: return False

# res = -1   
# while len(B_QUEUE) != 0:
#     pos_info = B_QUEUE.popleft()
#     # R_r, R,c, B_r, B_c, move
#     if pos_info[4] >= 9: break

#     if pos_info[0:2] == O: 
#         res = pos_info[4]
#         break

#     if pos_info[2:4] == O: continue

#     for dir in range(4):
#         r_next = [pos_info[0]+dr[dir],pos_info[1]+dc[dir]]
#         b_next = [pos_info[2]+dr[dir],pos_info[3]+dc[dir]]

#         if checkBoundary(r_next[0],r_next[1]) and mat[r_next[0]][r_next[1]] != '#':

#             n_red_info = move(pos_info[0],pos_info[1],dir,0)
#             n_blue_info = move(pos_info[2],pos_info[3],dir,1)

#             if n_red_info[0] == n_blue_info[0] and n_red_info[1] == n_blue_info[1]:
#                 if n_red_info[0] == O[0] and n_red_info[1] == O[1]:
#                     break

#                 if n_red_info[2] >= n_blue_info[2]:
#                     n_red_info[0] = n_red_info[0]-dr[dir]
#                     n_red_info[1] = n_red_info[1]-dc[dir]
#                 else:
#                     n_blue_info[0] = n_blue_info[0]-dr[dir]
#                     n_blue_info[1] = n_blue_info[1]-dc[dir]
#             if n_blue_info[0] == O[0] and n_blue_info[1] == O[1]: continue
#             else:
#                 n_info = [n_red_info[0],n_red_info[1],n_blue_info[0],n_blue_info[1],pos_info[4]+1]
#                 B_QUEUE.append(n_info)

# print(res)    


# # 기울기를 기울였을때, 같은 좌표라면, 상대적인 위치, 즉 기존 위치에서 어떤 구슬이 먼저 도착하는지 확인해야함
# # 같은 크기의 매핑을 이용해서 어떤 좌표를 이동했는지도 기록해야하나? 다시 왔다갔다 하지 않기 위해서?
