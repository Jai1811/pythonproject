sets = {1,2,3,4,5,2,3,1,"hello","world"}

emptydictionary = {}

emptyset = set()

print(sets)
print(len(sets))
print("This is an empty dict", emptydictionary)

sets.add(54)
sets.add((1,2,3))

print(sets)

set1 = {1,2,3,4,5}

set2 = {1,2,3,5,6,7,8}

print(set1.union(set2))

print(set1.intersection(set2))



sets.clear()