def main():
    import sys

    # 入力
    readline = sys.stdin.readline
    V,T,S,D = map(int,readline().rstrip().split())
    time = D / V
    if T <= time and time <= S:
        ans = 'No'
    else:
        ans = 'Yes'
    print(ans)
    
main()
