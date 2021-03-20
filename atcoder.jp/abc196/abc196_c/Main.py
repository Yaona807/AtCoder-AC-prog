def main():
    import sys
 
    readline = sys.stdin.readline
    # 入力
    X = list(readline().rstrip())
    string = ''
    num = ''
    count = 0
    if len(X) % 2 == 0:
        x = len(X) // 2
    else:
        x = len(X) // 2 + 1
    for i in range(x):
        num = num + X[i]
    for i in X:
        string = string + i
    if len(X) == 1:
        print(0)
        sys.exit()
    
    ans = int(num)

    if int(num+num) <= int(string):
        while True:
            if int(num+num) <= int(string):
                count += 1
                num = str(int(num)+1)
            else:
                count -= 1
                break

    else:
        while True:
            if int(num+num) > int(string):
                count -= 1
                num = str(int(num)-1)
            else:
                break
    print(ans + count)

main()