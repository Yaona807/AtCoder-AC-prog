def main():
    import sys
    readline = sys.stdin.readline
    # 入力
    N,M = map(int, readline().rstrip().split())
    AB_list = list(list(map(int,readline().rstrip().split()))for _ in range(M))
    K = int(readline().rstrip())
    CD_list = list(list(map(int,readline().rstrip().split()))for _ in range(K))
    max_cnt = 0
    for i in range(2 ** K):
        bool_list = list(False for _ in range(N))
        cnt = 0
        for j in range(K):
            if (i >> j) & 1 :
                bool_list[CD_list[j][1]-1] = True
            else:
                bool_list[CD_list[j][0]-1] = True
        for k in range(M):
            if bool_list[AB_list[k][0]-1] == bool_list[AB_list[k][1]-1] == True:
                cnt += 1
        max_cnt = max(max_cnt,cnt)
    print(max_cnt)
main()
