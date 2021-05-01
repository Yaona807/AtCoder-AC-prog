def main():
    import sys
    readline = sys.stdin.readline
    # 入力
    N,D,H = map(int,readline().rstrip().split())
    max_d = 0
    max_h = 0
    ans = 0.0
    for i in range(N):
        d,h = map(int,readline().rstrip().split())
        m = (H - h)/(D - d)
        b = h - m * d
        if b <= 0:
            b = 0.0
        ans = max(ans,b)
    print(ans)

main()