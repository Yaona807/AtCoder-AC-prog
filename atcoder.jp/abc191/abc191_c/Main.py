def main():
    import sys
    readline = sys.stdin.readline
    # 入力
    H,W = map(int, readline().rstrip().split())
    S_list = list(list(map(str,readline().rstrip()))for _ in range(H))
    ans = 0
    for i in range(H-1):
        for j in range(W-1):
            cnt = 0
            for k in range(2):
                for l in range(2):
                    if S_list[i+k][j+l] == '#':
                        cnt += 1
            if cnt == 1 or cnt == 3:
                ans += 1
    print(ans)

main()
