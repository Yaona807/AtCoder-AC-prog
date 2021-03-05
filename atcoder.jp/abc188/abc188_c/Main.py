def main():
    import sys

    readline = sys.stdin.readline
    # 入力
    N = int(readline().rstrip())
    A = list(list(map(int,readline().rstrip().split())))
    len_half_A = len(A)//2
    x = max(A[0:len_half_A])
    y = max(A[len_half_A:])
    ans = A.index(x)+1 if x < y else A.index(y)+1
    print(ans)
main()
