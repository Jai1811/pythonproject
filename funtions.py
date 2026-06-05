from operator import length_hint


def prints():
    print("dasdadf",end ="$")
    print("hello\nworld"," Jai Vyas")
    len(" ")

def  sum(x=1,y=6):
    return (x+y)


print(sum(2,6))
print(sum())#this will use the default arguments

prints()

len("asdad")

range(1)


cities=["Delhi","Gurugram","Milton Keynes","London"]

def print_List(list):
    for city in list:
        print(city)

print_List(cities)

def print_item(value):
    """Print whether the given value is an int or str (safe for other types)."""
    if isinstance(value, int):
        print("The number is", value)
    elif isinstance(value, str):
        print("The string is", value)
    else:
        print("Unsupported type:", type(value))

