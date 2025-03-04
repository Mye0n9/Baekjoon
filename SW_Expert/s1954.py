import sys

input = sys.stdin.readline

T = int(input())
for test_case in range(1, T + 1):
    print(f"#{test_case}")

    N = int(input())
    mat = [[0 for _ in range(N)] for _ in range(N)]

    def checkBoundary(r,c):
        return True if 0<=r<N and 0<=c<N else False
    
    def fillIn():
        dr = [0,1,0,-1]
        dc = [1,0,-1,0]
        dir = 0
        r,c = 0,0
        mat[r][c] = 1
        for i in range(2,N*N+1):
            # 다음 움직이는 지점이 matrix내에 있고, 업데이트된 지점이 아니라면
            if not(checkBoundary(r+dr[dir],c+dc[dir]) and mat[r+dr[dir]][c+dc[dir]] == 0):
                dir = (dir+1)%4
            
            nr = r+dr[dir]
            nc = c + dc[dir]
            mat[nr][nc] = i
            r,c = nr,nc
    fillIn()
    for i in range(N):
        for j in range(N):
            print(mat[i][j], end=' ')
        print()


        
