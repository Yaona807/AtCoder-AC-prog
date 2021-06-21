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
    s = list(readline_str())
    if len(s) == 1:
        if int(s[0]) % 8 == 0:
            print('Yes')
            exit()
    elif len(s) == 2:
        if (int(s[0])*10 + int(s[1])) % 8 == 0 or (int(s[1])*10 + int(s[0])) % 8 == 0:
            print('Yes')
            exit()
    cnt = collections.Counter(s)
    for i in range(1000):
        if i % 8 != 0:
            continue
        num = list('{:03d}'.format(i))
        cnt2 = collections.Counter(num)
        if cnt[num[0]] >= cnt2[num[0]] and cnt[num[1]] >= cnt2[num[1]] and cnt[num[2]] >= cnt2[num[2]]:
            print('Yes')
            exit()
    print('No')







if __name__ == '__main__':
    main()
