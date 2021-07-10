# -*- coding: utf-8 -*-

'''
文字列取得用関数(str,int併用)
'''
def inputter(is_str=False,split=False):
    import sys
    readline = sys.stdin.readline
    
    if is_str:
        if split:
            return map(str, readline().rstrip().split())
        else:
            return readline().rstrip()
    else:
        if split:
            return map(int, readline().rstrip().split())
        else:
            return int(readline().rstrip())

'''
二重リストを返す関数
'''
def double_list(input_data):
    return list(list(input_data))


# main関数
def main():
    n,x = inputter(0,1)
    a = double_list(inputter(0,1))
    cnt = 0
    for i in range(n):
        cnt += a[i]
        if (i + 1) % 2 == 0:
            cnt -= 1
    if cnt <= x:
        print('Yes')
    else:
        print('No')

if __name__ == '__main__':
    main()
