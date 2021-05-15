def main():
    import sys

    # 入力
    readline = sys.stdin.readline
    S = list(readline().rstrip())
    ok_list = []
    for i in range(10):
        if S[i] == 'o':
            ok_list.append(1)
        if S[i] == 'x':
            ok_list.append(-1)
        if S[i] == '?':
            ok_list.append(0)
    cnt = 0
    for i in range(10000):
        ok = list(ok_list)
        s_list = list(S)
        flag = 0
        num_str = list('{:04d}'.format(i))
        for j in range(4):
            if s_list[int(num_str[j])] == 'o':
                ok[int(num_str[j])] -= 1
            elif s_list[int(num_str[j])] == 'x':
                flag = 1
                break
            elif s_list[int(num_str[j])] == '?':
                ok[int(num_str[j])] -= 1
        for j in range(10):
            if ok[j] == 1:
                flag = 1
                break
        if flag == 0:
            cnt += 1
    print(cnt)    


main()
