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
    n,m = readline_int(True)
    a = list(list(readline_int(True)))
    sum_a = sum(a)
    ans = 'No'
    cnt = 0
    for i in range(n):
        if sum_a/(4*m) <= a[i]:
            cnt += 1
        if cnt >= m:
            ans = 'Yes'
            break
    print(ans)

if __name__ == '__main__':
    main()
