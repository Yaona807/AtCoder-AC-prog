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
    from collections import defaultdict

    n = readline_int()
    
    cnt = defaultdict(int)
    for _ in range(n):
        s = list(readline_str())
        s.sort()
        cnt[(''.join(s))] += 1
    total = 0

    for v in cnt.values():
        if v <= 1:
            continue
        total += v * (v - 1) // 2
    print(total)








if __name__ == '__main__':
    main()
