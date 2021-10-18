n = input()
l_list = list(map(int,input().split()))

l_list.sort(reverse=True)

total = sum(l_list)

if total > 2 * l_list[0]:
  print('Yes')
else:
  print('No')