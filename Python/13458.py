import sys
import math

input = sys.stdin.readline

n = int(input())
students = list(map(int, input().split()))
b,c = map(int,input().split())

cnt = n

for i in range(n):
    students[i] -= b

    if students[i] > 0:
        cnt+=math.ceil(students[i]/c)
print(cnt)