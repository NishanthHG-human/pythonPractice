# arr = [1, 2, "nishanth", 3, "Me"]
# print(arr[0])
# print(arr[1:4])
# arr[2] = "NishanthHG"
# print(arr)
# arr.insert(3, "inserted")
# print(arr)
# arr.append("Last added")
# print(arr)
# del arr[0]
# print(arr)
# print(len(arr))
# print(arr[-1])
# print("------------------------------------------------------")
# tup = (1, 2, "Nishanth", 3)
# print(tup[1])
# print(tup[2])
# #tup[2] = "Rahul"
# print("------------------------------------------------------")
#
# dict1= {1: "Hello", 'a': 123, 'b': "I am robo"}
# print(dict1[1])
# print(dict1.get("a"))
# print(dict1['b'])
#
# print("-----------------------------------------------------")

car = {
    "make": "Toyota",
    "model": "Camry",
    "year": 2020,
    "color": "Blue"
}
print(f"Car model: {car.get('model')}")

car["owner"]= "Rahul"
print(car)