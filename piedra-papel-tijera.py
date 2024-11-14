import unicodedata

nombre1 = input("¿Cómo se llamará el jugador 1?: ")
nombre2 = input("¿Cómo se llamará el jugador 2?: ")

# Función para normalizar el texto y eliminar acentos
def quitar_acentos(texto):
    return ''.join(
        c for c in unicodedata.normalize('NFD', texto)
        if unicodedata.category(c) != 'Mn'
    )

# Variable para controlar el bucle de turnos
jugar = True

while jugar:
    # Convertimos la elección a minúsculas
    jugador1 = input(f"¡Hola {nombre1}! ¿Qué eliges? ¿Piedra, papel o tijeras?: ").lower()
    jugador2 = input(f"¡Hola {nombre2}! ¿Qué eliges? ¿Piedra, papel o tijeras?: ").lower()

    # Condiciones de victoria para el jugador 1
    condicion1 = jugador1 == "piedra" and jugador2 == "tijeras"
    condicion2 = jugador1 == "papel" and jugador2 == "piedra"
    condicion3 = jugador1 == "tijeras" and jugador2 == "papel"

    # Verificamos el resultado
    if jugador1 == jugador2:
        print("¡Ha sido un empate!")
    elif condicion1 or condicion2 or condicion3:
        print('Ha ganado:', nombre1)
    else:
        print('Ha ganado:', nombre2)
    
    # Preguntar si quieren jugar otra vez y eliminar acentos
    otra_vez = input("¿Quieren jugar otra vez? (sí/no): ").lower()
    otra_vez = quitar_acentos(otra_vez)  # Normalizamos la respuesta

    if otra_vez != "si":
        jugar = False
        print("¡Gracias por jugar!")
