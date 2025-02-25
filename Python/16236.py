import sys
from collections import deque

input = sys.stdin.readline

N = int(input())
mat = []
shark = []
shark_size = 2
shark_eat = 0

for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        if row[j] == 9:
            shark = [i, j]  # 상어 위치 저장
    mat.append(row)

total_time = 0
dr = [-1, 0, 0, 1]  # 상, 좌, 우, 하 (우선순위 적용)
dc = [0, -1, 1, 0]


def bfs():
    global shark_size
    queue = deque([[shark[0], shark[1], 0]])  # [r, c, 이동거리]
    visited = [[False] * N for _ in range(N)]
    visited[shark[0]][shark[1]] = True
    fish_list = []  # 먹을 수 있는 물고기 후보

    while queue:
        r, c, move = queue.popleft()

        for i in range(4):  # 상, 좌, 우, 하 순서
            nr, nc = r + dr[i], c + dc[i]

            if 0 <= nr < N and 0 <= nc < N and not visited[nr][nc]:
                if mat[nr][nc] <= shark_size:  # 이동 가능
                    queue.append([nr, nc, move + 1])
                    visited[nr][nc] = True
                    if 0 < mat[nr][nc] < shark_size:  # 먹을 수 있는 물고기
                        fish_list.append((move + 1, nr, nc))

    # 먹을 수 있는 물고기 리스트를 정렬하여 가장 가까운 물고기 선택
    return sorted(fish_list)


while True:
    fish_list = bfs()  # BFS 한 번만 실행하여 물고기 찾기

    if not fish_list:  # 먹을 물고기가 없으면 종료
        break

    # 가장 가까운 물고기 선택
    step, fish_r, fish_c = fish_list[0]
    total_time += step

    # 물고기를 먹고 상어 위치 변경
    mat[shark[0]][shark[1]] = 0  # 기존 상어 자리 비우기
    shark = [fish_r, fish_c]
    mat[fish_r][fish_c] = 9  # 새로운 위치에 상어 배치

    # 상어가 먹은 개수 증가
    shark_eat += 1
    if shark_eat == shark_size:  # 먹은 개수가 크기와 같으면 크기 증가
        shark_size += 1
        shark_eat = 0

print(total_time)
