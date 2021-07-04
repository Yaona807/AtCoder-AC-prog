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
    p = readline_int()
    max_coin = 0
    k = 1
    coin = []
    while True:
        max_coin += 1
        k *= max_coin
        if k > p:
            break
        coin.append(k)
    cnt = 0

    for i in range(max_coin-2,-1,-1):
        cnt += p // coin[i]
        p %= coin[i]
    print(cnt)





if __name__ == '__main__':
    main()
