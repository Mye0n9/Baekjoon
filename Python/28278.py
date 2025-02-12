import sys

from collections import deque

itr = int(sys.stdin.readline())

Q = deque()

for _ in range(itr):
    cmd = sys.stdin.readline().strip()
    if len(cmd) >1:
        # command with 1 and input
        opt, val = map(int,cmd.split())
        Q.append(val)
    else:
        opt = int(cmd)
        if opt == 2:
            if len(Q)>0: print(Q.pop())
            else: print(-1)
        elif opt == 3:
            print(len(Q))
        elif opt == 4:
            if(len(Q) == 0): print(1)
            else: print(0)
        elif opt == 5:
            if len(Q)>0: print(Q[-1])
            else: print(-1)
