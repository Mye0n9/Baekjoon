import sys

input = sys.stdin.readline

n, m = map(int, input().split())
r, c, d = map(int, input().split())

mat = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


def cleaner(x, y, d):
    cnt = 0
    while True:

        if mat[x][y] == 0:
            mat[x][y] = -1 
            cnt += 1

        for _ in range(4):
            d = (d+3) % 4
            nx, ny = x + dx[d], y + dy[d]
            if in_range(nx, ny) and mat[nx][ny] == 0:
                x, y = nx, ny
                break

        else:
            x, y = x + dx[d] * (-1), y + dy[d] * (-1)
            if in_range(x, y) and mat[x][y] == 1 or not in_range(x,y):
                print(cnt)
                return

cleaner(r, c, d)