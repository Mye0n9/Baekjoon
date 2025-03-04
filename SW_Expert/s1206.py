import sys

input = sys.stdin.readline

# 어떻게 하면 더 효율적으로 코드를 짜는거지?
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    target = 0
    buildings = list(map(int,input().split()))
    if N >=5:
        for idx in range(2,N-2):
            if buildings[idx] > max(buildings[idx - 2], buildings[idx - 1], buildings[idx + 1], buildings[idx + 2]):
                target += buildings[idx] - max(buildings[idx - 2], buildings[idx - 1], buildings[idx + 1], buildings[idx + 2])
    print(f"#{test_case} {target}")