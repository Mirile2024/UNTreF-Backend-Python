# Pueden imprimir texto con comillas simples y dobles
print("Hola D'artagnan")
print('Hola "mundo" con comillas simples')

print("""Hola "D'artagnan" con comillas dobles""")

print("Hola \"D'artagnan\" con comillas dobles")
print('Hola "D\'artagnan" con comillas dobles')

""" Pueden hacer comentarios con tres comillas dobles
y que tengan multiples lineas
"""

print("""Hola "D'artagnan" con comillas dobles
      Pueden ir en lineas
      y se pueden anidar
      """)

# Pueden pasar varios parametros al print
print("Hola", "D'artagnan", "con", "comillas", "dobles")

#pueden pasarle un parametro sep
print("Hola", "D'artagnan", "con", "comillas", "dobles", sep="-")
# pueden pasarle un parametro end
print("Hola", "D'artagnan", "con", "comillas", "dobles", end="\n")
print(88)