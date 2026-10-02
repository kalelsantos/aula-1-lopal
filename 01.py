aluno = input("Digite o nome do aluno: ")
ano_nascimento = int(input("Digite o ano de nascimento do aluno: "))
ano_atual = int(input("Diga em que ano estamos: "))
nota1 = float(input("Digite a primeira nota do aluno: "))
nota2 = float(input("Digite a segunda nota do aluno: "))

media = (nota1 + nota2) / 2 
idade = ano_atual - ano_nascimento

if media >= 7:
    situacao = "aprovado"
elif media >= 5:
    situacao = "recuperção"
else:
    situacao = "reprovado"

print(f"Aluno: {aluno}")
print(f"Ano de Nascimento: {ano_nascimento}")
print(f"Idade: {idade}")
print(f"Média: {media}")
print(f"Você está {situacao}!")
