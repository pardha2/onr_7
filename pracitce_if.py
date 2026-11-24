'''current_bill=("APSPDCL ")
a=("ELECTRICITY BILL")


x=current_bill.center(50,"_")
y=a.center(50,"-")


print(x)
print(y)


print("---------------")


name=str(input("enter your name:"))
units=int(input("enter units:"))
if units>=1 and units<=100:
    print("perunit 5rs")
    price=5
elif units>= 101 and units<=200:
    print ("perunits 6rs")
    price=6
elif units>= 201 and units<=500:
   print("perunits 10rs")
   price=10
else:
  print("invalid")
  price=0
if units>1 and units<500:
    total=units*price
    print("final price:",total)
'''
#rapido,uber:
#km?
##1-6 per km 5rs
##7-12 per km 6 rs
##13-20 per km 8 rs
##21-30 per km 10 rs
##greater than 30 -->ride not possible

##testcase:
##case1: 10 km
##amount: 30+24=54

##case2: 15km
##amount: 30+36+24 = 90

'''
km=float(input("enter kms:"))
if km>=1 and km<=6:
    amount=km*5

elif km>6 and km<=12:
    amount=30+(km-6)*6

elif km>12 and km<=20:
    amount=30+36+(km-12)*8

print(amount)
'''

#toy: which type,price
#battery base: more than or equal --->500+wire toy free and 5%
#wire base:300 or more than 300 -->50rs reduce, 600-->50 rs
#wireless:2k purchase, 20 %discount, 2.more than 5k 30%
##
##battery:500
##500-475+wiretoy  ---> 25rs
##
##wir 900-150=750
##
##wirless --> 5k-3500

#-------------------------find where is the student-------------------------->
##1.college   no
##2.blocks    no
##3.floors    no
##4.classes   no
'''
college = input(" student in college: ")

if college == "yes":
    block = input(" student in blocks:")
    if block == "yes":
        floor = input(" student in the floor: ")
        if floor == "yes":
            classes = input(" student in classes:")
            if classes == "yes":
                print("Student in  class")
            else:
                print("Student in  floor")
        else:
            print("Student in block")
    else:
        print("Student in  college")

else:
    print("Student not in college")
'''

#--------------------------------lift--------------------------------
#6floors:
#basic=6
#"up 3" --- we can't move

#***
#up 2 ---- 6 floor

#***
#down 6--- ground floor

#down 7 ---> we can't move we have only 6


choose="up 5".split()
print(choose)
print(choose[0])

move,floor="up 5".split()
print(move)
print(floor)

'''floor = 6

if move == "up":
    print("We can't move")


elif move == "down":
    if num <= 6:
        floor = floor - num


        if floor == 0:
            print("Ground Floor")
        else:
            print(floor, "Floor")
    else:
        print("We can't move. We have only 6 floors")


else:
    print("Invalid choice")

'''










































