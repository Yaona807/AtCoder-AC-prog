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
    index_a = 0
    index_z = 0

    # 先頭のAを発見
    for i in range(len(s)):
        if s[i] == 'A':
            index_a = i
            break
    # 末尾のZを発見
    for i in range(len(s)-1,0,-1):
        if s[i] == 'Z':
            index_z = i
            break

    ans = index_z - index_a + 1
    print(ans)

if __name__ == '__main__':
    main()
