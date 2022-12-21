import random
import string

def random_alphabet():
    # Crear lista con todas las letras del alfabeto
    alphabet = list(string.ascii_lowercase)

    # Mezclar aleatoriamente las letras de la lista
    random.shuffle(alphabet)

    # Convertir la lista mezclada en una cadena de caracteres y devolverla
    return ''.join(alphabet)

print(random_alphabet())