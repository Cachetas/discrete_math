#-----------------------------------------------------------------------------------
# Exercício 2
# 9g: p -> q e (p ^ !q) -> F

def implica(a , b):
    if b == False and a == True: # Podemos atribuir uma condição para essa excepção.
     return False # E retornar falso.
    else:
     return True # Em qualquer outro caso, retornamos verdadeiro.

tabelaExpressaoA = []
tabelaExpressaoB = []
tabela = [[False, False], [False, True], [True, False], [True, True]]

for x in range (len(tabela)):
    p = tabela[x][0]
    q = tabela[x][1]
    # Segundo a ordem de operações a disjunção é prioritária à implicação

    ExpressaoA = implica(p, q) # p -> q

# ---

    if (p == True and (not q) == True): # (p ^ !q)
        e1 = True
    else:
        e1 = False

    ExpressaoB = implica(e1, False) # (p ^ !q) -> F

    # Adicionamos os valores às tabelas de verdade de cada expressão
    tabelaExpressaoA.append(ExpressaoA)
    tabelaExpressaoB.append(ExpressaoB)

# ---Fim do loop---

# E por último verificamos a equivalência das tabelas de verdade das duas expressões
if (set(tabelaExpressaoA) == set(tabelaExpressaoB)):
    print("Expressões equivalentes")
else:
    print("Expressões não equivalentes")