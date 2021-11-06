n = int(input())
s = list(map(int,input().split()))
t = int(input())

ans = set()
for i in s:
  ans.add(i//t)
print(len(ans))