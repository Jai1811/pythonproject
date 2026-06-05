#collection of unordered items, each element must be unique & immutable
sets = {1,2,3,4,5,2,3,1,"hello","world"}

#bad_set = {1, 2, [3, 4]}  # Raises TypeError: unhashable type: 'list'
#bad_set2 = {1,2,{"badsetDict",2}} # Raises TypeError: unhashable type: 'Dict'
good_set = {1,2,3,4,5,(6,7,8)}


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

print(set1.union(set2))#combines both set values and returns a new set

print(set1.intersection(set2))#combines common values and returns new



sets.clear()