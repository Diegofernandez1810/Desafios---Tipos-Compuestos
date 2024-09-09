nombres=[]
edades=[]
for x in range(2):
    nom=input("Ingrese el nombre de la persona:")
    nombres.append(nom)
    ed=int(input("ingrese la edad de dicha persona:"))
    edades.append(ed)

print("Nombre de las personas mayores de edad:")
for x in range(2):
    if edades[x]>=18:
        print(nombres[x])
