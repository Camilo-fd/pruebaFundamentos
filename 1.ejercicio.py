print("Ingrese el valor de los voltaje")
num1 = int(input())
num2 = int(input())
num3 = int(input())
num4 = int(input())
num5 = int(input())

promedio = num1 + num2 + num3 + num4 + num5 / 5

if promedio > 220:
    print("ALTO VOLTAJE")
else:
    print("VOLTAJE CORRECTO")