class Student:

    #class attribute
    universityName = "ABC university"
    name = "anonymous"

    def __init__(self, name, age, rollnumber, subject):
        self.name = name
        self.age = age
        self.rollnumber = rollnumber
        self.subject = subject

    def addStudentToDictionary(self):
         dictStudent = {"name": self.name,
                        "age":self.age,
                        "rollnumber":self.rollnumber,
                        "subject":self.subject
                        }
         return dictStudent

    def addStudentNameTotuple(self):
        tupleStudentName = (self.name)
        return tupleStudentName

    @staticmethod
    def this_is_static_method():
        print("this is static method")

s1 = Student("Shivam",21,56,["Physics","Chemistry","Maths","Accounts"])
s2  = Student("Vivek",23, 24,"PCM-A")

#print(s1.addStudentNameTotuple())
#print(s1.addStudentToDictionary())
#print(s2.addStudentToDictionary())

s1.name = "Vijay"
#print(s1.addStudentNameTotuple())

#print(s1.addStudentToDictionary())

#print(Student.universityName)
#print(s1.universityName)

print(Student.this_is_static_method())


