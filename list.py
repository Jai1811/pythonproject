
marks = [20,30,90.6,45,32, 45]

list = ["Karan",67, 99, "Maths"]

sub_list=  list[:2]

print(list[0:3])

print(sub_list)

print(list)

print(marks[0])

print(len(marks))

list.append(56)
print("apended list", list)

marks.sort()
print("sorted list", marks)

marks.sort(reverse=True)
print("sorted list descending",marks)

list.reverse()
print("reversed list",list)

list.insert(2,23)
print("inserted 23 in list",list)

marks.remove(45)
print("removed object 45",marks)

marks.pop(2)
print("removed object at index 2", marks)

if marks.__contains__(90.6):
    print("excellent student")

