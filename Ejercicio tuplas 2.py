fechatuplal=(25, 12, 2016)
print("Imprimimos la primer tupla")
print(fechatuplal)

fechalista=list(fechatuplal)
print("Imprimimos la lista que se le copio la tupla anterior")
print(fechalista)

fechalista[0]=31
print("Imprimimos la lista ya modificada")
print(fechalista)

fechatupla2=tuple(fechalista)
print("Imprimimos la segunda tupla que se le copio la lista")
print(fechatupla2)
