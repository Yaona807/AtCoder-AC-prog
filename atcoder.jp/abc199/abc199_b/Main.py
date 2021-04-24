def main():
    import sys
    readline = sys.stdin.readline
    # 入力
    N = int(readline().rstrip())
    A_list = list(list(map(int,readline().rstrip().split())))
    B_list = list(list(map(int,readline().rstrip().split())))
    ans = min(B_list) - max(A_list) + 1
    if ans > 0:
        print(ans)
    else:
        print(0)
main()