# Oscar Encarnacion liz 
print("Programa que acepta una frase y muestra los caracteres que posee la misma y cuantas veces se repiten.\n")


textbox = input("Ingrese una Frase: ")

resultado = {}

for letra in textbox:
	if letra in resultado:
		resultado[letra]=resultado[letra]+1

	else:
		resultado[letra]=1

print(resultado)
print("Longitud Total De Texto: ",len(textbox))		

input("Presione Enter Para Salir")