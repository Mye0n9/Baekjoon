import sys

n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().strip().split()))

res, left, right = 0,0,0
counter = dict()
distinct = 0

for right in range(n):
    if arr[right] in counter:
        counter[arr[right]]+=1
    else:
        counter[arr[right]] = 1
        distinct +=1
    
    while distinct > 2:
        counter[arr[left]] -=1
        if counter[arr[left]] == 0:
            del counter[arr[left]]
            distinct -= 1
        left+=1
    res = max(res, right - left + 1)
print(res)
