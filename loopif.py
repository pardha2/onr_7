'''
x=[1, 2, 4,0,5,9,8,10]

l=[]
o=[]
e=[]
for i in range(len(x)):
    if i%2==0 and x[i]%2!=0:
        l.append(x[i])

    if i%2!=0 and x[i]%2!=0:
        o.append(x[i])

    if i%2!=0 and x[i]%2==0:
        e.append(x[i])
        
print(l)
print(o)
print(e)
'''

'''
names=["a","b","c","d","e"]
s=""
for i in range(len(names)):
    if i%2==0:
        s+=names[i].upper()
print(s)
'''

#reverse:
names=["a","b","c","d","e"]
#["e","d","c","b","a"]
l=[]
s=""
'''
for i in names:
    l.insert(0,i)
print(l)
'''

'''
for i in range(len(names)-1,-1,-1):
    l.append(names[i])
print(l)
'''

'''
for i in range(len(names)-1,-1,-1):
    s+=names[i]
print(s)
'''

#x="".join(names[::-1])
#print(x,"direct")
for i in names:
    s=i+s
print(s)





#withou swapcase convert lower - upper, upper - lower
##x=["A","b","C","d","e","F","G"]
##["a","B","c","D","E","f","g"]
##
##
###find vowels in a string:
##x="hello"
##"eo"
##
###find consnants:
##x="hello"
##"hll"
##
###print whos marks
##d={"john":500,"hari":600,"sai":300,"ram":250}
##greater then 500 =A
##greater than 400 =B
##greater than 300 =c
##otherwise fail
##
###o/p:
##{"john":"B","hari":"B","sai":"fail","ram":"fail"}
##
##
##
















