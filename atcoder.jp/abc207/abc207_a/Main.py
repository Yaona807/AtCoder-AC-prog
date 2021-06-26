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
    a = list(list(readline_int(True)))
    a.sort(reverse=True)
    print(a[0]+a[1])

if __name__ == '__main__':
    main()
