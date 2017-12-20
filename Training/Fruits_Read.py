file = open("Fruits", 'r')
file.seek(0)
content = file.readlines()
content = [i.rstrip("\n") for i in content]
for j in content:
    print(len(j))
file.close()