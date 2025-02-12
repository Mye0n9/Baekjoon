import sys

def cain (m,n,x,y):
    val = x
    while val<=m*n:
        if(val-x)%m == 0 and (val-y)%n ==0:
            return val
        val+=m
    return -1

itr = int(sys.stdin.readline())

for _ in range(itr):
    m,n,x,y = map(int, sys.stdin.readline().split())
    print(cain(m,n,x,y))