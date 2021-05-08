def comb(n, r):
    import math
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

def main():
    import sys
    
    readline = sys.stdin.readline
    # 入力
    N = int(readline().rstrip())
    A_list = list(list(map(int,readline().rstrip().split())))
    cnt = 0
    ans = 0
    for i in range(len(A_list)):
        A_list[i] %= 200
    A_list.sort()
    set_num = set()
    for i in range(N):
        if A_list[i] in set_num:
            continue
        cnt = A_list.count(A_list[i])
        if cnt >= 2:
            ans += comb(cnt,2)
        set_num.add(A_list[i])
    # 出力
    print(ans)


main()
