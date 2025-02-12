import sys
from collections import deque


def check_boundary(r,c):
    # Check whether it has contact with boundary
    if 0<=r<N and 0<=c<N:
        return True
    else: False

input = sys.stdin.readline

N = int(input())
K = int(input())

mat = [[0 for _ in range(N)] for _ in range(N)]

for _ in range(K):
    r,c = map(int, input().split())
    mat[r-1][c-1] = 1

L = int(input())
commands = {}
for _ in range(L):
    key, value = map(str,input().split())
    commands[int(key)] = value

snake = deque([[0,0]])
# North: 0, East: 1, South: 2, West: 3
direction = 1
time = 0
while True:
   
    # Move
    dr,dc = 0,0
    if(direction == 0):dr,dc = -1,0
    elif(direction==1):dr,dc = 0,1
    elif(direction==2):dr,dc = 1,0
    else: dr,dc = 0,-1

    nr = snake[0][0]+dr
    nc = snake[0][1]+dc

    snake.appendleft([nr,nc])

    # Check Body Collision
    if snake.count([nr,nc])>1:
        break
    
    if not check_boundary(snake[0][0],snake[0][1]):
        break

    # Check Apple
    if mat[snake[0][0]][snake[0][1]] == 1:
        mat[snake[0][0]][snake[0][1]] = 0
    else:
        snake.pop()
    # Increment
    time+=1

     # Check Command
    if time in commands.keys():
        if commands[time] == 'D':
            direction = (direction+1)%4
        else:
            if direction == 0 : direction = 3
            else: direction  = (direction - 1)%4
    
print(time+1)