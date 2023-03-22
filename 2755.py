import sys

grade = {"A+": 4.3, "A0": 4.0, "A-": 3.7, "B+": 3.3, "B0": 3.0,
     "B-": 2.7, "C+": 2.3, "C0": 2.0, "C-": 1.7, "D+": 1.3,
     "D0": 1.0, "D-": 0.7, "F": 0.0}
avg = cnt = total = 0
n = int(sys.stdin.readline())
for i in range(n):
     a,b,c = sys.stdin.readline().split()
     cnt += int(b)
     total += int(b)*grade[c]
avg = total/cnt
print("%.2f"%(round(avg + 10**-10, 2)))