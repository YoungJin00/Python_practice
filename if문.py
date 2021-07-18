#money = True
#if money:
#    print("택시를 타고 가라")
#else:
#    print("걸어가라")
money = 2000
if money >= 3000:
     print("택시타고가라")
else:
      print("걸어가라")

money = 2000
card = True
if money >= 3000 or card:
     print("택시타고가라")
else:
      print("걸어가라")

1 in [1,2,3]
1 not in [1,2,3]

pocket= ['paper','handphone']
card =True
if 'money' in pocket:
    print("택시를 타고가라")
else:
    if card:
        print("택시를 타고가라")
    else:
        print("걸어 가라")

pocket= ['paper','cellphone']
card = True
if 'money' in pocket:
    print("택시를 타고가라1")
elif card:
    print("택시를 타고가라1")
else:
    print("걸어가라")

if score >= 60:
    message="sucess"
else:
    message="failure"

message = "success" if score >=60 else "failure"




