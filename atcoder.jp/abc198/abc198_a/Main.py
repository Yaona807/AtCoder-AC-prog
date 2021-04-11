def main():
    import sys
    readline = sys.stdin.readline
    # 入力
    N = int(readline().rstrip())
    ans = 0
    if N == 1:
        pass
    elif N == 2:
        ans = 1
    else:
        ans = N - 1
    print(ans)
main()