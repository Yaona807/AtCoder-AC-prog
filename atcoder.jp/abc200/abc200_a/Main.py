def main():
    import sys
    
    readline = sys.stdin.readline
    # 入力
    N = int(readline().rstrip())
    cnt = 1
    while True:
        N -= 100
        if N <= 0:
            break
        else:
            cnt += 1
    # 出力
    print(cnt)


main()
