from collections import deque

# Queue 사용시 메모리 초과

n = int(input())
board = [list(map(int,input().split())) for _ in range(n)]
record = [[0 for _ in range(n)] for _ in range(n)]

def checkBoundary(r,c):
    return True if 0<=r<n and 0<=c<n else False

def showMatrix(mat):
    for i in range(n):
        for j in range(n):
            print(mat[i][j],end=' ')
        print()
    print()

record[0][0] = 1

for i in range(n):
    for j in range(n):
        if board[i][j] == 0: continue
        if j + board[i][j] < n:
            record[i][j + board[i][j]] += record[i][j]
        if i + board[i][j] < n:
            record[i+board[i][j]][j] += record[i][j]

print(record[n-1][n-1])
