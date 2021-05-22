def main():
    import sys

    #入力
    readline = sys.stdin.readline
    a,b,c = map(int,readline().rstrip().split())
    a = 7 - a
    b = 7 - b
    c = 7 - c
    print(a+b+c)


main()
