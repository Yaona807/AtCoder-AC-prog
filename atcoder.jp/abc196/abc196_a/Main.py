def main():
    import sys

    readline = sys.stdin.readline
    # 入力
    a,b = map(int,readline().rstrip().split())
    c,d = map(int,readline().rstrip().split())
    min_y = min(c,d)
    max_x = max(a,b)
    print(max_x - min_y)

main()
