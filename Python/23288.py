from collections import deque

# 입력
n, m, k = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]

# 방향: 동 남 서 북
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

# 주사위 인덱스: [top, front, right, left, back, bottom]
dice = [1, 2, 3, 4, 5, 6]

# 방향 회전 함수
def rotate_dice(dir):
    global dice
    if dir == 0:  # 동
        dice = [dice[3], dice[1], dice[0], dice[5], dice[4], dice[2]]
    elif dir == 1:  # 남
        dice = [dice[1], dice[5], dice[2], dice[3], dice[0], dice[4]]
    elif dir == 2:  # 서
        dice = [dice[2], dice[1], dice[5], dice[0], dice[4], dice[3]]
    elif dir == 3:  # 북
        dice = [dice[4], dice[0], dice[2], dice[3], dice[5], dice[1]]

# 점수 계산: BFS
def get_score(x, y):
    num = board[x][y]
    visited = [[False] * m for _ in range(n)]
    q = deque()
    q.append((x, y))
    visited[x][y] = True
    count = 1

    while q:
        cx, cy = q.popleft()
        for i in range(4):
            nx, ny = cx + dx[i], cy + dy[i]
            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and board[nx][ny] == num:
                visited[nx][ny] = True
                q.append((nx, ny))
                count += 1
    return count * num

# 방향 변경: 주사위 바닥면과 칸의 숫자 비교
def change_dir(dir, bottom, cell):
    if bottom > cell:
        return (dir + 1) % 4  # 시계 방향
    elif bottom < cell:
        return (dir - 1) % 4  # 반시계 방향
    else:
        return dir  # 유지

# 초기 위치 및 방향
x, y, dir = 0, 0, 0
total_score = 0

for _ in range(k):
    # 이동
    nx, ny = x + dx[dir], y + dy[dir]

    # 경계 벗어나면 반대 방향
    if not (0 <= nx < n and 0 <= ny < m):
        dir = (dir + 2) % 4
        nx, ny = x + dx[dir], y + dy[dir]

    # 주사위 굴리기
    rotate_dice(dir)

    # 점수 획득
    total_score += get_score(nx, ny)

    # 방향 조정
    bottom = dice[5]
    cell = board[nx][ny]
    dir = change_dir(dir, bottom, cell)

    # 위치 갱신
    x, y = nx, ny

print(total_score)
