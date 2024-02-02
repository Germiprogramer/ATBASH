def cifrar_inverso(letra):
    alfabeto_min = "abcdefghijklmnopqrstuvwxyz"
    alfabeto_may = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

    if letra.islower():
        indice_min = alfabeto_min.index(letra)
        letra_cifrada = alfabeto_may[26 - indice_min - 1]
        return letra_cifrada
    elif letra.isupper():
        indice_may = alfabeto_may.index(letra)
        letra_cifrada = alfabeto_min[26 - indice_may - 1]
        return letra_cifrada
    else:
        return letra

def cifrar_mensaje(mensaje):
    mensaje_cifrado = ""
    for caracter in mensaje:
        mensaje_cifrado += cifrar_inverso(caracter)

    return mensaje_cifrado

# Ejemplo de uso:
mensaje_original = "GSVUOZTRHHZBDVZIVXIZAB"
mensaje_cifrado = cifrar_mensaje(mensaje_original)
print("Mensaje Original:", mensaje_original)
print("Mensaje Cifrado:", mensaje_cifrado)

