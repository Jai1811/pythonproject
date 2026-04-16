
#over write
w = open("test.txt","w")
w.write("hello world appended\n")
w.close()


w = open("sample.txt","a")
w.close()

#append a file
w = open("test.txt","a")
w.write("appended again")
w.close()

