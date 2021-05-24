def main():
    import sys

    #入力
    readline = sys.stdin.readline
    N = int(readline().rstrip())
    A_list = list(list(map(int,readline().rstrip().split())))
    max_num = 0
    ans = 0
    sum_num = 0
    for i in range(N):
        ans -= max_num * i
        max_num = max(max_num,A_list[i])
        sum_num += A_list[i]
        ans += sum_num
        ans += max_num * (i+1)
        print(ans)



main()
