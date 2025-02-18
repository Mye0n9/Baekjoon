import sys
from collections import deque, defaultdict

input = sys.stdin.readline
N, M, K = map(int, input().split())

# 양분 배열
mat = [[5] * N for _ in range(N)]
nutrition = [list(map(int, input().split())) for _ in range(N)]

# 좌표별 나무를 관리하는 defaultdict(deque)
tree_map = defaultdict(deque)

# 초기 나무 정보 입력
for _ in range(M):
    x, y, z = map(int, input().split())
    tree_map[(x - 1, y - 1)].append(z)

# 8방향 이동 (가을 번식용)
adjacent = [(-1, -1), (-1, 0), (-1, 1), (0, -1), (0, 1), (1, -1), (1, 0), (1, 1)]

def spring_summer():
    """봄 - 나이순으로 정렬된 deque에서 나무가 자라고, 양분 부족하면 죽음"""
    dead_trees = []
    
    for (x, y) in list(tree_map.keys()):
        temp_trees = deque()
        for _ in range(len(tree_map[(x, y)])):
            age = tree_map[(x, y)].popleft()
            if mat[x][y] >= age:
                mat[x][y] -= age
                temp_trees.append(age + 1)
            else:
                dead_trees.append((x, y, age))  # 여름에 사용할 죽은 나무 저장
        tree_map[(x, y)] = temp_trees

    # 여름: 죽은 나무들의 나이 / 2 만큼 양분으로 변환
    for x, y, age in dead_trees:
        mat[x][y] += age // 2

def fall():
    """가을 - 나이가 5의 배수인 나무는 번식"""
    new_trees = []

    for (x, y) in list(tree_map.keys()):
        for age in tree_map[(x, y)]:
            if age % 5 == 0:
                for dx, dy in adjacent:
                    nx, ny = x + dx, y + dy
                    if 0 <= nx < N and 0 <= ny < N:
                        new_trees.append((nx, ny))

    # 번식된 나무들을 추가 (가을에 동시에 처리)
    for nx, ny in new_trees:
        tree_map[(nx, ny)].appendleft(1)  # 어린 나무는 앞쪽에 추가

def winter():
    """겨울 - 영양분 추가"""
    for i in range(N):
        for j in range(N):
            mat[i][j] += nutrition[i][j]

# K년 동안 시뮬레이션
for _ in range(K):
    spring_summer()
    fall()
    winter()

# 남아 있는 나무 개수 출력
result = sum(len(tree_map[key]) for key in tree_map)
print(result)
