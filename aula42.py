frase = "Python é uma linguagem de programação" \
        'multiparadigma. ' \
        'Python foi criado por Guido van Rossum.'

# Saber qual letra na frase aparece mais vezes

index = 0
letra_mais_repetida = ''
qtd_letra_mais_repetida = 0
while index < len(frase):
  letra_atual = frase[index]
  if letra_atual == ' ':
    index += 1
    continue
  qtd_letra_atual = frase.count(letra_atual)

  if qtd_letra_atual > qtd_letra_mais_repetida:
    letra_mais_repetida = letra_atual
    qtd_letra_mais_repetida = qtd_letra_atual
  index += 1
print(f'A letra que mais apareceu foi "{letra_mais_repetida}" '
      f'que apareceu {qtd_letra_mais_repetida} vezes.')