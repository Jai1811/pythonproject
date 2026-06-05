#ordered, immutable sequences, used to protect data from accidental changes
tup = ("",1.24,'a',1,1)


print(tup[1])

#returns the first index appreance of the item
print(tup.index(1))

#return the total number of appearence of the element
print(tup.count(1))



print(tup)
print(type(tup))


