"""
Escreva um programa que leia três valores com ponto flutuante de dupla precisão: A, B e C. Em seguida, calcule e mostre:
a) a área do triângulo retângulo que tem A por base e C por altura.
b) a área do círculo de raio C. (pi = 3.14159)
c) a área do trapézio que tem A e B por bases e C por altura.
d) a área do quadrado que tem lado B.
e) a área do retângulo que tem lados A e B.
Entrada
O arquivo de entrada contém três valores com um dígito após o ponto decimal.

Saída
O arquivo de saída deverá conter 5 linhas de dados. Cada linha corresponde a uma das áreas descritas acima, sempre com mensagem correspondente e um espaço entre os dois pontos e o valor. O valor calculado deve ser apresentado com 3 dígitos após o ponto decimal.
"""
a, b, c = input().split()

a = float(a)
b = float(b)
c = float(c)

resp_A = a * c / 2
resp_B = c ** 2 * 3.14159
resp_C = (a + b) * c / 2
resp_D = b ** 2
resp_E = a * b

print(f"TRIANGULO: {resp_A:.3f}")
print(f"CIRCULO: {resp_B:.3f}")
print(f"TRAPEZIO: {resp_C:.3f}")
print(f"QUADRADO: {resp_D:.3f}")
print(f"RETANGULO: {resp_E:.3f}")
