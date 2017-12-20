def C_to_F(Celsius):
    if Celsius < -273.15:
        return "Material temps can't be lower than 273.15C"
    else:
        Fahrenheit = Celsius*9/5+32
        return Fahrenheit

temps = [10,-20,-289,100]
for i in temps:
    print(C_to_F(i))