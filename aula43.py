# Aula inicial sobre For 

texto = 'Python'

novo_texto = ''
for letra in texto:
   novo_texto += f'*{letra}'

novo_texto += '*'
print(novo_texto)