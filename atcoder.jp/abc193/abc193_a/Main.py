def main():
    import sys

    readline = sys.stdin.readline

    a,b = map(int,readline().rstrip().split())
    c = (1 - (b / a)) * 100
    print(c)
main()
