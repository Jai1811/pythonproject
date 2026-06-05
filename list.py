#ordered mutuable, allow duplicate elements
marks = [20,30,90.6,45,32, 45]

list = ["Karan",67, 99, "Maths"]

sub_list=  list[:2] #same as list[0:2]

print(list[0:3])

print(list[-4:-1])

print(sub_list)

print(list)

print(marks[0])

print(len(marks))

#adds an element to the list at the end
list.append(56)
print("apended list", list)

#sorts in ascending order
marks.sort()
print("sorted list", marks)

#sorts in ascending order
marks.sort(reverse=True)
print("sorted list descending",marks)

#reverses the list
list.reverse()
print("reversed list",list)

#inserts at a particular index
list.insert(2,23)
print("inserted 23 in list",list)

#removes the first occurance of an element
marks.remove(45)
print("removed object 45",marks)

#return and removes the item at the specified index
marks.pop(2)
print("removed object at index 2", marks)

if marks.__contains__(90.6):
    print("excellent student")

