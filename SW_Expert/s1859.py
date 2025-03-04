import sys

input = sys.stdin.readline

T = int(input())

for test_case in range(1, T + 1):
    # D = int(input())
    # price = list(map(int,input().split()))
    # max_val = 0

    # def dfs(D, day, budget, pile):
    #     global max_val
    #     if day == D-1:
    #         # 마지막 날에는 판매만
    #         budget += pile * price[day]
    #         max_val = max(max_val, budget)
    #         return
        
    #     # 구매하는 경우
    #     dfs(D,day+1, budget-price[day],pile+1)
    #     # 판매하는 경우
    #     dfs(D,day+1,budget+price[day]*pile,0) # 전체 다 팔아버리는경우

    # dfs(D,0,0,0)
    # print(f"#{test_case} {max_val}")

# 재귀로 푸는 방법: 시간초과 난다

    n = int(input())
    data = list(map(int, input().split()))
    
    max_val = 0
    
    while True :
        max_data = max(data)
        index = data.index(max_data)
        max_val += ( max_data * index ) - sum(data[:index]) # 가장 큰 값을 가진 index 전까지 구매하고 팔아버리기
        
        if index == len(data) - 1 : # index가 마지막이라면 끝내기
            break
            
        data = data[index+1:] # list slicing해서 새롭게 다시 진행하기
    print(f"#{test_case} {max_val}")
