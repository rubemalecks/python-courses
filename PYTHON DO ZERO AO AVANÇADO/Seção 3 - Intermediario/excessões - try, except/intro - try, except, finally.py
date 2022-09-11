try:
    print(a)  # NameError

except NameError as erro:  # Exceção é tratada
    print("ERRO", erro)
print("continua...")  # O programa continua

# ---------------------------------------------------------
# Caso queira tratar qualquer exceção não prevista:

try:
    a = []
    print(a[1])
except Exception as erro:
    print(erro, "<== erro")

# ---------------------------------------------------------

try:
    a = {}
    print(a[1])
except NameError as erro:
    print("Erro do desenvolvedor")
except (IndexError, KeyError) as erro:  # + de 1 exceção
    print("Erro de indice ou chave")  # Só este vai ser executado
except Exception as erro:
    print("erro inesperado")
else:  # será executado se não ocorrer nenhuma exceção
    print(a)
finally:  # SERÁ EXECUTADO SEMPRE
    print("FIM")
