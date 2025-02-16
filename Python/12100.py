# import sys
# import copy

# input = sys.stdin.readline

# N = int(input())
# mat = [list(map(int, input().split())) for _ in range(N)]

# # 이동 방향 (동, 서, 남, 북)
# dr = [0, 0, 1, -1]
# dc = [1, -1, 0, 0]

# def move(board, dir):
#     new_board = [[0] * N for _ in range(N)]

#     if dir == 0:  # 동쪽 (오른쪽)
#         for i in range(N):
#             top = N - 1
#             for j in range(N - 1, -1, -1):
#                 if board[i][j]:
#                     tmp = board[i][j]
#                     if new_board[i][top] == 0:
#                         new_board[i][top] = tmp
#                     elif new_board[i][top] == tmp:
#                         new_board[i][top] *= 2
#                         top -= 1
#                     else:
#                         top -= 1
#                         new_board[i][top] = tmp

#     elif dir == 1:  # 서쪽 (왼쪽)
#         for i in range(N):
#             top = 0
#             for j in range(N):
#                 if board[i][j]:
#                     tmp = board[i][j]
#                     if new_board[i][top] == 0:
#                         new_board[i][top] = tmp
#                     elif new_board[i][top] == tmp:
#                         new_board[i][top] *= 2
#                         top += 1
#                     else:
#                         top += 1
#                         new_board[i][top] = tmp

#     elif dir == 2:  # 남쪽 (아래)
#         for j in range(N):
#             top = N - 1
#             for i in range(N - 1, -1, -1):
#                 if board[i][j]:
#                     tmp = board[i][j]
#                     if new_board[top][j] == 0:
#                         new_board[top][j] = tmp
#                     elif new_board[top][j] == tmp:
#                         new_board[top][j] *= 2
#                         top -= 1
#                     else:
#                         top -= 1
#                         new_board[top][j] = tmp

#     else:  # 북쪽 (위)
#         for j in range(N):
#             top = 0
#             for i in range(N):
#                 if board[i][j]:
#                     tmp = board[i][j]
#                     if new_board[top][j] == 0:
#                         new_board[top][j] = tmp
#                     elif new_board[top][j] == tmp:
#                         new_board[top][j] *= 2
#                         top += 1
#                     else:
#                         top += 1
#                         new_board[top][j] = tmp

#     return new_board

# def findBest(board):
#     return max(max(row) for row in board)

# def main_func(board, cnt):
#     global max_val
#     if cnt == 5:
#         max_val = max(max_val, findBest(board))
#         return

#     for dir in range(4):
#         new_board = move(copy.deepcopy(board), dir)
#         if new_board != board:
#             main_func(new_board, cnt + 1)

# max_val = 0
# main_func(mat, 0)
# print(max_val)
from copy import deepcopy

n = int(input())

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

def move(board, dir):
    if dir == 0:  # 동쪽
        for i in range(n):
            top = n - 1
            for j in range(n - 2, -1, -1):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[i][top] == 0:
                        board[i][top] = tmp
                    elif board[i][top] == tmp:
                        board[i][top] = tmp * 2
                        top -= 1
                    else:
                        top -= 1
                        board[i][top] = tmp

    elif dir == 1:  # 서쪽
        for i in range(n):
            top = 0
            for j in range(1, n):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[i][top] == 0:
                        board[i][top] = tmp
                    elif board[i][top] == tmp:
                        board[i][top] = tmp * 2
                        top += 1
                    else:
                        top += 1
                        board[i][top] = tmp

    elif dir == 2:  # 남쪽
        for j in range(n):
            top = n - 1
            for i in range(n - 2, -1, -1):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[top][j] == 0:
                        board[top][j] = tmp
                    elif board[top][j] == tmp:
                        board[top][j] = tmp * 2
                        top -= 1
                    else:
                        top -= 1
                        board[top][j] = tmp

    else:
        for j in range(n):
            top = 0
            for i in range(1, n):
                if board[i][j]:
                    tmp = board[i][j]
                    board[i][j] = 0
                    if board[top][j] == 0:
                        board[top][j] = tmp
                    elif board[top][j] == tmp:
                        board[top][j] = tmp * 2
                        top += 1
                    else:
                        top += 1
                        board[top][j] = tmp

    return board


def dfs(board, cnt):
    global ans
    if cnt == 5:
        for i in range(n):
            for j in range(n):
                ans = max(ans, board[i][j])
        return

    for i in range(4):
        tmp_board = move(deepcopy(board), i)
        dfs(tmp_board, cnt + 1)

ans = 0
dfs(graph, 0)
print(ans)