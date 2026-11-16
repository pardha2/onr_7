#print(help(set))

'''
s=set((6,4,1,2,3,4,5))
print(id(s))
print(type(s))
print(s)

#print(help(set.add))

s.add(7)
print(id(s))
#print(s[0])
print(s)
'''






##s={1,True,"balayya",2+3j}
##print(s)
##
##s1={"robo",True,5+10j,1}
##print(s1)

'''
s=set()
s.add("hari")
print(s)

#print(help(set.update))

s.update(("pfs","python developer"))
print(s)

#s.remove("pfs")
##print(s.pop())
##print(s)

s.discard("pfs")
print(s)

s.clear()
print(s)

del(s)
print(s)


s={1,0}
s.discard(False)
print(s)
'''

print(help(set.union))

gandhiji={"pardhu","hari","ganesh","jyothi","aswitha","rahul"}
nehruji={"kamal","enos","chari","jyothi","aswitha","rahul"}

#union:----> all 
print(gandhiji.union(nehruji))
print(nehruji | gandhiji)


#intersection:----> commom 
print(gandhiji.intersection(nehruji))
print(nehruji & gandhiji)


#difference:
print(gandhiji.difference(nehruji))
print(nehruji-gandhiji)


#print(help(set.symmetric_difference))

print(gandhiji.symmetric_difference(nehruji))
print(nehruji ^ gandhiji)


#superset:
s1={1,2,3,4}
s2={1,2,3,4,5}
print(s1.issuperset(s2))
print(s1>=s2)


#subset:
print(s1.issubset(s2))
print(s1<=s2)


x={1,2,3,5}
y={4,5,6,5}
print(x.isdisjoint(y))






