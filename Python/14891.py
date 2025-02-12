import sys
from collections import deque
input = sys.stdin.readline

Q = []

for _ in range(4):
    Q += list(input().strip())

def replace(target, dir):
    nQ = deque(Q[target*8:(target+1)*8])
    if dir == 1:
        tmp = nQ.pop()
        nQ.appendleft(tmp)
    else: # dir == -1
        tmp = nQ.popleft()
        nQ.append(tmp)
    return list(nQ)
        
def rotate(idx, dir):
    # idx는 0, 8, 16, 24
    command = [[idx//8, dir]]
    left_idx = idx
    right_idx = idx

    left_dir = dir
    right_dir = dir

    l_stop = False
    r_stop = False

    # left section
    while left_idx > 7 and not(l_stop): # Q1 이후
        if Q[left_idx+6] != Q[left_idx-8+2]:
            left_dir *= (-1)
            left_idx -= 8
            command.append([left_idx//8, left_dir])
        else: l_stop = True
    # right section
    while right_idx < 23 and not(r_stop): # Q3 이전
        if Q[right_idx+2] != Q[right_idx+8+6]:
            right_dir *= (-1)
            right_idx += 8
            command.append([right_idx//8, right_dir])
        else: r_stop = True
    return command

itr = int(input())

for _ in range(itr):
    target , dir = map(int,input().split())
    cmd = rotate((target-1)*8, dir)
    for t,d in cmd:
        rotated = replace(t,d)
        for i in range(len(rotated)):
            Q[t*8+i] = rotated[i]

print(int(Q[0])+int(Q[8])*2+int(Q[16])*4+int(Q[24])*8)
