dato=input('Ingrese dato: ')
print(dato)
num=None
for convertidor in (int, float, complex):
    try:
      num=convertidor(dato)
      break
    except ValueError:
      pass

if num is None:
  print('Error de Entrada')
else:
  print(f'dato={num} del tipo: {type(num).__name__}')
  if type(num).__name__=='int':
    print('entero')
  if isinstance(num, int):
      print('es entero')

print(float('2.9')+int('2'))