with open("file.txt", "r") as file:
    count = sum(1 for i in file)
print(count)

print("-----------------------------------------------")

with open("file.txt", "r") as file:
    line = file.readline()
    while line != "":
        print(line)
        line = file.readline()
print("-----------------------------------------------")

with open("file.txt", "r") as reader:
    line = reader.readlines()
    reversed(line)
    with open("file.txt", 'w') as writer:
        for line1 in reversed(line):
            writer.write(line1)


