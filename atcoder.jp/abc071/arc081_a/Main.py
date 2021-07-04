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
    flag = 0
    sorted_a_cnt = sorted(a_cnt.items(),key=lambda x: x[0],reverse=True)
    
    for k,v in sorted_a_cnt:
        if v < 2:
            continue
        if v >= 4 and ans == 0:
            ans = k * k
            flag = 1
            break
        elif ans == 0:
            ans = k
        else:
            ans *= k
            flag = 1
            break

    if flag == 0:
        print(0)
    else:
        print(ans)

if __name__ == '__main__':
    main()
