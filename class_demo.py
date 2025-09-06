class Addition:
    num = 100
    def __init__(self, a, b):
        self.first_number = a
        self.second_number = b
        print("Executing constructor")

    def getdata(self):
        print("Executing getData method")

    def summation(self):
        print("Executing summation method")
        return self.first_number + self.second_number + Addition.num

# obj = Addition(2, 3)
# obj.getdata()
# print(obj.summation())
#
# print("---------------------------------------")
#
# obj1 = Addition(4, 5)
# obj1.getdata()
# print(obj1.summation())