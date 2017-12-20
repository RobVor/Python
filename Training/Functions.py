def Minutes_to_Hours(min):
    hours = min / 60
    return hours

print(Minutes_to_Hours(70))

def Opt(x, y, *Optional_Argument, **keyword):
    if ('optional' in keyword):
        print("Optional parameter was added. Parm is set at: ",keyword['optional'])
    else:
        print("No optional parameters have been added.")
    print(x,y,Optional_Argument,keyword)

Opt(1,2)
Opt(1,2,3)
Opt(1,2,3,4,5,optional='We have an entry!', optional2='And another one!', optional3='Last One!')