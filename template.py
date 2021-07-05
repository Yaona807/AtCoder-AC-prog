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
    print(n)

if __name__ == '__main__':
    main()
