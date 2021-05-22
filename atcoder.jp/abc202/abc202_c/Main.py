def main():
    import sys

    #入力
    readline = sys.stdin.readline
    N = int(readline().rstrip())
    A_list = list(list(map(int,readline().rstrip().split())))
    B_list = list(list(map(int,readline().rstrip().split())))
    C_list = list(list(map(int,readline().rstrip().split())))
    cnt_list1 = list(0 for _ in range(N+1))
    cnt_list2 = list(0 for _ in range(N+1))
    
    ans = 0
    for i in range(N):
        cnt_list1[A_list[i]] += 1
        cnt_list2[B_list[C_list[i]-1]] += 1

    for i in range(N):
        if cnt_list2[i+1] == 0:
            continue
        ans += cnt_list1[i+1] * cnt_list2[i+1]
    print(ans)



    


main()
