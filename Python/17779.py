N = int(input())
pan = [list(map(int, input().split())) for _ in range(N)]

# 5번 선거구 영역 표시 함수 (경계선 + 내부까지)
def getAreaFive(r, c, d1, d2):
    n_mat = [[0] * N for _ in range(N)]

    # 경계선 그리기
    for i in range(d1+1):
        n_mat[r+i][c-i] = 5
        n_mat[r+d2+i][c+d2-i] = 5
    for i in range(d2+1):
        n_mat[r+i][c+i] = 5
        n_mat[r+d1+i][c-d1+i] = 5

    # 경계 내부 채우기
    for i in range(r+1, r+d1+d2):
        flag = False
        for j in range(N):
            if n_mat[i][j] == 5:
                flag = not flag
            elif flag:
                n_mat[i][j] = 5
    return n_mat

# 선거구별 인구 합 계산
def getEachSection(r, c, d1, d2, boundaryMat):
    population = [0] * 5

    for i in range(N):
        for j in range(N):
            # 5번 선거구
            if boundaryMat[i][j] == 5:
                population[4] += pan[i][j]
            # 1번
            elif 0 <= i < r+d1 and 0 <= j <= c:
                population[0] += pan[i][j]
            # 2번
            elif 0 <= i <= r+d2 and c < j < N:
                population[1] += pan[i][j]
            # 3번
            elif r+d1 <= i < N and 0 <= j < c-d1+d2:
                population[2] += pan[i][j]
            # 4번
            elif r+d2 < i < N and c-d1+d2 <= j < N:
                population[3] += pan[i][j]

    return max(population) - min(population)

# 최소 인구 차이 찾기
ans = float('inf')
for x in range(N):
    for y in range(N):
        for d1 in range(1, N):
            for d2 in range(1, N):
                # 조건: 꼭짓점이 범위 내에 있어야 함
                if x + d1 + d2 < N and 0 <= y - d1 and y + d2 < N:
                    boundaryMat = getAreaFive(x, y, d1, d2)
                    diff = getEachSection(x, y, d1, d2, boundaryMat)
                    ans = min(ans, diff)

print(ans)