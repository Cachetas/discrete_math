#-----------------------------------------------------------------------------------
# Exercício 2
# Utilizaremos a mesma lógica definida no 2_9a para os próximos exercícios 9c, 9e, 9g, 9i
# 9c: (p->r) v (q->r) e (p ^ q) -> r

def implica(a , b):
    if b == False and a == True: # Podemos atribuir uma condição para essa excepção.
     return False # E retornar falso.
    else:
     return True # Em qualquer outro caso, retornamos verdadeiro.

tabelaExpressaoA = []
tabelaExpressaoB = []
tabela = [[False, False, False], [False, False, True], [False, True, False], [False, True, True], [True, False, False], [True, False, True], [True, True, True]]

for x in range (len(tabela)):
    p = tabela[x][0]
    q = tabela[x][1]
    r = tabela[x][2]

    e1 = implica(p, r) # (p->r)
    e2 = implica(q, r) # (q->r)

    if (e1 == True or e2 == True): # (p->r) v (q->r)
        ExpressaoA = True
    else:
        ExpressaoA = False

# ---

    if (p == True and q == True): # (p ^ q)
        e3 = True
    else:
        e3 = False

    ExpressaoB = implica(e3, r) # (p ^ q) -> r

# Adicionamos os valores às tabelas de verdade de cada expressão
    tabelaExpressaoA.append(ExpressaoA)
    tabelaExpressaoB.append(ExpressaoB)

# ---Fim do loop---

# E por último verificamos a equivalência das tabelas de verdade das duas expressões
if (set(tabelaExpressaoA) == set(tabelaExpressaoB)):
    print("Expressões equivalentes")
else:
    print("Expressões não equivalentes")
