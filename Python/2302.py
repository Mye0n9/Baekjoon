N = int(input())
cases = [0 for _ in range(N+1)]
# N이 1일때의 코너케이스 발생
cases[0] = 1 # 0일때 초기화 안하면 안됨
cases[1] = 1
cases[2] = 2
for i in range(3,N+1):
    cases[i] = cases[i-1]+cases[i-2] # 점화식 유도는 잘함

M = int(input())
num = 1
if M > 0:
    priv = 0
    for _ in range(M):
        vip = int(input())
        num *= cases[vip-1-priv]
        priv = vip
    num *= cases[N-priv]
else:
    num = cases[N]

print(num)