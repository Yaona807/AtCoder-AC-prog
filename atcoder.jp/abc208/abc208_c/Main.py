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
    n,k = readline_int(True)
    a = list(list(readline_int(True)))
    all_num = k // n
    k = k % n
    human = defaultdict(int)

    for i in sorted(a):
        if k > 0:
            human[i] = all_num + 1
            k -= 1
        else:
            human[i] = all_num
    
    for i in a:
        print(human[i])


if __name__ == '__main__':
    main()
