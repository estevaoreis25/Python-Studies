# Calculadora com while

while True:
  num1 = input('Digite o primeiro número:')
  num2 = input('Digite o segundo número:')
  operador = input('Digite o operador (+-*/):')
  
  if not num1.isnumeric() or not num2.isnumeric():
    print('Vocẽ precisa digitar números válidos.')
    continue
  num1 = float(num1)
  num2 = float(num2)
  resultado = 0

  if len(operador) > 1 or operador not in '+-*/':
    print('Operador inválido.')
    continue
  elif operador == '+':
    resultado = num1 + num2
  elif operador == '-': 
    resultado = num1 - num2
  elif operador == '*':
    resultado = num1 * num2
  elif operador == '/':
    resultado = num1 / num2
  print(f'O resultado é: {resultado}')
  sair = input('Quer sair? [s]im: ').lower().startswith('s')
  if sair:
    print('Saindo ...')
    break
  