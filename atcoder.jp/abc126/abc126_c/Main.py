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
    n,k = readline_int(True)
    ans = 0
    for i in range(1,n+1):
        total = 1 / n
        cnt = 0
        while True:
            if i * pow(2,cnt) >= k:
                break
            cnt += 1
        ans += total*pow(1/2,cnt)

    print(ans)


if __name__ == '__main__':
    main()
