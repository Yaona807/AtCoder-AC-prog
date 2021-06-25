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
    s = readline_str()
    ans = 'Good'
    for i in range(len(s)-1):
        ren = 0
        now = s[i]
        for j in range(i+1,i+2):
            if now == s[j]:
                ans = 'Bad'

    print(ans)

if __name__ == '__main__':
    main()
