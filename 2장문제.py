#1번
a=80
b=75
c=55
(a+b+c)/3

#2번
13 % 2 ==1

#3번,4번
pin = "881120-1068234"
yyyymmdd=pin[:6]
num = pin[7:]
print(yyyymmdd)
print(num)

if pin[7]=='1':
    print("남자")
else:
    print("여자")

#5
a="a:b:c:d"
b=a.replace(":","#")
print(b)

#6
a=[1,3,5,4,2]
a.sort()
a.reverse()
print(a)

#7
a=['Life','is','too','short']
result = " ".join(a)
print(result)

#8
a=(1,2,3)
a=a+(4,)
print(a)

#10
a={'A':90,'B':80,'C':70}
result=a.pop('B')
print(a)
print(result)

#11
a=[1,1,1,2,2,3,3,3,4,4,5]
aSet = set(a)
b=list(aSet)
print(b)

