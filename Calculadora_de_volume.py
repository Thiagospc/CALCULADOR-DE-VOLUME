import time
import math
#iniciando
print(60*'=')
print()
print(60*'#')
print()
print('Os valores serão calculados com pi = {}.'.format(math.pi))
print()
print(60*'#')
print()
# volume do cone
time.sleep(2)
print('Digite os valores abaixo:')
r = float(input('Raio >>>  '))
h = float(input('Altura >>>  '))

# cálculo do cone
V = (math.pi * (r ** 2) * h) /3

# cálculo do cilindro
vcil = (math.pi * (r ** 2)) * h

# volume da esfera
# cálculo da esfera
ve = (4 * math.pi * (r ** 3)) / 3
print()
time.sleep(1)
print('Calculando os valores: ')
time.sleep(1)
print(60*'+')
print(f'O volume do cone é {V} m³.')
print('O volume do cilindro é {} m³.'.format(vcil))
print('O volume da esfera é {} m³.'.format(ve))
print(80*'+')
print()
# lista
lista = [V, vcil, ve]
print('O maior volume é {} m³ e o menor volume é {} m³.'.format(max(lista), min(lista)))
print(80*'=') 
input()
