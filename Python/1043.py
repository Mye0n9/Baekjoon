# INCOMPLETE
import sys

N, M = map(int,sys.stdin.readline().split())

relation = dict()
for i in range(N):
    relation[i+1] = []

target = list(map(int, sys.stdin.readline().split()))

if len(target) == 1: print(M)
else:
    num_target = target[0]
    target = target[1:]
    
    for _ in range(M):
        party = list(map(int, sys.stdin.readline().split()))
