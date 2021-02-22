import sys

readline = sys.stdin.readline

C=readline().rstrip()
ans =  'Won' if C[0]==C[1] and C[1] == C[2] else 'Lost'
print(ans)