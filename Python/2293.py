n,k = map(int,input().split())

coins = [int(input()) for _ in range(n)]

possible = [0 for _ in range(k+1)]
possible[0] = 1

for coin in coins: # 순차적으로 낮은거 부터 전개되기에 가능
    for i in range(coin, k+1):
        possible[i] += possible[i-coin]

print(possible[k])