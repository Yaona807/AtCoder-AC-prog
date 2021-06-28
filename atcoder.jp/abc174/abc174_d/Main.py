'''
文字列取得用関数
split=Trueを引数に渡すことにより、
mapで分割したものを戻り値とする
'''


def readline_str(split=False):
    import sys
    readline = sys.stdin.readline
    if split:
        return map(str, readline().rstrip().split())
    else:
        return readline().rstrip()


'''
整数取得用関数
split=Trueを引数に渡すことにより、
mapで分割したものを戻り値とする
'''


def readline_int(split=False):
    import sys
    readline = sys.stdin.readline
    if split:
        return map(int, readline().rstrip().split())
    else:
        return int(readline().rstrip())

# main関数


def main():
    n = readline_int()
    c = list(list(readline_str()))

    r_cnt_max = c.count('R')
    r_cnt = 0
    w_cnt = 0
    for i in range(n):
        if w_cnt + r_cnt == r_cnt_max:
            break
        if c[i] == 'W':
            w_cnt += 1
        else:
            r_cnt += 1
    print(w_cnt)


if __name__ == '__main__':
    main()
