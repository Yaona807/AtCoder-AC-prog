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
    
    cnt = collections.Counter(a)
    
    total = 0
    for _, v in cnt.items():
        total += (v * (v - 1)) // 2

    for i in range(n):
        ans = total - (cnt[a[i]] * (cnt[a[i]] - 1)) // 2
        
        if cnt[a[i]] - 1 >= 2:
            ans += ((cnt[a[i]] - 1) * (cnt[a[i]] - 2)) // 2
        
        if ans <= 0:
            ans = 0
        
        print(ans)


if __name__ == '__main__':
    main()
