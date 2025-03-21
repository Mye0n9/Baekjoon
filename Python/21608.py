N = int(input())
f_dict = {}

for _ in range(N*N):
    tmp = list(map(int, input().split()))
    f_dict[tmp[0]] = tmp[1:]

board = [[0 for _ in range(N*N)] for _ in range(N*N)] # matrix

dr = [1,-1,0,0]
dc = [0,0,1,-1]

def showMatrix(mat):
    for i in range(N):
        for j in range(N):
            print(mat[i][j],end = '')
        print()

def checkBounadry(r,c):
    return True if 0<=r<N and 0<=c<N else False

def getNearByFriend(r,c, f_list):
    # 주변 위치를 탐색해서, 친구가 몇 명인지 확인
    cnt = 0
    for direction in range(4):
        nr = r + dr[direction]
        nc = c + dc[direction]
        if checkBounadry(nr,nc) and board[nr][nc] in f_list:
            cnt+=1
    return cnt

def getFriendPosition(n):
    # 비어 있는 칸 중에서 좋아하는 학생이 가장 많은 칸들의 좌표를 반환한다.
    friend_list = f_dict[n]
    max_cnt = -1
    targets = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 0:
                cnt = getNearByFriend(i,j,friend_list)
                if  cnt > max_cnt:
                    targets = [[i,j]]
                    max_cnt = cnt
                elif cnt == max_cnt:
                    targets.append([i,j])
    return targets

def getEmptyPosition(availables):
    max_empty = -1
    candidates = []
    for r,c in availables:
        cnt = 0
        for direction in range(4):
            if checkBounadry(r+dr[direction],c+dc[direction]) and board[r+dr[direction]][c+dc[direction]] == 0:
                cnt +=1
        if cnt > max_empty:
            candidates = [r,c]
            max_empty = cnt
    return candidates

for student in f_dict.keys():
    available_positions = getFriendPosition(student)
    pos = getEmptyPosition(available_positions)
    board[pos[0]][pos[1]] = student
    # showMatrix(board)
    # print()

ans = 0

for r in range(N):
    for c in range(N):
        f_count = getNearByFriend(r,c,f_dict[board[r][c]])
        if f_count != 0:
            ans+=10**(f_count-1)

print(ans)
