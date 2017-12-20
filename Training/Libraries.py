import os

All_Files = os.listdir()

for f in All_Files:
    with open(f,'r') as File:
        print("\n" + "***" + f + "***" + "\n")
        File.seek(0)
        content = File.readlines()
        content = [c.rstrip("\n") for c in content]
        for l in content:
            print(l)