def main():
    import sys
    readline = sys.stdin.readline
    a = int(readline().rstrip())
    b = a % 100
    ans = 100 - b
    print(ans)
main()