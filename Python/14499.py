import sys
from collections import deque

input = sys.stdin.readline

N,M,x,y,itr = map(int,input().split())

mat = [list(map(int,input().split())) for _ in range(N)]

horizontal = deque([0,0,0,0])
vertical = deque([0,0,0,0])

def boundary_check(x,y):
    if 0<=x<N and 0<=y<M:
        return True
    else: return False

def move(cmd):
    global x,y,vertical, horizontal
    if cmd == 1:
        nx = x
        ny = y+1

        if boundary_check(nx,ny):
            tmp = horizontal.pop()
            horizontal.appendleft(tmp)
            # change the matrix
            if(mat[nx][ny] == 0):
                mat[nx][ny] = horizontal[3]
            else:
                # change the dice
                horizontal[3] = mat[nx][ny]
                mat[nx][ny] = 0
            # allow two queues to be align
            vertical[1] = horizontal[1]
            vertical[3] = horizontal[3]
        else:
            return
    elif cmd == 2:
        nx = x
        ny = y-1

        if boundary_check(nx,ny):
            tmp = horizontal.popleft()
            horizontal.append(tmp)
             # change the matrix
            if(mat[nx][ny] == 0):
                mat[nx][ny] = horizontal[3]
            else:
                # change the dice
                horizontal[3] = mat[nx][ny]
                mat[nx][ny] = 0
            
            # allow two queues to be align
            vertical[1] = horizontal[1]
            vertical[3] = horizontal[3]
        else:
            return
    elif cmd == 3:
        nx = x-1
        ny = y

        if boundary_check(nx,ny):
            tmp = vertical.popleft()
            vertical.append(tmp)
             # change the matrix
            if(mat[nx][ny] == 0):
                mat[nx][ny] = vertical[3]
            else:
                # change the dice
                vertical[3] = mat[nx][ny]
                mat[nx][ny] = 0
            # allow two queues to be align
            horizontal[1] = vertical[1]
            horizontal[3] = vertical[3]
        else:
            return
    else:
        nx = x+1
        ny = y

        if boundary_check(nx,ny):
            tmp = vertical.pop()
            vertical.appendleft(tmp)
            # change the matrix
            if(mat[nx][ny] == 0):
                mat[nx][ny] = vertical[3]
            else:
                # change the dice
                vertical[3] = mat[nx][ny]
                mat[nx][ny] = 0
            # allow two queues to be align
            horizontal[1] = vertical[1]
            horizontal[3] = vertical[3]
        else:
            # ignore the command
            return
    x = nx
    y = ny
    print(vertical[1])

for cmd in list(map(int, input().split())):
    move(cmd)