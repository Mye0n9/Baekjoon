# 다시 풀어보자

N, M, K = map(int, input().split())

# 초기 파이어볼 배열 생성
arr = [[[] for _ in range(N)] for _ in range(N)]
for _ in range(M):
    r, c, m, s, d = map(int, input().split())
    arr[r-1][c-1].append([m, s, d])  # 인덱스 0부터 시작

# 방향 정의
directions = [(-1, 0), (-1, 1), (0, 1), (1, 1),
              (1, 0), (1, -1), (0, -1), (-1, -1)]

for _ in range(K):
    # 이동 결과를 저장할 새로운 배열
    board = [[[] for _ in range(N)] for _ in range(N)]
    
    # 모든 파이어볼 이동
    for i in range(N):
        for j in range(N):
            for m, s, d in arr[i][j]:
                dr, dc = directions[d]
                nr = (i + dr * s) % N
                nc = (j + dc * s) % N
                board[nr][nc].append([m, s, d])
    
    # 병합 및 분할 처리
    for i in range(N):
        for j in range(N):
            if len(board[i][j]) < 2:
                continue

            total_m, total_s = 0, 0
            even_dir = odd_dir = 0

            for m, s, d in board[i][j]:
                total_m += m
                total_s += s
                if d % 2 == 0:
                    even_dir += 1
                else:
                    odd_dir += 1

            new_m = total_m // 5
            if new_m == 0:
                board[i][j] = []
                continue

            new_s = total_s // len(board[i][j])
            if even_dir == 0 or odd_dir == 0:
                new_dirs = [0, 2, 4, 6]
            else:
                new_dirs = [1, 3, 5, 7]

            board[i][j] = []
            for d in new_dirs:
                board[i][j].append([new_m, new_s, d])
    
    arr = board  # 다음 턴을 위한 상태 업데이트

# 남은 파이어볼 질량 합계 출력
result = 0
for i in range(N):
    for j in range(N):
        for m, s, d in arr[i][j]:
            result += m

print(result)
