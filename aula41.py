""" while/else """

frase = "Python é uma linguagem de programação incrível"

index = 0
while index < len(frase):
    letra = frase[index]

    if letra == ' ':
        print('Achei um espaço em branco')
        break
    print(letra)
    index += 1
else:
    print('Não achei um espaço em branco')
print('Acabou')