# programa em python que imprima os números de 1 a 105
for i in range(1, 106):
    print(i)

# programa que imprima os números de pares de 0 a 100
for i in range(0, 101, 2):
    print(i)

# programa que imprima os números de 5 a 10 de forma decrescente
for i in range(10, 4, -1):
    print(i)

# solicite ao usuário para digitar um número (n). Em seguida, ler n números da entrada e imprimir o triplo de cada um
n = int(input("Digite um número: "))
for i in range(n):
    numero = int(input("Digite um número: "))
    print(f"O triplo de {numero} é {numero * 3}")   


# solicite um número ao usuário e que, logo em seguida, imprima a tabuada de multiplicação desse número
numero = int(input("Digite um número: "))
for i in range(1, 11):
    print(f"{numero} x {i} = {numero * i}")


# algoritmo que solicite ao usuário um número de entrada (n), leia n números inteiros da entrada e imprima o maior deles. Suponha que todos os números lidos serão positivos
n = int(input("Digite um número: "))
maior = 0
for i in range(n):
    numero = int(input("Digite outro número: "))
    if numero > maior:
        maior = numero
    print(f"O maior número é {maior}")


# programa que leia a quantidade de pessoas de um grupo e para cada uma delas leia o nome e a altura. No final exiba: o nome e a altura da menor pessoa do grupo; a altura média do grupo e o número de pessoas com altura maior que 1.85 metros
n = int(input("Digite a quantidade de pessoas: "))

menor_nome = ""
menor_altura = 9999
soma = 0 
conta_maiores = 0

for i in range(n):
    nome = input("Nome: ")
    altura = float(input("Altura (em metros): "))

    if altura < menor_altura:
        menor_altura = altura
        menor_nome = nome
    
    soma += altura

    if altura > 1.85:
        conta_maiores += 1
        
media = soma / n

print(f"A menor pessoa é {menor_nome} com {menor_altura:.2f} m")
print(f"Soma das alturas: {soma:.2f} m")
print(f"A altura média do grupo é {media:.2f} m")
print(f"Número de pessoas com altura maior que 1.85 m: {conta_maiores}")



# sequência de Fibonacci
n = int(input("Digite a quantidade de termos da sequência de Fibonacci: "))

fibonacci = [0, 1]

for i in range(2, n):
    proximo = fibonacci[i-1] + fibonacci[i-2]
    fibonacci.append(proximo)

fibonacci = fibonacci[:n]

print(f"Os {n} primeiros termos da sequência de Fibonacci são:")
print(fibonacci)



# programa para digitar o salário bruto
for i in range(10):
    nome = input(f"Digite o nome da {i+1}ª pessoa: ")
    salario = float(input(f"Digite o salário bruto de {nome}: "))

    if salario < 2200:
        liquido = salario
    elif salario < 2800:
        liquido = salario - (salario * 0.075)
    elif salario < 3700:
        liquido = salario - (salario * 0.15)
    else:
        liquido = salario - (salario * 0.225)

    print(f"{nome} - Salário líquido: R${liquido:.2f}")


# programa que solicita notas de alunos 
soma_turma = 0
aprovados = 0

for i in range(20):
    nome = input(f"Digite o nome do {i+1}º aluno: ")
    nota1 = float(input("Digite a 1ª nota: "))
    nota2 = float(input("Digite a 2ª nota: "))
    nota3 = float(input("Digite a 3ª nota: "))

    media_aluno = (nota1 + nota2 + nota3) / 3
    print(f"{nome} - Média: {media_aluno:.2f}")

    soma_turma += media_aluno

    if media_aluno >= 5.0:
        aprovados += 1

media_turma = soma_turma / 20
percentual_aprovados = (aprovados / 20) * 100

print("\n--- Resultados finais ---")
print(f"Média da turma: {media_turma:.2f}")
print(f"Percentual de alunos aprovados: {percentual_aprovados:.2f}%")


