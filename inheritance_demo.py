from class_demo import Addition


class Inheritance(Addition):
    num2 = 200

    def __init__(self):
        Addition.__init__(self, 5,5)

    def number_addition(self):
        print("Executing number_addition method")
        return self.num2 + self.summation()

obj = Inheritance()
print(obj.number_addition())
