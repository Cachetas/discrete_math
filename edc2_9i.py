#-----------------------------------------------------------------------------------
# Exercício 2
# 9i: (s -> t) ^ (u v t v !s) e s -> t

def implica(a , b):
    if b == False and a == True: # Podemos atribuir uma condição para essa excepção.
     return False # E retornar falso.
    else:
     return True # Em qualquer outro caso, retornamos verdadeiro.

tabelaExpressaoA = []
tabelaExpressaoB = []
tabela = [
    [False, False, False, False], [False, False, False, True], [False, False, True, False], [False, False, True, True],
    [False, True, False, False], [False, True, False, True], [False, True, True, False], [False, True, True, True],
    [True, False, False, False], [True, False, False, True], [True, False, True, False], [True, False, True, True],
    [True, True, False, False], [True, True, False, True], [True, True, True, False], [True, True, True, True]]

for x in range (len(tabela)):
    s = tabela[x][0]
    t = tabela[x][1]
    u = tabela[x][2]
    v = tabela[x][3]

    e1 = implica(s, t) # (s -> t)

    if(u or t or (not s) == True): # (u v t v !s)
        e2 = True
    else:
        e2 = False

    if(e1 and e2 == True): #(s -> t) ^ (u v t v !s)
        ExpressaoA = True
    else:
        ExpressaoA = False

# ---

    ExpressaoB = implica(s, t) # s -> t

    # Adicionamos os valores às tabelas de verdade de cada expressão
    tabelaExpressaoA.append(ExpressaoA)
    tabelaExpressaoB.append(ExpressaoB)

# ---Fim do loop---

# E por último verificamos a equivalência das tabelas de verdade das duas expressões
if (set(tabelaExpressaoA) == set(tabelaExpressaoB)):
    print("Expressões equivalentes")
else:
    print("Expressões não equivalentes")

