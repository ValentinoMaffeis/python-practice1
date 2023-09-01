"""Conversiones Básicas"""


"""
Convertir los numeros de string a enteros y luego sumarlos.
"""

numero_01 = "123"
numero_02 = "456"
numero_03 = "789"
numero_04 = "132"

# COMPLETAR - INICIO
x1= int(numero_01)
x2=int(numero_02)
x3=int(numero_03)
x4=int(numero_04)
suma_de_numeros=x1+x2+x3+x4

# COMPLETAR - FIN

assert suma_de_numeros == 1500


"""
Convertir los numeros de enteros a string y luego concatenarlos.
"""

numero_01 = 123
numero_02 = 456
numero_03 = 789

# COMPLETAR - INICIO
e1= str(numero_01)
e2=str(numero_02)
e3=str(numero_03)
suma_de_numeros_string= f"{e1}{e2}{e3}"


# COMPLETAR - FIN

assert suma_de_numeros_string == "123456789"


"""
Convertir los numeros de binario, octal y hexadecimal a enteros y luego
multiplicarlos.
"""

numero_binario = "0b111010110101110111101000000"
numero_octal = "0o1425"
numero_hexadecimal = "0x6f540"

# COMPLETAR - INICIO
entero1= int(numero_binario,2)
entero2= int(numero_octal, 8)
entero3= int(numero_hexadecimal,16)
multiplicacion_de_numeros= entero1*entero2*entero3
# COMPLETAR - FIN

assert multiplicacion_de_numeros == 44397345600000000


"""
Convertir todo los numeros a enteros y luego restarlos secuencialmente (El uno
menos el dos menos el tres menos el cuatro).
"""

numero_01 = "987"
numero_02 = "0x6f54F"
numero_03 = "0o1234"
numero_04 = 654

# COMPLETAR - INICIO
ent1= int(numero_01)
ent2= int(numero_02, 16)
ent3=int(numero_03, 8)
resultado_resta= ent1-ent2-ent3-numero_04



# COMPLETAR - FIN

assert resultado_resta == -456350