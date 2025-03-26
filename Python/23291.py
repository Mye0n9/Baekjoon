from collections import deque
from traceback import print_tb

N, K = map(int,input().split())

board = [[-1 for _ in range(N)] for _ in range(N)]

# height랑 row 정보 저장
height_info = [1 for _ in range(N)]
row_info = [0 for _ in range(N)]
row_info[-1] = N


tmp = list(map(int,input().split()))
for i in range(N):
    board[-1][i] = tmp[i]

def checkBoundary(r,c):
    return True if 0<=r<N and 0<=c<N else False

def showMatrix(mat):
    for i in range(N):
        for j in range(N):
            print(mat[i][j],end=' ')
        print()
    print()

def increment():
    min_idx = []
    min_val = float('inf')
    for idx in range(N):
        if board[-1][idx] < min_val:
            min_idx = []
            min_idx.append(idx)
            min_val = board[-1][idx]
        elif board[-1][idx] == min_val:
            min_idx.append(idx)

    for idx in min_idx:
        board[-1][idx] += 1

def stackOne():
    tmp = board[-1][0]
    board[-2][1] = tmp
    board[-1][0] = -1

    # update height and row list
    height_info[0] = 0
    height_info[1] = 2

    row_info[N-1] -=1
    row_info[N-2] +=1

def stackFlip():
    flipIdx = []
    for i in range(N):
        if height_info[i] >= 2:
            flipIdx.append(i)

    # 하기 전에 가능한지 여부를 따져봐야한다.
    a = row_info[-1] - len(flipIdx) # 넘겼을 때의 바닥의 길이
    b = height_info[flipIdx[-1]] # 넘기려고 하는 애의 높이

    if b > a:
        return False

    flip_board = []
    for idx in flipIdx:
        tmp = []
        for i in range(N):
            if board[i][idx] != -1:
                tmp.insert(0,board[i][idx])
                board[i][idx] = -1
                height_info[idx] -=1
                row_info[i] -=1
        flip_board.insert(0,tmp)

    r,c = (height_info[flipIdx[-1]+1]), flipIdx[-1]+1
    # 쌓기 시작하는 지점: N-1-r , c

    for i in range(len(flip_board)):
        for j in range(len(flip_board[0])):
            board[N-1-r-i][c+j] = flip_board[i][j]
            height_info[c+j]+=1
            row_info[N-1-r-i]+=1

    # print('row:',row_info)
    # print('height:',height_info)
    # showMatrix(board)

    return True

dr = [1,-1,0,0]
dc = [0,0,1,-1]

def adjust():
    inc_record = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for direction in range(4):
                if checkBoundary(i+dr[direction],j+dc[direction]) and board[i][j] != -1 and board[i+dr[direction]][j+dc[direction]] != -1:
                    if board[i][j] >= board[i+dr[direction]][j+dc[direction]]:
                        inc_record[i][j] -= (board[i][j]-board[i+dr[direction]][j+dc[direction]])//5
                    else:
                        inc_record[i][j] += (board[i + dr[direction]][j + dc[direction]] - board[i][j]) // 5

    for i in range(N):
        for j in range(N):
            board[i][j] += inc_record[i][j]

def makeFlat():
    global height_info, row_info
    n_board = [[-1 for _ in range(N)] for _ in range(N)]
    cnt = 0
    for j in range(N):
        for i in range(N-1,-1,-1):
            if board[i][j] != -1:
                n_board[N-1][cnt] = board[i][j]
                cnt+=1

    # Initialize Height and Row info
    height_info = [1 for _ in range(N)]
    row_info = [0 for _ in range(N)]
    row_info[-1] = N

    return n_board

def stackFlipTwo():
    # Step One
    for i in range(N//2):
        board[N-2][N//2+i] = board[N-1][N//2-1-i]
        board[N - 1][N // 2 - 1 - i] = -1
        # Update Height and Row info
        height_info[N//2+i] +=1
        height_info[N // 2 - 1 - i] -= 1


    row_info[N-2],row_info[N-1] = N//2, N//2

    # Step Two
    pr,pc = height_info[N//2+N//4], N//2+N//4
    mat = deque([])

    for j in range(N//2+N//4-1,-1,-1):
        for i in range(N):
            if board[i][j] != -1:
                mat.append(board[i][j])
                board[i][j] = -1

    for c in range(pc,N):
        idx = 0
        for r in range(N-1,-1,-1):
            if idx == 2:
                break

            if board[r][c] == -1:
                board[r][c] = mat.popleft()
                idx+=1


    # for i in range(N//4):
    #     for j in range(N//4):
    #         board[N-1-pr-i][N-1-j] = board[N//2+N//4+i][N//2+j]
    #         board[N // 2 + N // 4 + i][N // 2 + j] = -1

def getTarget():
    return max(board[-1]) - min(board[-1])

def oneCycle():
    global board

    cond = True
    increment()
    stackOne()
    while cond:
        cond = stackFlip()
    adjust()
    board = makeFlat()
    stackFlipTwo()
    adjust()
    board=makeFlat()

ans = 0
while getTarget() > K:
    ans+=1
    oneCycle()

print(ans)