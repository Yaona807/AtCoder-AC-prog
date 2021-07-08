# -*- coding: utf-8 -*-

'''
文字列取得用関数(str,int併用)
'''
def inputter(is_str=False, split=False):
    import sys
    readline = sys.stdin.readline

    if is_str:
        if split:
            return map(str, readline().rstrip().split())
        else:
            return readline().rstrip()
    else:
        if split:
            return map(int, readline().rstrip().split())
        else:
            return int(readline().rstrip())


'''
二重リストを返す関数
'''
def double_list(input_data):
    return list(list(input_data))


# main関数
def main():
    from collections import defaultdict
    n, m = inputter(0, 1)
    a_dict = defaultdict(int)
    for i in range(m):
        a = inputter()
        a_dict[a] = 1
    mod = 1000000007
    dp = [0] * (n + 1)
    dp[0] = 1
    for i in range(n + 1):
        if a_dict[i]:
            continue
        if i + 2 <= n:
            dp[i + 2] += dp[i] % mod
        if i + 1 <= n:
            dp[i + 1] += dp[i] % mod
    print(dp[n] % mod)


if __name__ == '__main__':
    main()
