def main():
    import sys
    readline = sys.stdin.readline
    a = readline().rstrip()
    count = 0
    flag = 0
    for i in a:
        if count == 1:
            count = 0
        else:
            count = 1
        
        if 'A' <= i and 'Z' >= i and count == 1:
            flag = 1
            break
        if 'a' <= i and 'z' >= i and count == 0:
            flag = 1
            break
    if flag == 0:
        print('Yes')
    else:
        print('No')
main()