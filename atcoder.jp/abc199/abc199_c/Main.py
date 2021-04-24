def main():
    import sys
    readline = sys.stdin.readline
    # 入力
    N = int(readline().rstrip())
    S = list(readline().rstrip())
    Q = int(readline().rstrip())
    flag = False
    for i in range(Q):
        T,A,B = map(int,readline().rstrip().split())
        if T == 2:
            flag = not(flag)
            continue
        if flag:
            A = A + N  if A <= N else A - N
            B = B + N  if B <= N else B - N
        S[A-1],S[B-1] = S[B-1],S[A-1]
    if flag:
        for i in range(N,2*N):
            print(S[i],end='')
        for i in range(0,N):
            print(S[i],end='')
    else:
        for i in S:
            print(i,end='')
 
main()