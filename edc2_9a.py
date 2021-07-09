#-----------------------------------------------------------------------------------
# Exercício 2
# Utilizado a função anterior para o exercício 9a

def implica(a , b):
    if b == False and a == True: # Podemos atribuir uma condição para essa excepção.
     return False # E retornar falso.
    else:
     return True # Em qualquer outro caso, retornamos verdadeiro.


# Verificar se (p->q) ^ (p->r) é equivalente a p->(q^r)

# Criamos as tabelas de verdade
tabelaExpressaoA = []
tabelaExpressaoB = []
tabela = [[False, False, False], [False, False, True], [False, True, False], [False, True, True], [True, False, False], [True, False, True], [True, True, True]]

# Populamos as variáveis com os valores lógicos da tabela
for x in range (len(tabela)):
    p = tabela[x][0]
    q = tabela[x][1]
    r = tabela[x][2]

# Utilizamos a função anterior para nos dar o resultado lógico, com a tabela de verdade, das implicações da expressão
    e1 = implica(p, q) # (p->q)
    e2 = implica(p, r) # (p->r)

# Agora precisamos de calcular a conjunção das duas expressões com os valores lógicos anteriores
    if (e1 == True and e2 == True): # (p->q) ^ (p->r)
        ExpressaoA = True # Só é verdade se ambas forem verdade
    else:
        ExpressaoA = False # Caso contrário é falso

# ---

# Seguimos para a segunda expressão
# Calculamos o valor lógico de q ^ r da mesma maneira

    if (q == True and r == True): # (q ^ r)
        e4 = True
    else:
        e4 = False
# E usamos a função do exercício 1 para calcular o valor lógico da implicação de p com q ^ r
    ExpressaoB = implica(p, e4) # p -> (q ^ r)

# Adicionamos os valores às tabelas de verdade de cada expressão
    tabelaExpressaoA.append(ExpressaoA)
    tabelaExpressaoB.append(ExpressaoB)

# ---Fim do loop---

# E por último verificamos a equivalência das tabelas de verdade das duas expressões
if (set(tabelaExpressaoA) == set(tabelaExpressaoB)):
    print("Expressões equivalentes")
else:
    print("Expressões não equivalentes")


ExpressaoA == ExpressaoB

