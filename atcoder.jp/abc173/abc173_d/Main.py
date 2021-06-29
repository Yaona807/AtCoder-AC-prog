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
    a = list(list(readline_int(True))) 
    a.sort(reverse=True)
    ans = 0
    index = 0
    for i in range(n-1):
        if i % 2 != 0:
            index += 1
        ans += a[index]
    print(ans)


if __name__ == '__main__':
    main()
