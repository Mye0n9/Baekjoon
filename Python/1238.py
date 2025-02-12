import sys
import heapq

MAX_VAL = 1e9

N, M ,X = map(int,sys.stdin.readline().strip().split())

graph = [[] for _ in range(N+1)]

for _ in range(M):
    start, end, time = map(int,sys.stdin.readline().strip().split())
    graph[start].append((end, time))

def dijkstra(start, end):
    path = [MAX_VAL for _ in range(N+1)]
    path[start] = 0
    queue = []
    heapq.heappush(queue,(0, start)) # queue에 걸리는 시간과 도착 노드, initialization이니깐 0과 start 넣어주기
    while queue:
        t, node = heapq.heappop(queue)
        if node == end:
            return t
        if t <= path[node]:
            for newNode, newTime in graph[node]:
                if t+newTime < path[newNode]:
                    path[newNode] = t + newTime
                    heapq.heappush(queue,(t+newTime,newNode))

res = 0
for i in range(1, N+1):
    # res = dijkstra(i, X)
    res = max(res, dijkstra(i,X)+dijkstra(X,i))
print(res)
