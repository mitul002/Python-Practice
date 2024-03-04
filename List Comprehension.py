#list comprenssion

li=[i for i in range(1,11)]
print(li*3)
li2=[i*3 for i in range(1,11)]
print(li2)
li3=[i*3 for i in range(1,11) if i%2==0]
print(li3)

print([i for i in [10,15,20,25,30,35,40,45,50] if i%2==0])
