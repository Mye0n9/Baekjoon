# 다시 풀어보자
from collections import deque

N, M, T = map(int, input().split())
mat = [deque(map(int, input().split())) for _ in range(N)]
moves = [list(map(int, input().split())) for _ in range(T)]

# 방향: 동(→), 서(←), 남(↓), 북(↑)
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]

# 원판 회전 함수
def rotate(row, direction, k):
    row.rotate(k if direction == 0 else -k)

# 원판 회전 실행 함수
def action(move):
    r, d, k = move
    multiple = r
    while multiple <= N:
        rotate(mat[multiple - 1], d, k)
        multiple += r

# 좌표 이동 (경계 처리)
def getNextPos(r, c, direction):
    nr, nc = r + dr[direction], c + dc[direction]
    if nc >= M:  # 오른쪽 경계를 넘어가면 왼쪽으로 연결
        nc = 0
    elif nc < 0:  # 왼쪽 경계를 넘어가면 오른쪽으로 연결
        nc = M - 1
    return nr, nc

# 같은 숫자 제거 (없으면 평균 조정)
def removeAdjacent():
    visit = [[False] * M for _ in range(N)]
    remove = set()
    total, count = 0, 0  # 전체 합과 숫자 개수

    for i in range(N):
        for j in range(M):
            if mat[i][j] != 0 and not visit[i][j]:
                value = mat[i][j]
                queue = deque([(i, j)])
                visit[i][j] = True
                group = [(i, j)]  # 같은 숫자를 저장하는 리스트

                while queue:
                    r, c = queue.popleft()
                    for d in range(4):
                        nr, nc = getNextPos(r, c, d)
                        if 0 <= nr < N and not visit[nr][nc] and mat[nr][nc] == value:
                            visit[nr][nc] = True
                            queue.append((nr, nc))
                            group.append((nr, nc))

                if len(group) > 1:
                    remove.update(group)

            if mat[i][j] != 0:
                total += mat[i][j]
                count += 1

    if remove:  # 같은 숫자들을 제거
        for r, c in remove:
            mat[r][c] = 0
        return True  # 숫자가 제거되었음을 반환

    if count > 0:  # 같은 숫자가 없으면 평균값으로 조정
        avg = total / count
        for i in range(N):
            for j in range(M):
                if mat[i][j] != 0:
                    if mat[i][j] > avg:
                        mat[i][j] -= 1
                    elif mat[i][j] < avg:
                        mat[i][j] += 1
    return False  # 숫자가 제거되지 않음

# 시뮬레이션 실행
for move in moves:
    action(move)
    removeAdjacent()

# 최종 남은 숫자의 합 출력
print(sum(sum(row) for row in mat))
