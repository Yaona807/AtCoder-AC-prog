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
    a = 1
    while True:
        b = 1 
        while True:
            c = pow(3,a) + pow(5,b)
            if c == n:
                print(a,b)
                return
            if c > n:
                break
            b += 1
        if b == 1:
            break
        a += 1
    print(-1)

if __name__ == '__main__':
    main()
