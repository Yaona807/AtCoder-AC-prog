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
    import math
    a,b = inputter(0,1)
    
    for i in range(1,pow(10,4)):
        if math.floor(i * 0.08) == a and math.floor(i * 0.1) == b:
            print(i)
            return
    print(-1)


if __name__ == '__main__':
    main()
