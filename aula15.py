nome = input("Qual o seu nome?")
print(f'O seu nome é {nome}')
print(f'O nome da variável é {nome=}')

numero_1 = input('Digite um número: ')
numero_2 = input('Digite outro número: ')

print(f'A soma entre {numero_1} e {numero_2} é {numero_1 + numero_2}')  # Concatenação

# Solução 1: converter para inteiro
int_numero_1 = int(numero_1)
int_numero_2 = int(numero_2)
print(f'A soma entre {int_numero_1} e {int_numero_2} é {int_numero_1 + int_numero_2}')
