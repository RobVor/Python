import pandas

DataFrame = pandas.DataFrame([[2,4,6],[10,20,30]],index=["First","Second"],columns=["Price", "Age", "Value"])
print(DataFrame,"\n")

DataFrame2 = pandas.DataFrame([{"Name":"Rob","Surname":"Vor"},{"Name":"Jack","Surname":"Longe"},{"Name":"Desmond"}])
print(DataFrame2,"\n")

print(DataFrame.mean())

DataFrame3 = pandas.read_csv("C:\\Users\\rvorster\\Downloads\\GI_processed.csv")
print(DataFrame3)