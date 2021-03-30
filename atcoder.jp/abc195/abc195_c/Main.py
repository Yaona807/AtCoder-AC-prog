def main():
    import sys
    readline = sys.stdin.readline
    # 入力
    N = int(readline().rstrip())
    check_num = 1000
    cnt = 0

    while True:
        if N - (check_num - 1) <= 0:
            break
        cnt += N - (check_num - 1)
        check_num *= 10**3
    
    print(cnt)

main()