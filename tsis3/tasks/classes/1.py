class InOutString:
    def __init__(self):
        self.s = ""

    def getString(self):
        print("Enter a string: ")
        self.s = input()

    def printString(self):
        print(self.s.upper())

str = InOutString()
str.getString()
str.printString()