print("Ingrese los voltajes")
v1 = int(input("voltaje1: "))
v2 = int(input("voltaje2: "))
v3 = int(input("voltaje3: "))

promedio = (v1 + v2 + v3) / 3

if promedio < 115:
    print("VOLTAJE CORRECTO")
elif promedio > 115 and promedio < 220:
    print("ALTO VOLTAJE")
elif promedio > 220:
    print("PELIGRO")