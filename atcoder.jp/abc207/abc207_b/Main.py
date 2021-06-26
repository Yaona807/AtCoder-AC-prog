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
    a,b,c,d = readline_int(True)
    ans = -1
    cnt = 0
    x = 0
    while True:
        if a <= x * d or cnt >= pow(10,7):
            break
        cnt += 1
        a += b
        x += c
    if cnt >= pow(10,7):
        print(-1)
    else:
        print(cnt)



if __name__ == '__main__':
    main()
