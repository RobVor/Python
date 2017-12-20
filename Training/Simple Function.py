def C_to_F(Celsius):
    if Celsius < -273.15:
        return "The lowest temp matter can reach is -273.15. Lower is not possible"
    else:
        Fahrenheit = Celsius * 9/5 + 32
        return Fahrenheit

print(C_to_F(-274))

def StrLen(String):
    result = len(String)
    return result

print(StrLen("Hello"))

def StrLen2(s):
    if type(s) == int or type(s) == float:
        print("Error!")
    else:
        result = len(s)
        print(result)

StrLen2("5.5")