N = int(input())
mat = [list(map(int, input().split())) for _ in range(N)]
min_val = float('inf')

def divide_area(x, y, d1, d2):
    area = [[0] * N for _ in range(N)]

    # 경계선 5번 구역
    for i in range(d1 + 1):
        area[x + i][y - i] = 5
        area[x + d2 + i][y + d2 - i] = 5
    for i in range(d2 + 1):
        area[x + i][y + i] = 5
        area[x + d1 + i][y - d1 + i] = 5

    # 내부 채우기
    for i in range(x + 1, x + d1 + d2):
        fill = False
        for j in range(N):
            if area[i][j] == 5:
                fill = not fill
            if fill:
                area[i][j] = 5

    population = [0] * 5

    for r in range(N):
        for c in range(N):
            if area[r][c] == 5:
                population[4] += mat[r][c]
            elif 0 <= r < x + d1 and 0 <= c <= y:
                population[0] += mat[r][c]
            elif 0 <= r <= x + d2 and y < c < N and r<c:
                population[1] += mat[r][c]
            elif x + d1 <= r < N and 0 <= c < y - d1 + d2 and r>c:
                population[2] += mat[r][c]
            elif x + d2 < r < N and y - d1 + d2 <= c < N:
                population[3] += mat[r][c]


    return max(population) - min(population)

for x in range(N):
    for y in range(N):
        for d1 in range(1, N):
            for d2 in range(1, N):
                if x + d1 + d2 < N and 0 <= y - d1 and y + d2 < N:
                    diff = divide_area(x, y, d1, d2)
                    min_val = min(min_val, diff)

print(min_val)
