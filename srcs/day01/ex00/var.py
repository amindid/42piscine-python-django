def my_var():
    intnum = 42
    string1 = "42"
    string2 = "quarante-deux"
    floatnum = 42.0
    boolvar = True
    listvar = [42]
    dictvar = {42: 42}
    tuplevar = (42,)
    setvar = set()
    print(f"{intnum} has a type {type(intnum)}")
    print(f"{string1} has a type {type(string1)}")
    print(f"{string2} has a type {type(string2)}")
    print(f"{floatnum} has a type {type(floatnum)}")
    print(f"{boolvar} has a type {type(boolvar)}")
    print(f"{listvar} has a type {type(listvar)}")
    print(f"{dictvar} has a type {type(dictvar)}")
    print(f"{tuplevar} has a type {type(tuplevar)}")
    print(f"{setvar} has a type {type(setvar)}")

if __name__ == '__main__':
    my_var()