# 다시 봐야함
from collections import deque

N, M = map(int, input().split())
mat = [list(map(int, input().split())) for _ in range(N)]

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

# 0: 무지개, -1: 검은색, 1~M: 색상, -2: 빈칸


def in_boundary(r, c):
    return 0 <= r < N and 0 <= c < N


def get_standard_block(blocks):
    return min((r, c) for r, c in blocks if mat[r][c] > 0)


def get_group():
    visited = [[False] * N for _ in range(N)]
    best_group = []
    max_rainbow = -1
    best_standard = (-1, -1)
    best_size = -1

    for r in range(N):
        for c in range(N):
            if mat[r][c] <= 0 or visited[r][c]:
                continue

            color = mat[r][c]
            q = deque()
            q.append((r, c))
            group = [(r, c)]
            rainbow = []

            visited[r][c] = True
            local_visited = [[False] * N for _ in range(N)]
            local_visited[r][c] = True

            while q:
                x, y = q.popleft()
                for d in range(4):
                    nx, ny = x + dr[d], y + dc[d]
                    if not in_boundary(nx, ny):
                        continue
                    if visited[nx][ny] or local_visited[nx][ny]:
                        continue
                    if mat[nx][ny] == 0 or mat[nx][ny] == color:
                        q.append((nx, ny))
                        group.append((nx, ny))
                        local_visited[nx][ny] = True
                        if mat[nx][ny] == 0:
                            rainbow.append((nx, ny))
                        else:
                            visited[nx][ny] = True

            if len(group) >= 2:
                rainbow_cnt = len(rainbow)
                standard = get_standard_block(group)

                if len(group) > best_size or \
                   (len(group) == best_size and rainbow_cnt > max_rainbow) or \
                   (len(group) == best_size and rainbow_cnt == max_rainbow and standard > best_standard):
                    best_group = group
                    best_size = len(group)
                    max_rainbow = rainbow_cnt
                    best_standard = standard

    return best_size, best_group


def gravity():
    for c in range(N):
        for r in range(N - 2, -1, -1):
            if mat[r][c] >= 0:
                nr = r
                while True:
                    if nr + 1 >= N or mat[nr + 1][c] != -2:
                        break
                    mat[nr + 1][c] = mat[nr][c]
                    mat[nr][c] = -2
                    nr += 1


def rotate():
    global mat
    mat = list(map(list, zip(*mat)))[::-1]


def remove_group(group):
    for r, c in group:
        mat[r][c] = -2


# main simulation
score = 0
while True:
    size, group = get_group()
    if size < 2:
        break
    score += size ** 2
    remove_group(group)
    gravity()
    rotate()
    gravity()

print(score)
