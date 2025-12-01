import os

palavra_secreta = "abracadabra"
qtd_tentativas = 0
letras_acertadas = []

while True:
  letra_digitada = input('Digite uma letra: ')
  qtd_tentativas +=1
  if len(letra_digitada) > 1:
    print('Digite apenas uma letra.')
    continue
  if letra_digitada in letras_acertadas:
    print('Você já tentou essa letra. Tente outra.')
    continue
  if palavra_secreta.count(letra_digitada) > 0:
    letras_acertadas.append(letra_digitada)
  
  os.system('clear')
  print('Palavra secreta: ', end='')
  encontrou_todas = True
  for letra in palavra_secreta:
    if letra in letras_acertadas:
      print(letra, end='')
    else:
      print('_', end='')
      encontrou_todas = False
  print()
  if encontrou_todas:
    print('Parabéns! Você ganhou!')
    print(f'Número de tentativas: {qtd_tentativas}')
    break
  