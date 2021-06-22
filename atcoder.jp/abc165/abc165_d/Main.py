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
    a,b,n = readline_int(True)

    ok = 0
    ng = n + 1
    max_result = 0
    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        calc_result = (a * mid) // b - a * (mid // b)
        if calc_result >= max_result:
            ok = mid
            max_result = calc_result
        else:
            ng = mid
    print(max_result)



if __name__ == '__main__':
    main()
