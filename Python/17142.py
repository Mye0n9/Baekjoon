from collections import deque
import sys, copy
input = sys.stdin.readline
INF = sys.maxsize

# 연구소의 크기(NxN), 활성화할 바이러스 M개 선택
N, M = map(int, input().split())
space = [list(map(int, input().split())) for _ in range(N)]
answer = INF

# 벽은 '-', 바이러스 위치는 '*'(비활성), 나머지 -1로 space(배열)를 초기화
# 바이러스의 위치가 담긴 큐(후보)를 return하는 함수
def init():
    virus = deque()
    for i in range(N):
        for j in range(N):
            # 벽일 경우
            if space[i][j] == 1:
                space[i][j] = '-'
            # 만약 바이러스가 들어갈 수 있는 자리라면
            elif space[i][j] == 2:
                space[i][j] = '*'	# 아직 선택한 상태가 아니므로 비활성 상태로 표시
                virus.append((i, j))
            else: # 벽도 아니고 바이러스도 아닌 경우
                space[i][j] = -1           
                # 바이러스가 모든 빈칸에 퍼졌나 안퍼졌나 판단하기 위함
    return virus

# 바이러스를 활성화 시킬수 있는 후보 좌표(위치)
candidate = init()


def bfs(sol):
    dydx = [(0, 1), (1, 0), (-1, 0), (0, -1)]
    visited = [[False]*N for _ in range(N)]
    tmp_space = copy.deepcopy(space)
    Q = copy.deepcopy(sol)
    time = 0
     
    # 활성 바이러스는 0으로 표시
    for y,x in Q:
        visited[y][x] = True
        tmp_space[y][x] = 0
        
    while Q:
        y, x = Q.popleft()
        
        for dy,dx in dydx:
            ny = y + dy
            nx = x + dx

            if 0<=ny<N and 0<=nx<N and not visited[ny][nx] and tmp_space[ny][nx] != '-':
            	# 빈칸이라면
                if tmp_space[ny][nx] == -1 :
                    tmp_space[ny][nx] = tmp_space[y][x] + 1
                    time = max(time, tmp_space[ny][nx]) # 시간을 갱신하는 코드
                
                # 비활성화 상태의 바이러스를 만난다면 통과해야하기 때문에 시간은 1초 늘려줘야하지만 갱신은 하지 않는다. (2차원 평면상에서의 한계)
                elif tmp_space[ny][nx] == '*':
                    tmp_space[ny][nx] = tmp_space[y][x] + 1      
                       
                visited[ny][nx] = True
                Q.append((ny, nx))
                
    # -1이 존재한다는 것은 모든 빈 칸에 바이러스를 퍼뜨릴 수 없었다는 의미
    for i in range(N):
        for j in range(N):
            if tmp_space[i][j] == -1:
                time = sys.maxsize
                return time
    return time
            
            
            
# 바이러스를 활성화 시킬 M개를 선택하는 함수 (백트래킹으로 구현)
def select_virus(sol, level):
    global answer
    # 활성화 시킬 M개를 정했다면
    if len(sol) == M:
        answer = min(bfs(sol), answer)		# bfs수행
        return 
    
    for i in range(level, len(candidate)):
        sol.append(candidate[i])
        select_virus(sol, i+1)
        sol.pop()

select_virus(deque(), 0)

if answer == INF:
    print(-1)
else:
    print(answer)