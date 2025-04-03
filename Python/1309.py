n = int(input())

if n == 1:
    print(3)
    exit()


dp = [1,3,7]

for _ in range(2,n+1):
    dp[2] = dp[0] * 3 + (dp[1]-dp[0])*2
    dp[0] = dp[1]
    dp[1] = dp[2]

print(dp[2]%9901)