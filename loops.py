age = 1
s = "break this"

#while
while(age>=1):
    print("Age is greater than one")
    if(s=="break this"):
        break

list = [1,2,3,4,56,6]

tup = (1,2,3,45,6,6)

#for loop with else
for num in list:
    print(num)
else:
    print("END")

for nums in tup:
    print(nums)
else:
    print("END")

#for loop over a range
for num in range(1,14,4):
    print(num)

#pass is a null statement that does nothing, it is used as a placeholder for future code
for i in range(1,7):
    pass
    print("AFTER PASS")