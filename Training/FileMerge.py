import os, datetime, time, glob2

Files = os.listdir()
ConcatTo = open(str(datetime.datetime.now().strftime("%Y-%m-%d-%H-%M-%S-%f")) + ".txt", 'a')
for i in Files:
    if i in ["file1.txt","file2.txt","file3.txt"]:
        with open(i, 'r') as FileGet:
            FileGet.seek(0)
            content = FileGet.read()
            print(content)
            ConcatTo.writelines(content + "\n")
ConcatTo.close()

fn = glob2.glob("*.txt")
print(fn)