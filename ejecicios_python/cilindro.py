import math

#Escribir un algoritmo que determine el área y el volúmen de un cilindro


radio = float(input("ingrese el radio del cilindro "))
altura = float(input("ingrese altura  del cilindro "))

area = 2*(3.141592)*radio*altura + 2*(3.141592)*radio*radio

volumen = (3.141592)*radio*radio*altura

print (area)
print (volumen)

