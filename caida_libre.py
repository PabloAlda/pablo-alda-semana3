#Programa para calcular la posición de un objeto en caída libre.
#Pedimos el valor de la gravedad
gravedad = float(input("Introducir el valor de la gravedad: "))
#Pedimos el valor de la altura inicial
altura_inicial = float(input("introducir la altura inicial: "))
#Pedimos el tiempo en el que desea calcular la posición del objeto
tiempo = float(input("Introducir el tiempo en el que desea calcular la posición del objeto: "))
#Pedimos la velocidad inicial
velocidad = float(input("Introducir la velocidad inicial: "))
#Fórmula de un objeto en caída libre
altura_final = velocidad*tiempo-(1/2)*gravedad*tiempo*tiempo+altura_inicial
#Mostramos en pantalla el valor de la posición del objeto en el tiempo deseado.
print("El objeto se encuentra en la posición:", altura_final ,"metros.")