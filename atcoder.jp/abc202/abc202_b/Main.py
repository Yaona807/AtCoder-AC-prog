def main():
    import sys

    #入力
    readline = sys.stdin.readline
    S = list(readline().rstrip())
    S.reverse()
    
    for i in S:
        if i == '6':
            print(9,end='')
        elif i == '9':
            print(6,end='')
        else:
            print(i,end='')

    


main()
