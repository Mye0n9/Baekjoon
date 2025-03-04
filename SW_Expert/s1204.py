import sys

input = sys.stdin.readline

T = int(input())

for test_case in range(1, T + 1):
    _ = input()
    nums = list(map(int,input().split()))
    max_num = max(nums)
    idx_list = [0 for _ in range(max_num+1)]

    for num in nums:
        idx_list[num] += 1
    
    answer = len(idx_list) -1 -idx_list[::-1].index(max(idx_list))
    print(f"#{test_case} {answer}")