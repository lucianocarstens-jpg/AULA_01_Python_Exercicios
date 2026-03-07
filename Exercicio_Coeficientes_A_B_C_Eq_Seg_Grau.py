import math

# Solicitar os coeficientes
a = float(input("Digite a: "))
b = float(input("Digite b: "))
c = float(input("Digite c: "))

# Calcular o discriminante
discriminante = b**2 - 4*a*c

# Calcular as raízes
if discriminante > 0:
    raiz1 = (-b + math.sqrt(discriminante)) / (2 * a)
    raiz2 = (-b - math.sqrt(discriminante)) / (2 * a)
elif discriminante == 0:
    raiz1 = -b / (2 * a)
    raiz2 = raiz1
else:
    # Embora assumido que sempre há raízes reais, incluí para completude
    print("Erro: Não há raízes reais.")
    exit()

# Exibir as raízes
print(f"Raíz 1: {raiz1}")
print(f"Raíz 2: {raiz2}")