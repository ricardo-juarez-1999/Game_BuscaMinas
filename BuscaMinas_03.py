import os
os.system("cls")
import numpy as np
import time
import random as rm

#\\<=>=//#||''

## random.randint(a, b)   Elige uno de dos numeros al azar
## random.choice(lista)   Elige algun elemento al azar de una lista 
## random.sample(lista, k)   Elige k elememtos unicos al azar (sin repetir)
## random.shuffle(lista)   Revuelve una lista al azar

### JUEGASO DEL BUSCAMINAS TURBO MEJORADO!!!!!

## Elegir el tamaño de la matriz
## Elegir el nivel de dificultad

print("Bienvenido hermanito :D !!!")
time.sleep(1.5)

m = int(input("Elige el tamaño de filas de la matriz del juego: "))
n = int(input("Elige el tamaño de columnas de la matriz del juego: "))
l = m*n
print("1: Facil  \n2: Dificil  \n3: Extremo")
dif = int(input("Elige la dificultad del juego: "))
if dif == 1:
    b = int(l/4)
elif dif == 2:
    b = int(l/3)
elif dif == 3:
    b = int(l/2)
else:
    print("Solo están disponibles las opciones de arriba :P")

elemensos = ["🚩"] * (l-b) + ["💣"] * b
rm.shuffle(elemensos)
matriz = []

for i in range(m):
    fila = elemensos[i*n: (i+1)*n]
    matriz.append(fila)

for i in range(m):
    print(matriz[i])
print()

print("Buenas cainal ;D")
time.sleep(2)
print("Este es el Jueguito del BuscaMinas")
time.sleep(2)
print("Esta es tu matriz inicial:")
print()

matriz_visi = []
fila2 = ["?"] * l
for i in range(m):
    filon = fila2[i*n : (i+1)*n]
    matriz_visi.append(filon)
for i in range(m):
    print(matriz_visi[i])
print()

safe = 0

while safe != (l-b):
    fil = int(input("Ingresa un valor para las filas carnal por favor: "))
    col = int(input("Ingresa un valor para las columnas carnal por favor: "))
    print()

    if matriz[fil][col] == "🚩":
        print("Acertaste cainal ;D")
        print("Tu matriz es la siguiente:")
        matriz_visi[fil][col] = matriz[fil][col]
        for i in range(m):
            print(matriz_visi[i])
        safe += 1

    else:
        print("Lo siento carnal :c")
        time.sleep(2)
        print("Explotaste en Cachitos")
        print("Tu record fue el siguiente:")
        matriz_visi[fil][col] = matriz[fil][col]
        for i in range(m):
            print(matriz_visi[i])

        break

if safe == (l-b):
    print("Felicidades")
    print("Completaste el juego muy bien :D")
    print("Has sobrevivido otro día más")
