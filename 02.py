# Crie um algoritmo que leia 3 valores (lados de um triângulo)
# Determine se formam um triângulo
# Se é um equilátero(3 lados iguais), isósceles(2 lados iguais) ou escaleno(todos os lados diferentes)

cor_rebecca = '\033[38;2;102;51;153m'
reset = '\033[0m'
cor_vermelho = '\033[31m'
cor_verde = '\033[38;2;0;250;154m'

rebecca1 = float(input(f"{cor_rebecca}Diga o tamanho do primeiro lado do triângulo: {reset}"))
rebecca2 = float(input(f"{cor_rebecca}Diga o tamanho do segundo lado do triângulo: {reset}"))
rebecca3 = float(input(f"{cor_rebecca}Diga o tamanho do terceiro lado do triângulo: {reset}"))

if rebecca1 > rebecca2 + rebecca3 or rebecca2 > rebecca1 + rebecca3 or rebecca3 > rebecca2 + rebecca1:
    print(f"{cor_vermelho} Isso não é um triângulo. {reset}")
else:
    print(f"{cor_verde} Isso é um triângulo: {reset}")
    if rebecca1 == rebecca2 == rebecca3 and rebecca1 != 0 and rebecca2 != 0 and rebecca3 != 0:
        print(f"{cor_rebecca}Equilátero. {reset}")
    elif rebecca1 == rebecca2 != rebecca3 or rebecca2 == rebecca3 != rebecca1 or rebecca3 == rebecca1 != rebecca2:
        print(f"{cor_rebecca}Isóceles. {reset}")
    elif rebecca1 != rebecca2 and rebecca2 != rebecca3 and rebecca3 != rebecca1:
        print(f"{cor_rebecca}Escaleno. {reset}")
    elif rebecca1 == 0 and rebecca2 == 0 and rebecca3 == 0:
        print(f"{cor_rebecca}Degenerado. {reset}")
    else:
        print("Como você chegou até aqui? ")

