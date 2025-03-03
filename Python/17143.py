import sys

input = sys.stdin.readline

R, C, M = map(int, input().split())

if M == 0:
    print(0)
    exit()

sharks = {}  # (r, c) -> [s, d, z]
res = 0

for _ in range(M):
    r, c, s, d, z = map(int, input().split())
    sharks[(r - 1, c - 1)] = [s, d, z]

# 방향: 1: 위, 2: 아래, 3: 오른쪽, 4: 왼쪽
dr = [-1, 1, 0, 0]
dc = [0, 0, 1, -1]

# 방향을 0-indexed로 조정
direction_map = {1: 0, 2: 1, 3: 2, 4: 3}
for key in sharks:
    sharks[key][1] = direction_map[sharks[key][1]]


def move_sharks():
    """ 상어를 이동시킨 후 새로운 위치를 업데이트하는 함수 """
    new_sharks = {}

    for (r, c), (s, d, z) in sharks.items():
        if d in [0, 1]:  # 위/아래 방향 이동
            cycle = (R - 1) * 2
        else:  # 좌/우 방향 이동
            cycle = (C - 1) * 2

        move_steps = s % cycle  # 불필요한 이동 줄이기

        for _ in range(move_steps):
            nr, nc = r + dr[d], c + dc[d]
            if 0 <= nr < R and 0 <= nc < C:
                r, c = nr, nc
            else:  # 벽에 부딪히면 방향 변경
                d ^= 1  # (0 ↔ 1), (2 ↔ 3)
                r, c = r + dr[d], c + dc[d]

        # 새로운 위치에 상어가 존재하는 경우 크기 비교
        if (r, c) in new_sharks:
            if new_sharks[(r, c)][2] < z:
                new_sharks[(r, c)] = [s, d, z]
        else:
            new_sharks[(r, c)] = [s, d, z]

    return new_sharks


# 1. 낚시왕이 오른쪽으로 한 칸씩 이동
for c in range(C):
    # 2. 낚시왕이 있는 열에서 가장 가까운 상어를 잡는다.
    for r in range(R):
        if (r, c) in sharks:
            res += sharks[(r, c)][2]  # 상어 크기 추가
            del sharks[(r, c)]
            break

    # 3. 상어 이동
    sharks = move_sharks()

print(res)