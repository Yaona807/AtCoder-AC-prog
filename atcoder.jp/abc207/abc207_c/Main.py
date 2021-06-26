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
    n = readline_int()
    li = [[0,0]] * n
    cnt = 0
    for i in range(n):
        t,l,r = readline_int(True)
        if t == 1:
            li[i] = [l,r]
        elif t == 2:
            li[i] = [l,r-0.1]
        elif t == 3:
            li[i] = [l+0.1,r]
        elif t == 4:
            li[i] = [l+0.1,r-0.1]
    
    for i in range(n-1):
        for j in range(i+1,n):
            if li[i][0] <= li[j][0] <= li[i][1] or li[i][0] <= li[j][1] <= li[i][1] or li[j][0] <= li[i][0] <= li[j][1] or li[j][0] <= li[i][1] <= li[j][1]:
                cnt += 1
    
    print(cnt)
    



if __name__ == '__main__':
    main()
