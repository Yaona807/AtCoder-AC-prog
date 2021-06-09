'''
文字列取得用関数
split=Trueを引数に渡すことにより、
mapで分割したものを戻り値とする
'''


from math import pi


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
    import math
    a,b,h,m = readline_int(True)

    a_w = 12*60 / 360
    b_w = 60 / 360
    time = h*60 + m
    dig = abs((time/a_w)%360 - (time/b_w)%360)
    if dig > 180:
        dig = 360 - dig

    rad = dig * pi / 180
    ans = math.sqrt(pow(a,2)+pow(b,2) - 2*a*b*math.cos(rad))
    print(ans)



if __name__ == '__main__':
    main()
