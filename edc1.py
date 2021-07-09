# Exercício 1

# Numa tabela de verdade, a->b é falso se e só se b for falso, e a for verdadeiro.
from sys import argv
from sys import exit

def implica(A , B, a, b):
    if B == False and A == True: # Podemos atribuir uma condição para essa excepção.
        print("")
        return str("{} e {} = Falso \n".format(a, b))  # E retornar falso.
    else:
        print("")
        return str("{} e {} = Verdadeiro \n".format(a, b)) # Em qualquer outro caso, retornamos verdadeiro.

try:
    a = argv[1]
    b = argv[2]

except Exception as e:
    print("É necessário correr este script num terminal com os valores lógicos das variáveis a e b")
    print("Exemplo: python edc1.py F V")
    exit(1)


if a == "V":
    A = True

elif a == "F":
    A = False

else:
    print("")
    print("O Valor inválido: {}".format(a))
    print("Execute o script como no exemplo com (V ou F como argumentos):")
    print("ex:. python edc1.py F V")
    print("")



if b == "V":
    B = True

elif b == "F":
    B = False

else:
    print("")
    print("O Valor inválido: {} ".format(b))
    print("Execute o script como no exemplo com (V ou F como argumentos):")
    print("ex:. python edc1.py F V")
    print("")
    exit(1)

print(implica(A, B, a, b))