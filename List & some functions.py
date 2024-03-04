list1=[23, 30, 40,46, 'a', 'b', 'c']
print(list1[0])
print(list1[-2])
print(list1[0:3])

print("\nList 1: ")
for i in list1:
    print(i, end=" ")

list1.reverse()
print(f"\nReversed List {list1}\n")


list1.append("new item")
print(list1)


list1.pop()
list1.pop()
print(list1)

list1.remove(40)
print(list1)


list2=[93, 30, 40,46, 7, 1]

print("\nList 2:")
for i in list2:
    print(i, end=" ")
list2.sort()
print(f"\nSorted List {list2}\n")
list2.reverse()
print(f"Reversed List {list2}")
