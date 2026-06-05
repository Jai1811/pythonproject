#to make variables or variables as private __ is appended in the beginning of the word
#to make variables protected _ is appended in the beginning of the word
class Account:
    __name ="anonymous"

    def __init__(self, accountNumber, password, bal):
        self.__accountNumber = accountNumber
        self.__password = password
        self.__bal = bal


    def set__accountNumber(self,accountNumber):
        self.__accountNumber =  accountNumber

    def get__accountNumber(self):
         return self.__accountNumber

    def __hello(self):
        print("this is a private method")



acc1 = Account(122343,"1213asda",218376)

acc2 = Account(21231,"12123wsxa",21213412)

acc2.set__accountNumber(2313)
print(acc2.get__accountNumber())


