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
    n = inputter()
    a = list(inputter() for _ in range(n))
    now = 1
    
    for i in range(pow(10,6)):
        if now == 2:
            print(i)
            return
        now = a[now - 1]
    print(-1)


if __name__ == '__main__':
    main()
