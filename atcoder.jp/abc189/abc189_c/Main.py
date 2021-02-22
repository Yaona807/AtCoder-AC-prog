def main():
    import sys

    readline = sys.stdin.readline

    N = int(readline().rstrip())
    A = list(map(int,readline().rstrip().split()))
    MAX=0
    for l in range(N):
        x = A[l]
        for r in range(l,N):
            x=min(x,A[r])
            MAX=max(MAX,x*(r-l+1))
    print(MAX)
main()