def main():
    import sys

    readline = sys.stdin.readline
    # 入力
    N = int(readline().rstrip())
    AB_list = list(list(map(int,readline().rstrip().split()))for _ in range(N))
    a_list = []
    b_list = []
    c_list = []
    for i in AB_list:
        a_list.append(i[0])
        b_list.append(i[1])
        ans = 10000000000000000000
    for i in range(len(a_list)):
        for j in range(len(b_list)):
            if i == j:
                ans = min(ans,a_list[i]+b_list[j])
            else:
                ans = min(ans,max(a_list[i],b_list[j]))

    print(ans)
main()
