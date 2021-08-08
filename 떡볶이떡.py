#떡의 개수(n) 요청한 떡의 길이(m)입력받기
n, m = list(map(int, input().split(' ')))

#각 떡의 개별 높이 정보를 입력 받기
array = list(map(int, input().split()))

#이진탐색 시작점과 끝점 설정
st = 0
end = max(array)

#이진탐색수행
result = 0
while(st <= end):
    total = 0
    mid = (st + end) // 2
    for x in array:
        #잘랏을 때의 떡의 양 계싼
        if x > mid:
            total += x-mid
        #떡의 양이 부족한 경우 더 많이 자르기
    if total < m:
        end = mid - 1
    else:
        result = mid #최대한 덜 잘랐을 떄가 정답이므로 result에 기록
        st = mid + 1

print(result)