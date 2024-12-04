import numpy as np
import random

def main():
  print("UCAB, elaborado por: Angel Araujo, Veronica Betancourt, Sebastian Armas, Ariagna Guerra, German Alonzo")
  E = np.array([" "]*10)
  V = np.array([0]*10)
  PG = np.array([0]*10)

  # funciones y procedimientos
  def Ganancias(a, b):
    if a == "I":
      print("Invierno")
      return b * 0.35
    elif a == "O":
      print("Otoño")
      return b * 0.15
    elif a == "P":
      print("Primavera")
      return b * 0.30
    else:
      print("Verano")
      return b * 0.20

  
  # Arreglo E
  for i in range(10):
    x = random.randint(1, 4)
    if x == 1:
      E[i] = "I"
    elif x == 2:
      E[i] = "O"
    elif x == 3:
      E[i] = "P"
    else:
      E[i] = "V"
    print(E[i], end=" ")
  print()

  # Arreglo V
  for i in range(10):
    y = random.randint(500, 999)
    V[i] = y
    print(V[i], end=" ")
  print()

  # Ganancias por estacion y arreglo PG
  print("Ganancias por estacion:")
  for i in range(0,10,1):
    PG[i] = Ganancias(E[i], V[i])
    print(PG[i], end=" ")
    print()

  # Menor estacion con ventas
  men = V[0]
  est = 0
  for i in range(0,10,1):
    if V[i] < men:
      men = V[i]
      est = E[i]
  print("La estacion con menos ventas es:", est,"con", men,"ventas")

  # Menor a mayor
  for i in range(0, 9, 1):
    for j in range(i + 1, 10, 1):
      if(V[j] < V[i]):
        aux = V[i]
        V[i] = V[j]
        V[j] = aux

      if(PG[j] < PG[i]):
        auy = PG[i]
        PG[i] = PG[j]
        PG[j] = auy
  print("Las ventas ordenadas de menor a mayor son: ")
  for i in range(0,10,1):
    print(V[i], end=" ")
  print()
  print("Y las ganancias de menor a mayor son:")
  for i in range(0,10,1):
    print(PG[i], end=" ")
  print()

  print("Las estaciones son: I = Invierno, O = Otoño, P = Primavera, V = Verano")
  print("Y el arreglo de estaciones es:", E)
  print("Las ventas por estaciones de menor a mayor son:",V)
  print("Las ganancias por estacion son:",PG)
  print()

  print("Con valores aleatorios hasta aqui") 

  print()
#--------------------------------------------------------------- Parte 4 y 5
  print("Con los valores que da el profesor")
  EE = ["I","O","V","P","P","O","V","V","I","V"]
  VV = [850,730,625,540,778,975,943,814,599,919]
  PGG = np.array([0]*10)
  # Menor estacion con ventas
  men = VV[0]
  est = 0
  for i in range(0,10,1):
    if VV[i] < men:
      men = VV[i]
      est = EE[i]
  print() 

  # Ganacias por estacion y arreglo PGG
  print("Ganancias por estacion:")
  for i in range(0, 10, 1):
    PGG[i] = Ganancias(EE[i], VV[i])
    print(PGG[i], end=" ")
    print()

  # Menor a mayor
  for i in range(0, 9, 1):
    for j in range(i + 1, 10, 1):
      if(VV[j] < VV[i]):
        aux = VV[i]
        VV[i] = VV[j]
        VV[j] = aux
      if (PGG[j] < PGG[i]):
        auy = PGG[i]
        PGG[i] = PGG[j]
        PGG[j] = auy

  print("Las estaciones son: I = Invierno, O = Otoño, P = Primavera, V = Verano")
  print("El arreglo de estaciones dado por el profesor es:", EE)
  print("Las ventas por estaciones y arreglado de menor a mayor dado por el profesor son:",VV)
  print("Las ganancias por estacion con los arreglos dados por el profesor son:",PGG)
  print("La estacion con menos ventas es:", est,"con", men,"ventas")
  print("Las ventas ordenadas de menor a mayor son: ")
  for i in range(0,10,1):
    print(VV[i], end=" ")
  print()
  print("Y las ganancias de menor a mayor son:")
  for i in range(0,10,1):
    print(PGG[i], end=" ")
  print()
  print()

main()
