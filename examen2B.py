#1) Como dividir una columna de texto en dos columnas separadas
# Entrada
import pandas as pd
import numpy as np

df =pd.DataFrame(["STD,City State",
	"33,Kolkata West_Bengal",
	"44,Chennai Tamil_Nadu",
	"40,Hyderabad Telengana",
	"80,Bangalore Karnataka"],columns=['row'])
# print(df['row'])

s1=df['row'].str.split(',')
s3=[]
s2=[]
for rows in s1:
	s3.append(rows[0])
	s2.append(rows[1].split(' '))
df1 = pd.DataFrame(s2[1:], columns =s2[0])
df1[s3[0]]=s3[1:]
print ("\n P1")
print(df1)


# 2) Cómo obtener la frecuencia de valores repetidos en tod0 el dataframe

df2 = pd.DataFrame(np.random.randint(1,10,20).reshape(-1,4),columns=list('abcd'))
print ("\n P2")
print (df2)

print(df2.groupby('a').count())
print(df2.groupby('b').count())
print(df2.groupby('c').count())
print(df2.groupby('d').count())

# 3 ¿Cómo obtener las posiciones donde coinciden los valores de dos columnas?
df3 =pd.DataFrame({'fruit1':np.random.choice(['apple','orange','banana'],10),
				   'fruit2':np.random.choice(['apple','orange','banana'],10)})
print ("\n P3")
print (df3)

# 4) A partir de un diccionario crear un DataFrame
df4 = pd.DataFrame.from_dict({'X':[28,35,46,50,66], 'Y':[74,84,99,13,26],'Z':[36,47,56,62,73]})
print("\n P4")
print(df4)

# 5) Genere 3 columnas con 5 elementos cada uno. Cree una función para eliminar los N primeras o N últimas filas

df5 = pd.DataFrame(np.random.randint(1,10,15).reshape(-1,3),columns=list('ABC'))
print("\n P5")
print(df5)

def func5(a:int, b:int):
	return null

# 6) Genere 5 columnas con 5 elementos cada uno.
# Cree una función para ordenar de forma ascendente o descendente los datos por columna.

df6 = pd.DataFrame(np.random.randint(1, 10, 25).reshape(-1, 5), columns=list('ABCDE'))
print("\n P6")
print(df6)

def func6(condicion): #recibe true para ascendente y false para descendente
	print(df6.sort_values('A',ascending=condicion))

func6(True)

# 7) Genere 4 columnas con 5 elementos cada uno.
# Cree una función para obtener los N primeros o N ultimos registros.

df7 = pd.DataFrame(np.random.randint(1, 10, 20).reshape(-1, 4), columns=list('ABCD'))
print("\n P7")
print(df7)

def func7(n, condicion): #recibe true para los pirmeros y false para los ultimos
	if(condicion == True):
		print(df7[:n])
	else:
		print(df7[n+1:])
func7(2,True)

# 8) Genere 4 columnas con 5 elementos cada uno.
# Cree una función para obtener los N primeros o N ultimos registros.

df8 = pd.DataFrame(np.random.randint(1, 10, 20).reshape(-1, 4), columns=list('ABCD'))
print("\n P8")
print(df8)

def func8(n, condicion): #recibe true para los pirmeros y false para los ultimos
	if(condicion == True):
		print(df8[:n])
	else:
		print(df8[n+1:])
func8(2,True)

# 9) Genere 6 columnas con 5 elementos cada uno.
# Cree una función para obtener un nuevo DataFrame sin la columna X.

df9 = pd.DataFrame(np.random.randint(1, 10, 30).reshape(-1, 6), columns=list('ABCDEF'))
print("\n P9")
print(df9)

def func9(n): #recibe true para los pirmeros y false para los ultimos
	print(df9.drop(n,1))

func9('C')

# 10) Genere 3 columnas con 5 elementos cada uno.
# Cree una función para obtener el numero de columnas en un dataframe

df10 = pd.DataFrame(np.random.randint(1, 10, 15).reshape(-1, 3), columns=list('ABC'))
print("\n P10")
print(df10)

def func10(df):
	return df.shape[1]

print("Num de cols = " + str(func10(df10)))

# Genere 2 columnas con 20 elementos cada uno.
# La primera columna debe de tener uno de los siguientes valores: C1, C2, C3 y C4. Estos valores se pueden repetir.
# La segunda columna tiene valores de números cualesquiera.
# Cree una función para agrupar por la Primera Columna y que se listenlos valores agrupados de la segunda Columna.

col1 = ['C1','C1','C3','C1''C1','C1','C3','C1''C1','C2','C2','C4''C1','C2','C2','C4''C1','C2','C2','C4']

df11 = pd.DataFrame(np.random.randint(1, 10, 20).reshape(-1, 1), columns=['col2'])
df11['col1']=col1[0]
print("\n P11")

print(df11.groupby('col1'))
