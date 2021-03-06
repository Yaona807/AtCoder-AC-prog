def main():
    import sys

    readline = sys.stdin.readline
    # 入力
    A,B = map(int,readline().rstrip().split())
    if A+B >= 15 and B >= 8:
        print(1)
    elif A+B >= 10 and B >= 3:
        print(2)
    elif A+B >= 3:
        print(3)
    else:
        print(4)
main()
