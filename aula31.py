"""
Flag (Bandeira) - Marca um local
None = Não valor
is e is not  = e ou não é (tipo, valor, identidade)
id = identidade do objeto
"""

v1 = 'a'
v2 = 'a'
print(id(v1))
print(id(v2))

v3 = 'b'
print(id(v3))

condicao = False
passou_no_if = None

if condicao:
  passou_no_if = True
  print('Faça algo')
else:
  print('Não faça algo')

if passou_no_if is None:
  print('Não passou no if')
else:
  print('Passou no if')

