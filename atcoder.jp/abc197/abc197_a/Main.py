def main():
    import sys

    readline = sys.stdin.readline
    # 入力
    S = list(readline().rstrip())
    print(S[1]+S[2]+S[0])

main()