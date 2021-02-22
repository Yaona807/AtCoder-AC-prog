import sys

readline = sys.stdin.readline

N, X = map(int, readline().rstrip().split())
X *= 100
count = 0
flag = 0
for i in range(N):
    V, P = map(int, readline().rstrip().split())
    count += V*P
    if count > X:
        flag = 1
        print(i+1)
        break
if flag == 0:
    print(-1)
