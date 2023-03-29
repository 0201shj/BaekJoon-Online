import sys

n = int(sys.stdin.readline())   # 테스트 케이스 개수
for i in range(n):
    score = list(map(int, sys.stdin.readline().split())) #N명의 점수 list로
    avg = 0
    rate = 0
    sub = 0
    count = 0
    for j in range(1, int(score[0]+1)):
        sub += int(score[j])        #점수 총합
        avg = sub/int(score[0])     #평균 점수
    for k in range(1, int(score[0] + 1)):
        if int(score[k]) > avg:     #평균 점수 보다 큰 학생
            count += 1
        rate = count/int(score[0])  #평균 점수 보다 큰 학생 평균
    print("{:.3f}%".format(rate*100))   # 보기 좋게 출력