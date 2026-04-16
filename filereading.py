#readmode
f = open("test.txt","r")
#data = f.read()
#data1 = f.read(5)
#datalinebyline = f.readline()

#print(datalinebyline)

with open("test.txt","r") as f:
    data = f.read()
    print(data)