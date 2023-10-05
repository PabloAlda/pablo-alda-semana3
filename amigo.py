#Programa que hace preguntas y responde en función de ellas
#Pregunto el nombre
nombre = input("Hola, ¿cómo te llamas?")
#Preguntamos el sexo
sexo = input(f"{nombre}, ¿cuál es tu sexo?")
#Si es hombre le respondemos en masculino, si es mujer en femenino.
if sexo == 'Hombre':
 print("Encantado de conocerlo.")
else:
 print("Encantado de conocerla")
#Incluyo el nombre en la frase de pregunta de cumpleaños
cumpleanos = input(f"Qué día es tu cumpleaños {nombre}?")
#Pregunto que hizo ese día añadiendo su fecha
actividada_cumpleaños = input(f"Qué hiciste este año el {cumpleanos}")
#Respuesta amable
print("Qué plan más chulo.")
#Pregunto donde vive usando el nombre
lugar_vive = input(f"{nombre}, ¿dónde vives?")
#Si vive en MAdrid se mostrara un mensaje en pantalla
if lugar_vive=='Madrid':
  print("En Madrid hay mucha contaminación")
#Preguntar cuantos años tienes usando el nombre
anos = input(f"¿Cuántos años tienes {nombre}?")
#Si es mayor de edad se imprimira un mensaje en pantalla
if anos>'17':
    print(f"{nombre} ya puedes ir a la carcel, ten cuidado.")