#1
a = "a:b:c:d"
b=a.split(":")
print(b)
c = "#".join(b)
print(c)

#2
a={'A':90,'B':80}
a.get('C',70)

#3
a=[1,2,3]
id(a)
a= a+[4,5]

#4
A=[20, 55, 67, 82, 45, 33, 90, 87,100,25]
result = 0
while A:
    mark = A.pop()
    if mark >= 50:
        result += mark
print(result)

#5
def fib(n):
    if n == 0: return 0
    if n == 1: return 1
    return fib(n-2) + fib(n-1)

for i in range(10):
    print(fib(i))


#6
user = input("숫자를 입력하세요 : ")
numbers = user.split(",")
total = 0
for n in numbers:
    total += int(n)

print(total)

#7
user = input("구구단을 출력할 숫자를 입력하세요(2~9):")
dan = int(user)
for i in range(1,10):
    print(i * dan,end=' ')

#8
#f=open('abc.txt','r')
#lines = f.readlines()
#f.close()

#lines.reverse()

#f=open('abc.txt','w')
#for line in lines:
    #    line = line.strip()
    #f.write(line)
    #f.write('\n')
#f.close()


#10
class Calculator:
    def __init__(self, numberList):
        self.numberList = numberList

    def sum(self):
        result = 0
        for num in self.numberList:
            result += num
        return result
    def avg(self):
        total = self.sum()
        return total / len(self.numberList)

cal1 = Calculator([1,2,3,4,5])
print(cal1.sum())
print(cal1.avg())

cal2 = Calculator([6,7,8,9,10])
print(cal2.sum())
print(cal2.avg())

