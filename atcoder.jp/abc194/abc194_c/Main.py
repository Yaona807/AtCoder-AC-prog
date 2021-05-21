def main():
    import sys
    readline = sys.stdin.readline
    # 入力
    N = int(readline().rstrip())
    A_list = list(list(map(int,readline().rstrip().split())))
    cnt_list = list(0 for _ in range(401))
    
    for i in range(N):
        cnt_list[A_list[i] + 200] += 1

    ans = 0
    for i in range(401):
        for j in range(i,401):
            ans += cnt_list[i] * cnt_list[j] * abs(i - j)**2
    print(ans)
main()
