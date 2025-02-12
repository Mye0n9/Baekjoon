import sys

from collections import deque

n = int(sys.stdin.readline())
s, t = map(int,sys.stdin.readline().split())

itr = int(sys.stdin.readline())

mat = [[] for _ in range(n+1)]

for _ in range(itr):
    x,y = map(int,sys.stdin.readline().split())
    if y not in mat[x]: mat[x].append(y)
    if x not in mat[y]: mat[y].append(x)

visited = [0 for _ in range(n+1)]

queue = deque()
queue.append([s,0])

val,cnt = 0,0
res = -1

while queue:
    val, cnt = queue.popleft()
    
    if val == t:
        res = cnt
        break
    
    visited[val] = 1
    for i in mat[val]:
        if visited[i] == 0:
            queue.append([i, cnt+1])
print(res)