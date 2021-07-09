#-----------------------------------------------
# Exercício 3

# Módulo para importar argumentos ao abrirmos a função
from sys import argv

def modulo(x, n):
    a = x // n
    b = x - (a * n)
    return b

# Tentamos verificar se o programa está a abrir com os parametros correctos
try:
    x = int(argv[1])
    n = int(argv[2])

# Caso não esteja, retornamos um erro
except Exception as e:
    print("")
    print("É necessário correr este script com dois números: x e n.")
    print("Exemplo: python edc3.py x n, em que x é o dividendo e n é o divisor.")
    print("")
    exit(1)

print("")
print(x, "mod", n, "=", modulo(x, n))
print("")