N = int(input())

board = []
init_val = 0
for _ in range(N):
    tmp = list(map(int,input().split()))
    for i in range(N):
        init_val+=tmp[i]
    board.append(tmp)

dr = [0,1,0,-1]
dc = [-1,0,1,0]
tornado_log = []
tornado_direction = []
# left(0), down(1), right(2), up(3)
direction = 0
mv_count = 0
scale = 1

pivot = [N//2,N//2]

def checkBoundary(r,c):
    return True if 0<=r<N and 0<=c<N else False

def showMatrix(mat):
    for i in range(N):
        for j in range(N):
            print(mat[i][j],end = '')
        print()

def tornadoMove(pivot):
    global mv_count, direction,scale
    r,c = pivot[0], pivot[1]
    if mv_count == 2:
        scale+=1
        mv_count = 0

    for _ in range(scale):
        r,c = r + dr[direction], c + dc[direction]
        tornado_log.append([r,c])
        tornado_direction.append(direction)

    mv_count+=1
    direction = (direction + 1) % 4
    return [r,c]

while checkBoundary(pivot[0],pivot[1]):
    pivot = tornadoMove(pivot)

spreadPos = [[-2,0],[-1,-1],[-1,0],[-1,1],[0,-2],[1,-1],[1,0],[1,1],[2,0]] # 이걸 회전 시켜야 함
spreadAmt = [0.02,0.1,0.07,0.01,0.05,0.1,0.07,0.01,0.02]

def spreadSand(r,c,direction):
    total = 0
    # ratio
    if direction == 0:
        for i in range(len(spreadPos)):
            nr, nc = r+spreadPos[i][0], c+spreadPos[i][1]
            amt = int(board[r][c] * spreadAmt[i])
            if checkBoundary(nr,nc):
                board[nr][nc]+=amt
            total += amt
        # a
        nr,nc = r,c-1
        if checkBoundary(nr,nc):
            board[nr][nc] += board[r][c]-total
            # print(board[r][c]-total)
    elif direction == 1:
        for i in range(len(spreadPos)):
            nr, nc = r-spreadPos[i][1], c-spreadPos[i][0]
            amt = int(board[r][c] * spreadAmt[i])
            if checkBoundary(nr,nc):
                board[nr][nc]+=amt
            total += amt
        # a
        nr,nc = r+1,c
        if checkBoundary(nr,nc):
            board[nr][nc] += board[r][c]-total
            # print(board[r][c]-total)
    elif direction == 2:
        for i in range(len(spreadPos)):
            nr, nc = r-spreadPos[i][0], c-spreadPos[i][1]
            amt = int(board[r][c] * spreadAmt[i])
            if checkBoundary(nr,nc):
                board[nr][nc]+=amt
            total += amt
        # a
        nr,nc = r,c+1
        if checkBoundary(nr,nc):
            board[nr][nc] += board[r][c]-total
            # print(board[r][c]-total)
    else:
        for i in range(len(spreadPos)):
            nr, nc = r+spreadPos[i][1], c+spreadPos[i][0]
            amt = int(board[r][c] * spreadAmt[i])
            if checkBoundary(nr,nc):
                board[nr][nc]+=amt
            total += amt
        # a
        nr,nc = r-1,c
        if checkBoundary(nr,nc):
            board[nr][nc] += board[r][c]-total
            # print(board[r][c]-total)
    # print(total)
    board[r][c] = 0


tornado_log = tornado_log[:-1]

for i in range(len(tornado_log)):
    spreadSand(tornado_log[i][0],tornado_log[i][1],tornado_direction[i])
    # showMatrix(board)
    # print()

final_val = 0

for i in range(N):
    for j in range(N):
        final_val+=board[i][j]

print(init_val - final_val)


