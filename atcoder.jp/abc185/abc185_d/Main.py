def main():
    import sys

    readline = sys.stdin.readline

    N,M = map(int,readline().rstrip().split())
    minimum = N
    white_list=[]
    count = 0
    if M == 0:
        print(1)
        sys.exit()
    A = sorted(list(map(int,readline().rstrip().split())))
    if N==M:
        print(0)
        sys.exit()
    if A[0] != 1:
        minimum = min(minimum,A[0]- 1)
        white_list.append(A[0]- 1)
    if A[-1] != N:
        minimum = min(minimum,N - A[-1])
        white_list.append(N - A[-1])
    if M != 1:
        for i in range(0,M-1):
            if A[i+1]-A[i]-1 == 0:
                continue
            minimum = min(minimum,A[i+1]-A[i]-1)
            white_list.append(A[i+1]-A[i]-1)
    for i in white_list:
        if i % minimum == 0:
            count += i // minimum
        else:
            count += i // minimum + 1
    print(count)
main()