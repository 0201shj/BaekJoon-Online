#이번 학기에 들은 과목과 학점 그리고 성적이 주어졌을 때, 평균 평점을 계산하는 프로그램을 작성하시오.
#성적은 A+~F까지 총 13개가 있다.
#A+: 4.3, A0: 4.0, A-: 3.7
#B+: 3.3, B0: 3.0, B-: 2.7
#C+: 2.3, C0: 2.0, C-: 1.7
#D+: 1.3, D0: 1.0, D-: 0.7
#F: 0.0
#평균 평점은 각 과목의 학점*성적을 모두 더한 뒤에, 총 학점으로 나누면 된다.
import sys

grade = {"A+": 4.3, "A0": 4.0, "A-": 3.7, "B+": 3.3, "B0": 3.0,
     "B-": 2.7, "C+": 2.3, "C0": 2.0, "C-": 1.7, "D+": 1.3,
     "D0": 1.0, "D-": 0.7, "F": 0.0}
avg = 0
cnt = 0
total = 0
n = int(sys.stdin.readline())
for k in range(n):
     a,b,c = sys.stdin.readline().split()
     total += int(b)
     cnt += int(b)*grade[c]
avg = cnt/total

def my_round(number, n=1):
     pow_ten = pow(10, n)

     number = number * pow_ten

     if number % 10 > 4:
          number += (10 - number % 10)

     number = number / pow_ten
     return float(str(number)[:n + 2])

print(my_round(avg,3))