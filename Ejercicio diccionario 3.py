contactos = {
    "Ana": "ana@gmail.com",
    "Juan": "juan@yahoo.com",
    "Sara": "sara@hotmail.com"
}

def agregar_contacto(nombre, email):
    contactos[nombre] = email

def eliminar_contacto(nombre):
    if nombre in contactos:
        del contactos[nombre]
    else:
        print("Contacto no encontrado")

def obtener_email(nombre):
    return contactos.get(nombre, "Contacto no encontrado")

def listar_contactos():
    for nombre, email in contactos.items():
        print(f"Nombre: {nombre}, Email: {email}")

agregar_contacto("Luis", "luis@gmail.com")

eliminar_contacto("Sara")

print(obtener_email("Ana"))

listar_contactos()
