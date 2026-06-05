str  = "this is a string of characters"
str2  = 'dsad"s'
str3 = """asdafsdad"""

sgtr = "this is a chapter on strings"

#concatination
print(str+str2)

#lenght
print(len(str))

#indexing
print(str[17])

#slicing postive index ending index not included
print(str[0:3])

print(str[0:])

print(str[0:len(str)])

print(str.replace("a","0"))

print(str[:len(str)])

#slicing negative index ending index not included
print(str[-18:-1])

print(str.endswith("'s"))

print(str.capitalize())

print(str.upper())

print(str.find('a'))

print(str.find("a string"))

print(str.count('a'))
