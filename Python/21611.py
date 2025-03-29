N, M = map(int,input().split())

board = [list(map(int,input().split())) for _ in range(N)]
command = [list(map(int,input().split())) for _ in range(M)]

# 얼음 파편 용 방향: 위, 아래, 왼, 오

dr= [0,-1,1,0,0]
dc = [0,0,0,-1,1]

break_record = 0

def checkBoundary(r,c):
    return True if 0<=r<N and 0<=c<N else False

def showMatrix(mat):
    for i in range(N):
        for j in range(N):
            print(mat[i][j], end= ' ')
        print()
    print()

def breakBids(d,s):
    global break_record
    pr, pc = (N-1)//2, (N-1)//2
    for _ in range(s):
        if checkBoundary(pr+dr[d],pc+dc[d]):
            pr+=dr[d]
            pc+=dc[d]
            board[pr][pc] = 0

def moveBids():
    r, c = (N-1)//2, (N-1)//2
    n_list = []

    direction, scale = 0, 1
    # 왼, 아래, 오, 위
    m_dr = [0,1,0,-1]
    m_dc = [-1,0,1,0]

    while checkBoundary(r,c):
        for _ in range(scale):
            r+=m_dr[direction]
            c+=m_dc[direction]
            if checkBoundary(r,c) and board[r][c] !=0:
                n_list.append(board[r][c])

        direction += 1
        if direction %2 ==0:
            if direction == 4:
                direction = 0
            scale+=1
    return n_list

def clearContinuous(flat_board):
    global break_record
    range_list = [0 for _ in range(len(flat_board))]
    n_list = []
    p_val = -1

    cnt = 1
    for i in range(len(flat_board)):
        if i == 0:
            p_val = flat_board[i]
        else:
            if flat_board[i] == p_val: # 같다면 그냥 계속 흘러가게
                cnt+=1
            else:
                if cnt >=4:
                    break_record += (p_val * cnt)
                    for j in range(i-cnt, i):
                        range_list[j] = 1# 이만큼 동안 겹쳤음
                p_val = flat_board[i]
                cnt=1
    # 마지막 체크
    if cnt >= 4:
        break_record += (p_val * cnt)
        for j in range(len(flat_board)-1-cnt, len(flat_board)):
            range_list[j] = 1

    for i in range(len(flat_board)):
        if range_list[i] == 0:
            n_list.append(flat_board[i])

    return n_list

def formingNewGroups(flat_board):
    p_val = -1
    cnt = 1
    n_list = []

    for i in range(len(flat_board)):
        if p_val == -1:
            if flat_board[i] > 0:
                p_val = flat_board[i]
        else:
            if flat_board[i] == p_val: # 같다면 그냥 계속 흘러가게
                cnt+=1
            else:
                n_list.append(cnt)
                n_list.append(p_val)

                p_val = flat_board[i]
                cnt=1
    # 마지막 고려
    if p_val > 0:
        n_list.append(cnt)
        n_list.append(p_val)
    return n_list

def putInToTwoDimension(flat_board):
    n_board = [[0 for _ in range(N)] for _ in range(N)]
    r, c = (N-1)//2, (N-1)//2
    idx = 0

    flag = True

    direction, scale = 0, 1
    # 왼, 아래, 오, 위
    m_dr = [0,1,0,-1]
    m_dc = [-1,0,1,0]

    while flag and checkBoundary(r,c):
        for _ in range(scale):
            if idx == len(flat_board):
                flag = False
                break

            r+=m_dr[direction]
            c+=m_dc[direction]
            if checkBoundary(r,c):
                n_board[r][c] = flat_board[idx]
                idx+=1
            else:
                break

        direction += 1
        if direction %2 ==0:
            if direction == 4:
                direction = 0
            scale+=1
    return n_board

for d,s in command:
    breakBids(d,s)

    n_flat_board = moveBids()
    p_len = len(n_flat_board)
    n_flat_board = clearContinuous(n_flat_board)


    while p_len != len(n_flat_board):
        p_len = len(n_flat_board)
        n_flat_board = clearContinuous(n_flat_board)


    n_flat_board = formingNewGroups(n_flat_board)

    board = putInToTwoDimension(n_flat_board)

print(break_record)

