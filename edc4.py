#-----------------------------------------------
# Exercício 5

from sys import argv

def mdc(a , b):

    if a > b:
        dividendo = a
        divisor = b
    else: 
        dividendo = b
        divisor = a
    quociente = dividendo // divisor
    resto = dividendo - (quociente * divisor)

    while resto > 0:
        return mdc(quociente, resto)

    return print("O mínimo divisor comum é", divisor)

try:
    a = int(argv[1])
    b = int(argv[2])

except Exception as e:
    print("É necessário correr este script com os valores para as variáveis a e b")
    print("Exemplo python edc4.py a b, em que a é o dividendo e b é o divisor.")
    exit(1)

mdc(a, b)
