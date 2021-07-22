#1
def is_odd(number):
    if number % 2 == 1:
        return True
    else:
        return False

print(is_odd(3))
print(is_odd(4))

#2
def avg_numbers(*args):
    result = 0
    for i in args:
        result += i
    return result / len(args)

print(avg_numbers(1,2))
print(avg_numbers(1,2,3,4,5))

#3
first = int(input("첫번째 숫자를 입력하세요: "))
second = int(input("두번째 숫자를 입력하세요: "))

total = first + second
print("두수의 합은 %d 입니다" %total)

#4 출력결과 다른것 3
print("you" "need" "python")
print("you"+"need"+"python")
print("you", "need", "python")
print("".join(["you", "need", "python"]))

#특별문제
name = input("이름 : ")
height = int(input("키 : "))
weight = int(input("몸무게 : "))

sta = (height - 100) *0.9
print(sta)
rate = weight / sta * 100

print("%s님의 비만도는 %d %%입니다" %(name, rate))
