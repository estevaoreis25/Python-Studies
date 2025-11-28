"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""

num_str = input('Digite um número inteiro: ')

try:
  num_int = int(num_str)
  if num_int % 2 == 0:
    print(f'O número {num_int} é par.')
  else:
    print(f'O número {num_int} é ímpar.')
except:
  print('Isso não é um número inteiro.')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora_atual_str = input('Que horas são? ')
try:
  hora_atual = int(hora_atual_str)
  if hora_atual in range(0, 12):
    print('Bom dia!')
  elif hora_atual in range(12, 18):
    print('Boa tarde!')
  elif hora_atual in range(18, 24):
    print('Boa noite!')
  else:
    print('Hora inválida. Digite um valor entre 0 e 23.')

except ValueError:
  print('Você não digitou uma hora válida.')


"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
nome = input('Digite seu primeiro nome: ').strip()
tamanho_nome = len(nome)

if tamanho_nome <= 4:
  print('Seu nome é curto.')
elif 5 <= tamanho_nome <= 6:
  print('Seu nome é normal.')
else:
  print('Seu nome é muito grande.')
