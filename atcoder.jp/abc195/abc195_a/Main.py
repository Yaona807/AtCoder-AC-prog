def main():
    import sys

    readline = sys.stdin.readline
    # 入力
    M,H = map(int,readline().rstrip().split())
    print('Yes' if H % M == 0 else 'No')
main()
