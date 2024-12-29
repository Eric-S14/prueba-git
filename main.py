def redondear(numero):
    if numero > 3.50:
        return int(numero) + 1
    else:
        return int(numero)

def suma_redondeada(a, b):
    resultado = a + b
    return redondear(resultado)

numero1 = 2.45
numero2 = 1.10
print(f"La suma redondeada de {numero1} y {numero2} es: {suma_redondeada(numero1, numero2)}")
