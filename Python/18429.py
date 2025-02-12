import sys

input = sys.stdin.readline

N,K = map(int, input().split())

increase = list(map(int,input().split()))

p = 500
cnt = 0

def bt(date, performance, arr):
    global cnt
    if date == N:
        cnt+=1
        return
    
    for idx, val in enumerate(arr):
        if performance + val - K >= 500:
            bt(date+1,performance + val - K,arr[:idx]+arr[idx+1:])

bt(0,p,increase)
print(cnt)

    
    
