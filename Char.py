StarBase = "*"

for i,j in enumerate(reversed(range(10))):
    NewStar = ((StarBase * (i-1)).rjust(9) + (StarBase * i))
    if i > 5:
        NewStar = NewStar[:i] + " "* j + NewStar[:i]
    print(NewStar)
for i,j in enumerate(reversed(range(10))):
    NewStar = ((StarBase * (j-1)).rjust(9) + (StarBase * j))
    if i < 4:
        NewStar = NewStar[:j] + " " * i + NewStar[:j]
    print(NewStar)