import sys
from collections import deque

sys.setrecursionlimit(10000)

mat = [0]*100001

def dOp(a):
    return (a*2) % 10000

def sOp(a):
    return (a-1)%10000

def lOp(a):
    return (a%1000) * 10 + a//1000

def rOp(a):
    return (a%10)*1000 + a//10

n = int(sys.stdin.readline())

for _ in range(n):
    a,b = map(int, sys.stdin.readline().strip().split())
    
    Q = deque()
    Q.append([a,''])
    mat[a] = 1

    while Q:
        val, cmd = Q.popleft()

        if val == b:
            print(cmd)
            break
        else:
            d = dOp(val)
            if(mat[d] == 0):
                Q.append([d, cmd+'D'])
                mat[d] = 1

            s = sOp(val)
            if(mat[s] == 0):
                Q.append([s,cmd+'S'])
                mat[s] = 1
            
            l = lOp(val)
            if(mat[l] == 0):
                Q.append([l,cmd+'L'])
                mat[l] = 1
            
            r = rOp(val)
            if(mat[r] == 0):
                Q.append([r, cmd+'R'])
                mat[r] = 1