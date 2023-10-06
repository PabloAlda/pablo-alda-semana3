#Función para calcular el área del pentágono
def area_pentagono (lado,apotema):
    area = 5*lado*apotema/2
    return area

#Pido apotema y lado al usuario
lado_input = float(input("Longitud de los lados"))
apotema_input = float(input("Longitud apotema"))
 
area_calculada = area_pentagono(lado_input,apotema_input)

print(area_calculada)

