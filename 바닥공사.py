#바닥공사

#정수 N을 입력받기
n = int(input())

#앞서 계산된 결과를 저장하기 위한 DP테이블 초기화
d = [0] * 1001

d[1] = 1
d[2] = 3

for i in range(3,n+1):
    d[i] = (d[i-1] + d[i-2] *2) % 796796

print(d[n])

