c = ["H", 2, "There!", 3.5]
print(c)
print(type(c))
print(dir(c))
print(dir([]))
print(c[1:3])
for i in c:
    print(type(i))

c.append("Hi!")
print(c)
c.remove("Hi!")
print(c)