#Inicio  
#    1. Solicitar al usuario las medidas en cm
#    Mostrar mensaje "Por favor, ingresar las medidas deseadas en cm: "
medidas_cm = float(input ("Por favor, ingresar las medidas deseadas en cm: "))
#    2. Convertir las medidas solicitadas en pulgadas
#    convertir medidas = medidas_en_centimetros / 2.54
pulgadas = 2.54
conversion = medidas_cm / pulgadas
#    3. Mostrar las medidas en pulgadas
#    Mostrar mensaje: "Las medidas en pulgadas son: ", medidas
print("Las medidas en pulgadas son: ", conversion)
#Fin del programa