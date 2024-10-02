print("")
print("Zamarripa Castro Erick Fabián")
print("")
#Crear Tupla 
thistuple = ("apple", "banana", "cherry")
print(thistuple)


#Tupla con miembros duplicados 
thistuple = ("apple", "banana", "cherry", "apple", "cherry")
print(thistuple)


#Contanto miembros de la tupla
thistuple = ("apple", "banana", "cherry")
print(len(thistuple))


#Notese la diferencia de cuando SI es Tupla y cuando NO lo es, revisa lo que muestra este pequeño código 
thistuple = ("apple",)
print(type(thistuple))


#NOT a tuple
thistuple = ("apple")
print(type(thistuple))


#Asignando tuplas a variables 
#tuple1 = ("apple", "banana", "cherry")tuple2 = (1, 5, 7, 9, 3)
tuple3 = (True, False, False)


#Combinando tipos de datos en mis tuplas
tuple1 = ("abc", 34, True, 40, "male")
print(tuple1)



#Tipo de datos de una tupla
mytuple = ("apple", "banana", "cherry")
print(type(mytuple))


#Utilizando el método tuple para hacer una 
thistuple = tuple(("apple", "banana", "cherry"))
print(thistuple)

# Definición de una tupla con tres frutas
thistuple = ("apple", "banana", "cherry")
# Imprime el segundo elemento de la tupla (índice 1)
print(thistuple[1])  # Salida: banana

# Re-definición de la tupla
thistuple = ("apple", "banana", "cherry")
# Imprime el último elemento de la tupla (índice -1)
print(thistuple[-1])  # Salida: cherry

# Re-definición de la tupla con más elementos
thistuple = ("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# Imprime los elementos desde el índice 2 al 4 (excluyendo el 5)
print(thistuple[2:5])  # Salida: ('cherry', 'orange', 'kiwi')

# Imprime los primeros cuatro elementos de la tupla
print(thistuple[:4])  # Salida: ('apple', 'banana', 'cherry', 'orange')

# Imprime desde el índice 2 hasta el final
print(thistuple[2:])  # Salida: ('cherry', 'orange', 'kiwi', 'melon', 'mango')

# Imprime los elementos desde el índice -4 hasta -1 (excluyendo el último)
print(thistuple[-4:-1])  # Salida: ('orange', 'kiwi', 'melon')

# Comprobar si 'apple' está en la tupla
thistuple = ("apple", "banana", "cherry")
if "apple" in thistuple:
    print("Yes, 'apple' is in the fruits tuple")  # Salida: Yes, 'apple' is in the fruits tuple

# Crear una tupla y convertirla a lista para modificar un elemento
x = ("apple", "banana", "cherry")
y = list(x)  # Convierte la tupla a lista
y[1] = "kiwi"  # Cambia el segundo elemento de la lista a 'kiwi'
x = tuple(y)  # Convierte de nuevo la lista a tupla

print(x)  # Salida: ('apple', 'kiwi', 'cherry')

# Agregar un nuevo elemento a la tupla
thistuple = ("apple", "banana", "cherry")
y = list(thistuple)  # Convierte la tupla a lista
y.append("orange")  # Agrega 'orange' a la lista
thistuple = tuple(y)  # Convierte de nuevo la lista a tupla

# Definición de una tupla con tres frutas y desestructuración
fruits = ("apple", "banana", "cherry")
(green, yellow, red) = fruits  # Asigna cada elemento de la tupla a variables

print(green)  # Salida: apple
print(yellow)  # Salida: banana
print(red)  # Salida: cherry

# Imprime cada elemento de la tupla usando un bucle
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
    print(thistuple[i])  # Salida: apple, banana, cherry
