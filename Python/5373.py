def showMatrix(mat):
    for i in range(18):
        for j in range(3):
            print(mat[i][j], end='')
        print()

def showTop(mat):
    for i in range(3):
        for j in range(3):
            print(mat[i][j],end='')
        print()

def rotateTarget(side, direction):
    # 자기 자신을 돌리는 것
    n_mat = [['' for _ in range(3)] for _ in range(3)]
    if direction == '+': # 시계 방향
        for i in range(N):
            for j in range(N):
                n_mat[j][N-1-i] = totalMat[side*3+i][j]
    else:
        for i in range(N):
            for j in range(N):
                n_mat[N-1-j][i] = totalMat[side*3+i][j]

    for i in range(N):
        for j in range(N):
            totalMat[side*3+i][j] = n_mat[i][j]

def rotateSurroundings(target, direction):
    temp = [0]*3
    if target == 'U':
        # U: F, R, B, L의 윗줄
        if direction == '+':
            for i in range(3):
                temp[i] = totalMat[2 * 3][i]
            for i in range(3):
                totalMat[2 * 3][i] = totalMat[5 * 3][i]
                totalMat[5 * 3][i] = totalMat[3 * 3][i]
                totalMat[3 * 3][i] = totalMat[4 * 3][i]
                totalMat[4 * 3][i] = temp[i]
        else:
            for i in range(3):
                temp[i] = totalMat[2 * 3][i]
            for i in range(3):
                totalMat[2 * 3][i] = totalMat[4 * 3][i]
                totalMat[4 * 3][i] = totalMat[3 * 3][i]
                totalMat[3 * 3][i] = totalMat[5 * 3][i]
                totalMat[5 * 3][i] = temp[i]

    elif target == 'D':
        # D: F, L, B, R의 아랫줄
        if direction == '+':
            for i in range(3):
                temp[i] = totalMat[2 * 3 + 2][i]
            for i in range(3):
                totalMat[2 * 3 + 2][i] = totalMat[4 * 3 + 2][i]
                totalMat[4 * 3 + 2][i] = totalMat[3 * 3 + 2][i]
                totalMat[3 * 3 + 2][i] = totalMat[5 * 3 + 2][i]
                totalMat[5 * 3 + 2][i] = temp[i]
        else:
            for i in range(3):
                temp[i] = totalMat[2 * 3 + 2][i]
            for i in range(3):
                totalMat[2 * 3 + 2][i] = totalMat[5 * 3 + 2][i]
                totalMat[5 * 3 + 2][i] = totalMat[3 * 3 + 2][i]
                totalMat[3 * 3 + 2][i] = totalMat[4 * 3 + 2][i]
                totalMat[4 * 3 + 2][i] = temp[i]

    elif target == 'F':
        # F: U ↓, R ←, D ↑, L →
        if direction == '+':
            for i in range(3):
                temp[i] = totalMat[0 * 3 + 2][i]
            for i in range(3):
                totalMat[0 * 3 + 2][i] = totalMat[4 * 3 + 2 - i][2]
                totalMat[4 * 3 + 2 - i][2] = totalMat[1 * 3][2 - i]
                totalMat[1 * 3][2 - i] = totalMat[5 * 3 + i][0]
                totalMat[5 * 3 + i][0] = temp[i]
        else:
            for i in range(3):
                temp[i] = totalMat[0 * 3 + 2][i]
            for i in range(3):
                totalMat[0 * 3 + 2][i] = totalMat[5 * 3 + i][0]
                totalMat[5 * 3 + i][0] = totalMat[1 * 3][2 - i]
                totalMat[1 * 3][2 - i] = totalMat[4 * 3 + 2 - i][2]
                totalMat[4 * 3 + 2 - i][2] = temp[i]

    elif target == 'B':
        # B: U ↑, L ←, D ↓, R →
        if direction == '+':
            for i in range(3):
                temp[i] = totalMat[0 * 3][i]
            for i in range(3):
                totalMat[0 * 3][i] = totalMat[5 * 3 + i][2]
                totalMat[5 * 3 + i][2] = totalMat[1 * 3 + 2][2 - i]
                totalMat[1 * 3 + 2][2 - i] = totalMat[4 * 3 + 2 - i][0]
                totalMat[4 * 3 + 2 - i][0] = temp[i]
        else:
            for i in range(3):
                temp[i] = totalMat[0 * 3][i]
            for i in range(3):
                totalMat[0 * 3][i] = totalMat[4 * 3 + 2 - i][0]
                totalMat[4 * 3 + 2 - i][0] = totalMat[1 * 3 + 2][2 - i]
                totalMat[1 * 3 + 2][2 - i] = totalMat[5 * 3 + i][2]
                totalMat[5 * 3 + i][2] = temp[i]

    elif target == 'L':
        # L: U ←, B →, D ←, F ←
        if direction == '+':
            for i in range(3):
                temp[i] = totalMat[0 * 3 + i][0]
            for i in range(3):
                totalMat[0 * 3 + i][0] = totalMat[3 * 3 + 2 - i][2]
                totalMat[3 * 3 + 2 - i][2] = totalMat[1 * 3 + i][0]
                totalMat[1 * 3 + i][0] = totalMat[2 * 3 + i][0]
                totalMat[2 * 3 + i][0] = temp[i]
        else:
            for i in range(3):
                temp[i] = totalMat[0 * 3 + i][0]
            for i in range(3):
                totalMat[0 * 3 + i][0] = totalMat[2 * 3 + i][0]
                totalMat[2 * 3 + i][0] = totalMat[1 * 3 + i][0]
                totalMat[1 * 3 + i][0] = totalMat[3 * 3 + 2 - i][2]
                totalMat[3 * 3 + 2 - i][2] = temp[i]

    elif target == 'R':
        # R: U →, F →, D →, B ←
        if direction == '+':
            for i in range(3):
                temp[i] = totalMat[0 * 3 + i][2]
            for i in range(3):
                totalMat[0 * 3 + i][2] = totalMat[2 * 3 + i][2]
                totalMat[2 * 3 + i][2] = totalMat[1 * 3 + i][2]
                totalMat[1 * 3 + i][2] = totalMat[3 * 3 + 2 - i][0]
                totalMat[3 * 3 + 2 - i][0] = temp[i]
        else:
            for i in range(3):
                temp[i] = totalMat[0 * 3 + i][2]
            for i in range(3):
                totalMat[0 * 3 + i][2] = totalMat[3 * 3 + 2 - i][0]
                totalMat[3 * 3 + 2 - i][0] = totalMat[1 * 3 + i][2]
                totalMat[1 * 3 + i][2] = totalMat[2 * 3 + i][2]
                totalMat[2 * 3 + i][2] = temp[i]


T = int(input())

N = 3
for _ in range(T):
    num = int(input())
    moves = input().split()

    totalMat = [['' for _ in range(3)]for _ in range(18)]
    # Initialization
    idx = 0
    colors= ['w','y','r','o','g','b']
    sides = ['U','D','F','B','L','R']
    # U, D, F, B, L, R
    for i in range(18):
        for j in range(3):
            totalMat[i][j] = colors[i//3]

    for move in moves:
        t, d = move[0], move[1]
        # print(t, d)
        side = sides.index(t)
        rotateSurroundings(t,d)
        rotateTarget(side,d)

    # showMatrix(totalMat)
    showTop(totalMat)
