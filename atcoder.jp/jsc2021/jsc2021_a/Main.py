def main():
    import sys
    readline = sys.stdin.readline
    # 入力
    X,Y,Z = map(int,readline().rstrip().split())
    
    a = Y / X
    ans = 1
    while True:
        if (ans / Z) >= a:
            ans -= 1
            break
        ans += 1
    print(ans)
main()