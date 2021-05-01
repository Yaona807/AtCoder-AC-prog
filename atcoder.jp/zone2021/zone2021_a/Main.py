def main():
    import sys
    readline = sys.stdin.readline
    # 入力
    S = list(readline().rstrip())
    cnt = 0
    ans = 'ZONe'
    for i in range(len(S)):
        for j in range(len(ans)):
            if S[i+j] != ans[j]:
                break
            elif j == 3:
                cnt += 1
    
    print(cnt)
main()