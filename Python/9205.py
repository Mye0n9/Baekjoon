# INCOMPLETE

import sys
from collections import deque

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = int(input().strip())
    points = []
    flag = False
    for _ in range(n+2):
        points.append(list(map(int,input().split())))
    
    visited = [0 for _ in range(n+2)]
    source = points[0]
    target = points[n+1]

    Q = deque()
    visited[0] = 1
    Q.append(source)
    while Q:
        ref = Q.popleft()

        if ref[0] == target[0] and ref[1] == target[1]:
            flag = True
            break

        for idx, npoint in enumerate(points):
            if visited[idx] ==0 and (0<=abs(npoint[0]-ref[0]) +abs(npoint[1]-ref[1])<=1000):
                visited[idx] = 1
                Q.append(npoint)
    if flag == 1: print("happy")
    else: print("sad")

