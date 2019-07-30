#print only even numbers from  a list

newlist = [1,2,3,4,5,6,7,8,9,10]
a = []
for i in newlist:
    if i % 2 == 0:
        a.append(i)
print(a)

print(type(a))

newlist2 = [x for x in range(1,11) if x % 2 == 0]
print(newlist2)




