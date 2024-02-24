import requests

# Función para obtener información de un personaje
def obtener_personaje(id):
    url = f"https://rickandmortyapi.com/api/character/{id}"
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        datos = respuesta.json()
        personaje = datos
        return personaje
    else:
        print(f"Error al obtener información del personaje: {respuesta.status_code}")
        return None

# Función para mostrar información de un personaje
def mostrar_informacion(personaje):
    print(f"Nombre: {personaje['name']}")
    print(f"Especie: {personaje['species']}")
    print(f"Género: {personaje['gender']}")
    print(f"Estado: {personaje['status']}")
    print(f"Ubicación: {personaje['location']['name']}")
    print(f"Imagen: {personaje['image']}")

# Obtener ID del personaje del usuario
id = input("Introduce el ID del personaje: ")

# Obtener información del personaje
personaje = obtener_personaje(id)

# Mostrar información del personaje
if personaje:
    mostrar_informacion(personaje)

