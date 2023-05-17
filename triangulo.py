A,B,C,D = map(int,input().split())
 
if (A + B > C and A + C > B and C + B > A) or (A + B > D and A + D > B and D + B > A) or (A + C > D and A + D > C and D + C > A):
    print("S")
 
elif (B + D > C and B + C > D and D + C > B):
    print("S")
else:
    print("N")


# Ana e suas amigas estão fazendo um trabalho de geometria para o colégio, em que precisam formar vários triângulos, numa cartolina, com algumas varetas de comprimentos diferentes. Logo elas perceberam que não dá para formar triângulos com três varetas de comprimentos quaisquer: se uma das varetas for muito grande em relação às outras duas, não dá para formar o triângulo.
# Neste problema, você precisa ajudar Ana e suas amigas a determinar se, dados os comprimentos de quatro varetas, é ou não é possível selecionar três varetas, dentre as quatro, e formar um triângulo.
# Input
# A entrada é composta por apenas uma linha contendo quatro números inteiros A, B, C e D (1 ≤ A, B, C, D ≤ 100).
# Output
# Seu programa deve produzir apenas uma linha contendo apenas um caractere, que deve ser 'S' caso seja possível formar o triângulo, ou 'N' caso não seja possível formar o triângulo.