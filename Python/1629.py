import sys

a,b,c = map(int,sys.stdin.readline().split())

def operation(a, b, c):
    if b == 1:
        return a % c

    tmp = operation(a, b // 2, c)

    if b % 2 == 1:
        return ((tmp * tmp) % c) * a % c
    else:
        return (tmp * tmp) % c

print(operation(a,b,c))