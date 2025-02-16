import sys

input = sys.stdin.readline

N, M = map(int,input().split())

houses = []
chickens = []
combinations = []

max_val = 9999

for i in range(N):
    tmp = list(map(int,input().split()))
    for j in range(N):
        if tmp[j] == 1:
            houses.append([i,j])
        elif tmp[j] == 2:
            chickens.append([i,j])

total_chickens = len(chickens)
        
def dfs(depth, index, combination):
    if depth >= M:
        combinations.append(combination.copy())
        return
    else:
        for s in range(index, total_chickens):
            combination.append(s)
            dfs(depth+1, s+1,combination)
            combination.pop()

dfs(0,0,[])

for comb in combinations:
    val = 0
    for h in houses:
        tmp = 9999
        for c in comb: # index
            dist = (abs(h[0]-chickens[c][0]) + abs(h[1]-chickens[c][1]))
            # print(f"c: dist: ", c, dist)
            tmp = min(tmp, dist)# 선택된 치킨집 조합에 대해서 각각의 길이를 구하고, 그 중에서 가장 최소 값으로 설정
        val += tmp # 각 집에 대한 최소 distance를 더해준다.
        # print("val: ", val)
    max_val = min(max_val, val) # 한 조합에 대한 최소값들의 합 중에서 가장 최소값을 구한다.


print(max_val)
