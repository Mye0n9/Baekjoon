N, K = map(int, input().split())

mat = [list(map(int, input().split())) for _ in range(N)]

# 각 말 정보: [r, c, direction]
pieces = []
board = [[[] for _ in range(N)] for _ in range(N)]

for i in range(K):
    r, c, d = map(int, input().split())
    pieces.append([r-1, c-1, d])
    board[r-1][c-1].append(i)

# 방향: 1→오른쪽, 2→왼쪽, 3→위, 4→아래
dr = [0, 0, 0, -1, 1]
dc = [0, 1, -1, 0, 0]

def reverse_dir(d):
    return d - 1 if d % 2 == 0 else d + 1

def move(i):
    r, c, d = pieces[i]
    nr, nc = r + dr[d], c + dc[d]

    # 말이 현재 위치에서 어느 위치에 있는지 찾기
    idx = board[r][c].index(i)
    moving_stack = board[r][c][idx:]
    board[r][c] = board[r][c][:idx]

    # 범위 밖이거나 파란색이면 방향만 바꾸고 1회 시도
    if not (0 <= nr < N and 0 <= nc < N) or mat[nr][nc] == 2:
        d = reverse_dir(d)
        pieces[i][2] = d
        nr, nc = r + dr[d], c + dc[d]

        if not (0 <= nr < N and 0 <= nc < N) or mat[nr][nc] == 2:
            # 제자리로 되돌림
            board[r][c] += moving_stack
            return False

    # 흰색 or 빨간색
    if mat[nr][nc] == 1:
        moving_stack.reverse()

    for p in moving_stack:
        pieces[p][0], pieces[p][1] = nr, nc
        board[nr][nc].append(p)

    return len(board[nr][nc]) >= 4

turn = 0
while turn <= 1000:
    turn += 1
    for i in range(K):
        if move(i):
            print(turn)
            exit()
print(-1)
