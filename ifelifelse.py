#leap year:

'''
year=int(input())

#is this year is leap year or not?
if year%4==0 and year%100!=0 or year%400==0:
    print("leap year")
else:
    print("not a leap year")

'''






#find grade of a student based on marks:
##90-100 -->A
##80-90-->B
##60-80-->C
##less than 40-->fail


#give number is
##less than 0 negative
##equal to 0 equal
##greater than 0 positive

'''
num=int(input("enter the value"))
if num > 0:
    print("positive")
elif num < 0:
    print("negative")
else:
    print("zero")
    '''




#take multiple values and multiple varibles in a single line:
#need to find greatest among three
'''
a,b,c=map(int,input().split())
if a>b and a>c:
    pritn(a)
elif b>a and b>c:
    print(b)
else:
    print(c)
'''





#take a empty dictinary
#take 2 inputs from the user 1.username 2. password:
#add username as key and password as value

#1.user and password if both are in dictinary then print valid
#otherwise not valid



'''
data={'john': 23456,"sai":34567,"raju":87654}

##username=input()
##password=input()
##data[username]=password

print(data)


username=input()
password=int(input())

if username in data and password in data.values():
    print("valid")
else:
    print("invalid")

'''

#------------------> nested conditions <-----------------------
'''
if condition:
    #statement
    if condition:
        #statement
    else:
        #statement 2
else:
    #statement 3
'''
        

'''
mens=["pants","shirts","shorts"]
womens=["tops","dupata","dreeses"]
option=int(input("1.mens 2.womens:"))

if option==1:
    print(mens)
    choose=int(input("select size:"))
    if choose>=32 and choose<=38:
        print("avaialble")
    else:
        print("not avialble")

else:
    print(womens)
    choose=int(input("1.size 2. colors"))
    colors=["red","blue","green"]
    if choose==1:
        size=int(input())
        if choose>=32 and choose<=38:
            print("avaialble")
    else:
        print(colors)
'''


#1.
#username is username exists then
#ask password
#username not exist ---> username not found
#wrong password


#2. electricity bill
name,units,

1-100 units per unit 5 rs
101-200 units per units 6 rs
201- 500 units per units 10 rs
















