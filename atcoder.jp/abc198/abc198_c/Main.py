def main():
    import sys
    import math
    readline = sys.stdin.readline
    R, X, Y = map(int, readline().rstrip().split())
    
    r = math.sqrt(X**2+Y**2)
    
    if r == R:
        print(1)
    elif r <= 2*R:
        print(2)
    else:
        print(math.ceil(r / R))

main()
