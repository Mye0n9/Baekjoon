r,c,k = map(int,input().split())
mat = []

# 배열에 들어간 수는 100보다 작은 값
# 두 개의 리스트로 할까?

max_len = 0
counter = [0] * 100
orderDictionary = {}

for _ in range(3):
    mat.append(list(map(int,input().split())))

def showMatrix(mat):
    for i in range(len(mat)):
        for j in range(len(mat[i])):
            print(mat[i][j], end='')
        print()

def checkBoundary(r,c):
    return True if 0<=r<len(mat) and 0<=c<len(mat[0]) else False

def rOperation(mat):
    global max_len, counter, orderDictionary
    n_mat = []

    for i in range(len(mat)):
        ans = []
        for j in range(len(mat[0])):
            if mat[i][j] > 0:
                counter[mat[i][j]-1] += 1

        for k in range(100):
            if counter[k] != 0:
                if counter[k] not in orderDictionary.keys():
                    orderDictionary[counter[k]] = [k + 1]
                else:
                    orderDictionary[counter[k]].append(k + 1)

        orderDictionary = dict(sorted(orderDictionary.items()))
        for count in orderDictionary.keys():
            for val in orderDictionary[count]:
                ans.append(val)
                ans.append(count)
        n_mat.append(ans)
        max_len = max(max_len,len(ans))

        orderDictionary = {}
        counter = [0] * 100
        ans = []

    for i in range(len(n_mat)):
        while len(n_mat[i]) != max_len:
            n_mat[i].extend([0, 0])

    max_len = 0
    return n_mat

def cOperation(mat):
    global max_len, counter, orderDictionary
    n_mat = []

    for i in range(len(mat[0])):
        ans = []
        for j in range(len(mat)): # 열 별로 추출 진행
            if mat[j][i] > 0:
                counter[mat[j][i]-1] += 1
            # print(mat[j][i],end = '')
        # print()
        # print(counter)
        for k in range(100):
            if counter[k] != 0:
                if counter[k] not in orderDictionary.keys():
                    orderDictionary[counter[k]] = [k+1]
                else:
                    orderDictionary[counter[k]].append(k+1)
        orderDictionary = dict(sorted(orderDictionary.items()))
        for count in orderDictionary.keys():
            for val in orderDictionary[count]:
                ans.append(val)
                ans.append(count)
        n_mat.append(ans)
        max_len = max(max_len, len(ans))
        # print()
        # Refresh
        orderDictionary = {}
        counter = [0]*100
        ans = []

    for i in range(len(n_mat)):
        while len(n_mat[i]) != max_len:
            n_mat[i].extend([0,0])

    f_mat = [[0 for _ in range(len(n_mat))] for _ in range(len(n_mat[0]))]
    for i in range(len(n_mat)):
        for j in range(len(n_mat[0])):
            f_mat[j][i] = n_mat[i][j]

    return f_mat

itr = 0
while itr <=100:

    if checkBoundary(r-1,c-1) and mat[r-1][c-1] == k:
        break

    itr+=1
    if len(mat) >= len(mat[0]):
        mat = rOperation(mat)
    else:
        mat = cOperation(mat)

if itr > 100:
    print(-1)
else:print(itr)