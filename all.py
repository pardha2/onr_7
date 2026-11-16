d={"name":"python","age":1991,"trend":"yes"}
print(d)
'''
print(d.get("age"))

#print(help(dict))

print(d.keys())

print(d.values())

print(d.items())



print(help(dict.update))

d.update(name="balayya",age=23)
print(d)

'''

#print(help(dict.setdefault))

d.setdefault("practice","done")

d.setdefault("time")


d.update([(1,876789)])
print(d)
print(d)

d.setdefault(1,2000)


print(d.pop("practice"))

print(d)
##
##print(d.popitem("practice"))
##print(d)

d1=d.copy()
print(d1)

print(d.clear())
print(d)
print(d1)

del d
print(d)














