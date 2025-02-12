import sys
from collections import deque

F, S, G, U, D = map(int, sys.stdin.readline().split())

if S == G:
    print(0)
    sys.exit()

queue = deque([(S, 0)])
visited = [0] * (F + 1)
visited[S] = 1

while queue:
    val, cnt = queue.popleft()
    
    for next_val in (val + U, val - D):
        if 1 <= next_val <= F and visited[next_val] == 0:
            if next_val == G:
                print(cnt + 1)
                sys.exit()
            visited[next_val] = 1
            queue.append((next_val, cnt + 1))

print("use the stairs")
