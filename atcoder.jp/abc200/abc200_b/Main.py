def main():
    import sys
    
    readline = sys.stdin.readline
    # 入力
    N,K = map(int,readline().rstrip().split())

    for i in range(K):
        if N % 200 == 0:
            N //= 200
        else:
            n = int(str(N) + '200')
            N = int(n)
    # 出力
    print(N)


main()
