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
    n,l = readline_int(True)
    taste_list = []
    for i in range(n):
        taste_list.append(i+l)
    
    total = sum(taste_list)
    ans = [1010101010110101,1010101010110101]
    for i in range(len(taste_list)):
        num = total - taste_list[i]
        if ans[0] > abs(total-num):
            ans[0] = abs(total-num)
            ans[1] = num
    print(ans[1])
            

if __name__ == '__main__':
    main()
