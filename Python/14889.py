import sys

sys.setrecursionlimit(10000)

def func(num,cnt):
    global answer

    if cnt==n//2: # If one team has been made
        start=0
        link=0
        for i in range(n):
            for j in range(n):
                if not visited[i] and not visited[j]: # Team start's synergy
                    start+=arr[i][j]
                if visited[i] and visited[j]: # Team start's synergy
                    link+=arr[i][j]
        answer=min(answer,abs(start-link))
    else: # Iterate all the possible cases.
        for i in range(num,n):
            if not visited[i]:
                visited[i]=1
                func(i,cnt+1)
                visited[i]=0

input = sys.stdin.readline
n=int(input())

arr=[]
for _ in range(n):
    arr.append(list(map(int,input().split())))

visited=[0 for _ in range(n)]

answer=1e9
func(0,0)
print(answer)