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
    a,b,x = readline_int(True)

    ok = 0
    ng = pow(10,9) + 1

    while abs(ok-ng) != 1:
        mid = (ok + ng) // 2

        if a*mid + b * len(str(mid)) > x:
            ng = mid
        if a*mid + b * len(str(mid)) <= x:
            ok = mid
    print(ok)



if __name__ == '__main__':
    main()
