print("Ingrese los siguientes valores")
base = int(input("base: "))
altura = int(input("altura: "))

area = base*altura/2

if int(area) > 1000:
    print("DATOS NO VALIDOS")
else:
    print(int(area))