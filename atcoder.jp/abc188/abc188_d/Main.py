def main():
    import sys

    readline = sys.stdin.readline
    # 入力
    N,C = map(int,readline().rstrip().split())
    events = {}
    for _ in range(N):
        a,b,c = map(int,readline().rstrip().split())
        if str(a) in events:
            events[str(a)] += c
        else:
            events[str(a)] = c
        if str(b+1) in events:
            events[str(b+1)] -= c
        else:
            events[str(b+1)] = -c
    ans = 0
    s = 0
    pre = 0
    new_events = sorted(events.items(), key=lambda x:int(x[0]))
    for event in new_events:
        ans += min(C,s) * (int(event[0]) - pre)
        s += int(event[1])
        pre = int(event[0])
    print(ans)
main()
