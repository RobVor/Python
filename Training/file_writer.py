file = open("Writer.txt",'w')
file.write("Line 1\n")
file.write("Line 2\n")
list = ["Line 1", "Line 2", "Line 3"]
for j in list:
    file.write(j + "\n")
file.close()

file = open("Number", 'w')
NumList = [1,2,3]
for i in NumList:
    file.write(str(i) + "\n")
file.close()

file = open("Writer.txt",'a')
list = ["Add 1", "Add 2", "Add 3"]
for k in list:
    file.write(k + "\n")
file.close()