import sys
import heapq

input = sys.stdin.readline

N, M, fuel = map(int, input().split())

mat = [list(map(int, input().split())) for _ in range(N)]

r, c = map(int, input().split())
taxi = (r-1, c-1)

passengers = []
destinations = {}

dr = [1, -1, 0, 0]
dc = [0, 0, 1, -1]

for _ in range(M):
    r1, c1, r2, c2 = map(int, input().split())
    passengers.append((r1-1, c1-1))
    destinations[(r1-1, c1-1)] = (r2-1, c2-1)

def is_valid(nr, nc):
    return 0 <= nr < N and 0 <= nc < N and mat[nr][nc] == 0

def bfs(start):
    """ 출발 지점에서 모든 승객까지의 최단 거리 탐색 (heapq 사용) """
    pq = [(0, start[0], start[1])]  # (거리, row, col)
    dist_map = [[-1] * N for _ in range(N)]
    dist_map[start[0]][start[1]] = 0

    while pq:
        d, r, c = heapq.heappop(pq)
        for i in range(4):
            nr, nc = r + dr[i], c + dc[i]
            if is_valid(nr, nc) and dist_map[nr][nc] == -1:
                dist_map[nr][nc] = d + 1
                heapq.heappush(pq, (d + 1, nr, nc))

    return dist_map

def find_closest_passenger():
    """ 가장 가까운 승객을 찾는 함수 """
    global taxi, fuel

    dist_map = bfs(taxi)
    min_dist = float('inf')
    target = None

    for passenger in passengers:
        r, c = passenger
        if dist_map[r][c] != -1 and dist_map[r][c] < min_dist:
            min_dist = dist_map[r][c]
            target = passenger
        elif dist_map[r][c] == min_dist:
            if passenger < target:  # 행이 작은 승객 우선, 같다면 열이 작은 승객 우선
                target = passenger

    if target is None or min_dist > fuel:
        return False, None

    fuel -= min_dist
    taxi = target
    return True, target

def move_to_destination(passenger):
    """ 승객을 목적지로 이동 """
    global taxi, fuel

    dest = destinations[passenger]
    dist_map = bfs(passenger)
    dest_dist = dist_map[dest[0]][dest[1]]

    if dest_dist == -1 or dest_dist > fuel:
        return False

    fuel += dest_dist  # 도착하면 연료 2배 충전
    taxi = dest
    passengers.remove(passenger)
    del destinations[passenger]
    return True

while passengers:
    success, passenger = find_closest_passenger()
    if not success or not move_to_destination(passenger):
        print(-1)
        exit()

print(fuel)
