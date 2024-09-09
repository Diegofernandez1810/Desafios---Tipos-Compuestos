conjunto_a = {1, 2, 3, 4}
conjunto_b = {3, 4, 5, 6}

union = conjunto_a.union(conjunto_b)
print(f"Unión: {union}")

interseccion = conjunto_a.intersection(conjunto_b)
print(f"Intersección: {interseccion}")

diferencia = conjunto_a.difference(conjunto_b)
print(f"Diferencia A - B: {diferencia}")

diferencia_simetrica = conjunto_a.symmetric_difference(conjunto_b)
print(f"Diferencia simétrica: {diferencia_simetrica}")
