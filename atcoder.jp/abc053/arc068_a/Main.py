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
    import math
    x = readline_int()
    amari = x % 11
    cnt = 0
    
    if amari != 0:
        cnt += 1
    if amari > 6 and amari != 0:
        cnt += 1
    print(math.floor(x / 11)*2 + cnt)

if __name__ == '__main__':
    main()
