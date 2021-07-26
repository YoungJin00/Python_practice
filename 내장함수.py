#절댓값
abs(3)
abs(-3)

#반복 가능한 자료형 x를 입력 인수로 받으며 모두 참이면 True, 거짓있으면 False
all([1,2,3])
all([1,2,3,0])
all([])

#chr 유니코드 값을 입력받아 그 코드에 해당하는 문자를 출력하는 함수
chr(97)
chr(44032)
#ord 문자의 유니코드 값
ord('a')
ord('가')

#dir : 객체가 자체적으로 가지고 있는 변수나 함수를 보여준다.
dir([1,2,3])
dir({'1':'a'})

#divmod(a,b) 2개 입력 받아 a/b 몫과 나머지를 튜플형태로
divmod(7,3)

#enumerate 열거하
for i, name in enumerate(['body','foo','bar']):
    print(i,name)

#eval 실행 가능한 문자열을 입력으로 받아 결괏값을 돌려줌
eval('1+2')
eval("'hi' + 'a'")

#filter 걸러냄

def positive(l):
    result = []
    for i in l:
        if i > 0:
            result.append(i)
    return  result
print(positive([1,-3,2,0,-5,6]))

#hex 16진수로 변환
#oct 8진수로 변환

#id 객체를 입력받아 객체의 고유 주소 값을 돌려줌

#input 사용자 입력 받는 함수

#int 문자열 형태의 숫자나 소수점있는 숫자를 정수로

#isinstance isinstance(object,class) 첫참이면 트루 거짓이면 false

#len

#map(f,iterable) 함수(f)와 반복 가능한(iterable)자료형을 입력
def two_times(numberList):
    result = [ ]
    for number in numberList:
        result.append(number *2)
    return result
result = two_times([1,2,3,4])
print(result)

def two_times(x):
    return x*2
list(map(two_times,[1,2,3,4]))

#max, min

#open(filename,[mode])
#w 쓰기 모드
#r 읽기 모드
#a 추가모드로
#b 바이너리 모드


#pow(x,y) x의 y 제곱한 결괏값

#range 범위 지정

#round 반올림

#sorted 입력값을 정렬한후 리스트로 돌려줌
#str 문자열을 객체를 변환하여 돌려줌

#sum은 입력받은 튜플이나 리스트 값

#tuple

#type 입력값의 자료형이 무엇인지








