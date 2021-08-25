n, m = map(int, input().split())

array = []
for i in range(n):
    array.append(int(input()))

d= [10001] * (m+1)

d[0] = 0
for i in range(n): # i = 화폐 개수
    for j in range(array[i], m+1): # j = 총합
        if d[j-array[i]] != 10001: #(i-k)원을 만드는 방밥이 존재하는 경우
            d[j] = min(d[j],d[j-array[i]]+1)

#계산된 결과 출력
if d[m] == 10001: #최종적으로 M원을 만드는 방법이 없는 경우
    print(-1)
else:
    print(d[m])
