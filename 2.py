# Oscar Encarnacion liz 
print("Leer 10 numeros enteros, almacenarlos en un vector y determinar cuantos numeros de los almacenados en dicho vector comienzan en 3\n")

numeros = input("Intruduzca Diez Numeros Separados Por Una Coma: ")
numeros = numeros.split(",")

total = 0 

for x in numeros:
  c = 0
  if x[0] == "3":
    c+=1
    total = total + c

print("Hay", total, "Numeros Que Empiezan Con Tres")    
input("Presione Enter Para Salir")