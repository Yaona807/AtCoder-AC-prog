def main():
    import sys

    # 入力
    readline = sys.stdin.readline
    N = int(readline().rstrip())
    max_T = 0
    ans_dict = {}
    for i in range(N):
        S,T = map(str,readline().rstrip().split())
        ans_dict[S] = int(T)
    sorted_ans_dict = sorted(ans_dict.items(), key=lambda x:x[1],reverse=True)
    j = 0
    for i in sorted_ans_dict:
        j += 1
        if j == 2:
            print(i[0])
            break


main()
