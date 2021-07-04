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
    import collections
    n = readline_int()
    a = list(list(readline_int(True)))
    a_cnt = collections.Counter(a)
    ans = 0
    cnt = 0
    for i in range(pow(10,5)+1):
        if a_cnt[i]:
            cnt += a_cnt[i]
        ans = max(ans,(cnt + a_cnt[i + 1]))
        cnt -= a_cnt[i - 1]
    print(ans)

if __name__ == '__main__':
    main()
