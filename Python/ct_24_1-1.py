from collections import deque
import copy
# 0. 생성 가능한 유물 수를 확인하는 코드
dr = [1,-1,0,0]
dc = [0,0,1,-1]
def checkBoundary(r,c):
    return True if 0<=r<5 and 0<=c<5 else False

def showMatrix(mat):
    for r in range(5):
        for c in range(5):
            print(mat[r][c],end= '')
        print()
    print()

def getTreasure(mat):
    visited = [[0 for _ in range(5)] for _ in range(5)]
    t_pos = []
    def bfs (r,c):
        Q = deque([])
        Q.append([r,c])
        out = [[r,c]]
        visited[r][c] = 1
        while Q:
            pr, pc = Q.popleft()
            for d in range(4):
                nr, nc = pr+dr[d], pc+dc[d]
                if checkBoundary(nr,nc) and visited[nr][nc] == 0 and mat[nr][nc] == mat[r][c]:
                    visited[nr][nc] = 1
                    out.append([nr,nc])
                    Q.append([nr,nc])
        return out

    for i in range (5):
        for j in range(5):
            out = bfs(i,j)
            if len(out) >= 3:
                t_pos.extend(out)

    return len(t_pos), t_pos

# Flip이 이상하게 된듯
def rotateBoard(pr,pc,degree):
    tmp = copy.deepcopy(board)
    for r in range(3):
        for c in range(3):
            if degree == 0: # 90
                tmp[pr+c][pc+3-1-r] = board[pr+r][pc+c]
            elif degree == 1:
                tmp[pr+3-1-r][pc+3-1-c] = board[pr+r][pc+c]
            else:
                tmp[pr+3-1-c][pc+r] = board[pr+r][pc+c]
    return tmp

# 1. 5x5 안에 행 1~3, 열 1~3을 움직이면서, 회전 시키고, 유물의 수를 최대로 만드는 방법을 만들기
def stepOne():
    res = []
    mat = []
    val = -1
    for dg in range(3): # 90, 180, 270
        for c in range(3): # 열이 가장 작은 구간
            for r in range(3): # 행이 가장 작은 구간
                n_tmp = rotateBoard(r,c,dg)
                num, treasures = getTreasure(n_tmp)
                # print(dg,c,r,num,treasures)
                if num > val:
                    val = num
                    res = treasures
                    mat = n_tmp
    return val, res, mat

# 2. 유물 채우기

def fillUp(mat):
    n_mat = copy.deepcopy(mat)
    for c in range(5):
        for r in range(4,-1,-1):
            if n_mat[r][c] == 0:
                # if idx < len(orders):
                n_mat[r][c] = wall.popleft()
                # else:
                #     board[r][c] = orders[-1]
    return n_mat



if __name__ == '__main__':
    K, M = map(int,input().split())

    board = [list(map(int,input().split())) for _ in range(5)]

    wall = deque(list(map(int,input().split())))
    for i in range(K):
        # print('K:',i)
        value, positions, board = stepOne()
        score = value
        for pos in positions:
            board[pos[0]][pos[1]] = 0

        board = fillUp(board)
        while True:
            cnt, targets = getTreasure(board)
            score+=cnt
            if cnt == 0:
                break
            else:
                for target in targets:
                    board[target[0]][target[1]] = 0
                board = fillUp(board)
        if score>0:
            print(score,end=' ')
        else:
            break