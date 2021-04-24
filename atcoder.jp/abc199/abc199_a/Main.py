def main():
    import sys
    readline = sys.stdin.readline
    # 入力
    A,B,C = map(int,readline().rstrip().split())
    if A**2 + B**2 < C ** 2:
        print('Yes')
    else:
        print('No')
main()