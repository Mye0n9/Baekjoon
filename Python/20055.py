import sys
from collections import deque

input = sys.stdin.readline

N, K = map(int,input().split())

A = deque(list(map(int,input().split())))
belt = deque([False]*N)
itr = 0
while True:
    itr+=1
    A.rotate(1)
    belt.rotate(1)

    belt[N-1] = False

    for i in range(N-2, -1, -1):
        if belt[i] and not belt[i+1] and A[i+1] > 0:
            belt[i], belt[i+1] = False, True
            A[i+1]-=1
    
    belt[N-1] = False
    if A[0] >0:
        belt[0] = True
        A[0] -=1
    
    if A.count(0) >= K: break

print(itr)
