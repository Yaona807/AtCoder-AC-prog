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
    c = list(list(readline_int(True))for _ in range(3))
    max_c = 0
    for i in c:
        max_c = max(max_c,max(i))
    
    index = [[0,1,2],[1,2,0],[2,0,1]]
    ans = 'No'
    for a1 in range(max_c + 1):
        for a2 in range(max_c + 1):
            for a3 in range(max_c + 1):
                for i in range(3):
                    if [_ - a1 for _ in c[index[i][0]]] == [_ - a2 for _ in c[index[i][1]]] == [_ - a3 for _ in c[index[i][2]]]:
                        ans = 'Yes'
    print(ans)


if __name__ == '__main__':
    main()
