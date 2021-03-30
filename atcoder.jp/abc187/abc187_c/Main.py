def main():
    import sys
    readline = sys.stdin.readline
    # 入力
    N = int(readline().rstrip())
    S = set(readline().rstrip() for _ in range(N))
    ans = 'satisfiable'

    for i in S:
        if '!'+i in S:
            ans = i
            break
    
    print(ans)
    
    
main()