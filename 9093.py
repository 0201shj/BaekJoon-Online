import sys

for _ in range(int(input())):
    s = sys.stdin.readline().split()
    for i in range(len(s)):
        j = s[i]
        n = str(j[::-1])
        print(n, end=' ')
    print()