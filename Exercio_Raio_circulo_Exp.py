import math

# Solicitar o raio do círculo
raio = float(input("Digite o raio do círculo: "))

# Calcular a área usando **
area = math.pi * (raio ** 2)

# Calcular o perímetro
perimetro = 2 * math.pi * raio

# Exibir os resultados
print(f"A área do círculo é: {area:.2f}")
print(f"O perímetro do círculo é: {perimetro:.2f}")