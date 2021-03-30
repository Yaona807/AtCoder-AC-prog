def main():
    import sys
    readline = sys.stdin.readline
    # 入力
    L = int(readline().rstrip())
    ans = 1
    for i in range(1,12):
        ans *= (L - i)
    for j in range(11,0,-1):
        ans //= j
    
    print(ans)
main()