import sys

input = sys.stdin.readline

max_val = -1e9
min_val = 1e9

N = int(input())
vals = list(map(int,input().split()))

operators = list(map(int,input().split()))

def operation(idx, val1, val2):
    if idx == 0:
        return val1+val2
    elif idx == 1:
        return val1-val2
    elif idx == 2:
        return val1*val2
    else:
        return val1 // val2 if val1 > 0 else -(-val1 // val2)

def main_func(idx, val): # idx는 몇번째 값들끼리 연산을 하는지
    global max_val, min_val
    if idx == N-1:
        max_val = max(max_val, val)
        min_val = min((min_val,val))
        return
    
    if operators[0] >0:
        operators[0] -=1
        main_func(idx+1, val+vals[idx+1])
        operators[0] +=1
    
    if operators[1] > 0:
        operators[1] -=1
        main_func(idx+1, val-vals[idx+1])
        operators[1] +=1
    
    if operators[2] >0:
        operators[2] -=1
        main_func(idx+1, val*vals[idx+1])
        operators[2] +=1
    
    if operators[3] >0:
        operators[3] -=1
        main_func(idx+1, int(val/vals[idx+1]))
        operators[3] +=1
    
main_func(0, vals[0])
print(max_val)
print(min_val)