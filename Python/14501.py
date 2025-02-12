N = int(input())

ti, pi = [], []
for _ in range(N):
    t, p = map(int, input().split())
    ti.append(t)
    pi.append(p)

dp = [0] * (N + 1)
for day in range(N - 1, -1, -1):
    case1 = dp[day + 1]
    case2 = 0
    if day + ti[day] <= N:
        case2 = dp[day + ti[day]] + pi[day]
    dp[day] = max(case1, case2)

print(dp[0])
