'''
n=int(input("enter a number:"))

if n==10:
    print("equal")

if n>=10:
    print("greater")

if n<=100:
    print("possible")

print("done")
'''

'''
n=int(input())
if n>10:
    print(">10")
    
if n>20:
    print(">20")
    
if n>=50 and n<=60:
    print("half")
'''

#password=input()
##if password.isalpha(): #sdfg
##    print("valid")
##    
##if password.isnumeric():#123456
##    print("valid")
##    
##else:
##    print("invalid")


'''
if password.isalpha() and password.isnumeric():
    print("valid")

else:
    print("invalid")
'''


'''
password=input()

if not(password.isalnum()):
    print("valid")
else:
    print("invalid")

'''
    



##l=["pardhu","john","balayya","sampu"]
##take input from the user:

##ram
##success
##["pardhu","john","balayya","sampu","ram"]


'''
l=["pardhu","john","balayya","sampu"]
user=input()
if user not in l:
    print("valid")
    l.append(user)
    print(l)
    print("scuees")
else:
    print("invalid")
'''



#5 -->buzz
#3 -->fizz
# both 3 and 5 --> fizzbuzz
'''
num = int(input("Enter a number: "))
if num % 5 == 0:
    print("bus")
elif num%3==0:
    print("fizz")
elif num%3==0 and num%5==0:
    print("fizzbuzz")
else:
    print("wrong")
'''



#age?
#age 6-12 child
#age 13-18 teenage
#age 19-26 youth
#age greate than 27 uncle










while True:
    num = int(input("Enter a number: "))
    if num % 5 == 0:
        print("bus")
    elif num%3==0:
        print("fizz")
    elif num%3==0 and num%5==0:
        print("fizzbuzz")
    else:
        print("wrong")















