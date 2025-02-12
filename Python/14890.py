import sys

input = sys.stdin.readline

N,L = map(int, input().split())
mat = []
for _ in range(N):
    mat.append(list(map(int,input().split())))

def checkRoad(road):
    slope_check = [0]*N
    idx = 0

    while idx < N - 1: # L까지만 설정하면 indexError 생길 가능성 있음. 전체 순회 하는게 차라리 좋음
        if abs(road[idx] - road[idx+1]) > 1: # gap too high
            return 0
        
        if road[idx] - road[idx+1] == -1: # increasing
            # check whether it is possible to set the slope with length L and if there is no slop already been set
            for j in range(L):
                if(idx-j<0): return 0
                if(road[idx] != road[idx-j]): return 0
                if(slope_check[idx-j] != 0): return 0
                if(slope_check[idx-j] == 0): slope_check[idx-j] = 1
                
        elif road[idx] - road[idx+1] == 1: # decreasing
            # check whether it is possible to set the slope with length L and if there is no slop already been set
            for j in range(L):
                if(idx+j+1>=N): return 0
                if(road[idx+1] != road[idx+j+1]): return 0
                if(slope_check[idx+j+1] == 1): return 0
                if(slope_check[idx+j+1] == 0): slope_check[idx+j+1] = 1
        idx+=1

    return 1


cnt = 0
for i in range(N):
    # check the row
    cnt+= checkRoad(mat[i])
    # check the column
    cnt+= checkRoad([mat[j][i] for j in range(N)])
    
print(cnt)
