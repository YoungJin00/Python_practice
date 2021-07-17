
"Hello World"
'Python is fun'
"""Life is short, You need python"""
'''Life is short, You need python'''

food = "Python's favorite food is perl"
food

##food = 'Python's favorite food is perl
say = '"Python is very easy." he says.'
say
food = 'Python\'s favorite is perl'
food
say = "\"Python is very easy.\" he says."
say

multiline = "Life is too short\nYou need python"
multiline

multiline1 ="""
Life is too short
You need python
"""
print(multiline1)

head = "python"
tail = " is fun!"
head + tail

a= "python"
a *2

print("="*50)
print("My Promdgram")
print("="*50)

a = "Life is too short"
len(a)

a = "Life is too short, You need python"
a[3]
a[7]
a[12]
a[-1]
a[-0]
b=a[0]+a[1]+a[2]+a[3]+a[4]
b
a[0:4]
a[0:2]
a[5:7]
a[12:17]
a[19:]
a[:17]
a[:]
a[19:-7]


number = 3
"I eat %d apples." % number
number = 10
day = "three"
"I ate %d apples. so I was sick for %s days." % (number, day)

"I have %s apples" %3

"Error is %d%%." %98
"%10s" % "hi"
"%-10sjane." %"hi"

"%10.4f" % 3.42134234

"I eat {0} apples.".format("five")

number =3
"I eat {0} apples".format(number)

number = 10
day = "three"
"I ate {0} apples. so I was sick for {1} days.".format(number, day)

"{0:<10}".format("hi")
"{0:>10}".format("hi")

"{0:=^10}".format("hi")
"{0:!<10}".format("hi")

y=3.145321234
"{0:0.4f}".format(y)
"{0:10.4f}".format(y)

"{{and}}".format()

name='홍길동'
age = 30
f'나의 이름은 {name}입니다. 나이는 {age}입니다.'
f'나는 내년이면 {age+1}살이 된다'

d={'name' :'홍길동','age':30}
f'나의 이름은 {d["name"]}입니다. 나이는 {d["age"]}입니다.'

a="hobby"
a.count('b')

a="Python is the best choice"
a.find('b')
a.find('k')

a="Life is too short"
a.index('t')
a.index('k')

",".join('abcd')
",".join(['a','b','c','d'])

a="hi"
a.upper()

a="HI"
a.lower()

a=" hi "
a.lstrip()
a.rstrip()
a.strip()

a= "Life is too short"
a.replace("Life","Your leg")

a.split()

b="a:b:c:d"
b.split(':')