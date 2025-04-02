N, M = map(int,input().split())

def backtracking(cnt,n_list,num):
    if cnt == M:
        for val in n_list:
            print(val,end=' ')
        print()
        return

    for i in range(num,N+1):
        n_list.append(i)
        backtracking(cnt+1,n_list,i+1)
        n_list.pop()

backtracking(0,[],1)