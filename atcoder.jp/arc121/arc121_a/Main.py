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


'''
整数取得用関数(多次元配列)
Nに数値を渡すことにより、
N次元配列の値を取得可能
'''
def readline_list_int(N=1):
    if N == 1:
        return list(list(readline_int(True)))
    else:
        return list(list(readline_int(True))for _ in range(N))


'''
文字列取得用関数(多次元配列)
Nに数値を渡すことにより、
N次元配列の値を取得可能
また、split=Trueにより、
文字列を分割した状態で格納可能
'''
def readline_list_str(N=1, split=False):
    if split:
        return list(list(readline_str(True)) for _ in range(N))

    else:
        return list(list(readline_str()) for _ in range(N))


# main関数
def main():
    N = readline_int()
    xy_list = readline_list_int(N)
    xyz_list = []
    for i in range(N):
        xyz_list.append([xy_list[i][0],xy_list[i][1],i])
    ans_list = []
    x_soreted = sorted(xyz_list, key=lambda x:x[0])
    y_soreted = sorted(xyz_list, key=lambda x:x[1])

    check_list = []
    if not(x_soreted[-1] in check_list):
        check_list.append(x_soreted[-1])
    if not(x_soreted[-2] in check_list):
        check_list.append(x_soreted[-2])
    if not(x_soreted[0] in check_list):
        check_list.append(x_soreted[0])
    if not(x_soreted[1] in check_list):
        check_list.append(x_soreted[1])
    if not(y_soreted[-1] in check_list):
        check_list.append(y_soreted[-1])
    if not(y_soreted[-2] in check_list):
        check_list.append(y_soreted[-2])
    if not(y_soreted[0] in check_list):
        check_list.append(y_soreted[0])
    if not(y_soreted[1] in check_list):
        check_list.append(y_soreted[1])
    for i in range(len(check_list)):
        for j in range(0,i):
            ans_list.append(max(abs(check_list[i][0]-check_list[j][0]),abs(check_list[i][1]-check_list[j][1])))
    ans_list.sort(reverse=True)
    print(ans_list[1])


if __name__ == '__main__':
    main()

