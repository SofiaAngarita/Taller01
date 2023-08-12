def mostrar_menu():
  print("Bienvenido a la calculadora en Python")
  print("Por favor, elija una opción:")
  print("1. Sumar dos números")
  print("2. Restar dos números")
  print("3. Multiplicar dos números")
  print("4. Dividir dos números")
  print("5. Salir del programa")

  # Definir una variable para controlar el bucle
continuar = True

# Iniciar el bucle
while continuar:
  # Mostrar el menú
  mostrar_menu()
  # Pedir al usuario que ingrese una opción
  opcion = input("Ingrese su opción: ")
  # Verificar si la opción es válida
  if opcion in ["1", "2", "3", "4"]:
    # Pedir al usuario que ingrese dos números
    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: ")) 
  if opcion == "1":
# Sumar los números
    resultado = num1 + num2
# Mostrar el resultado
    print(f"La suma de {num1} y {num2} es {resultado}")

  elif opcion == "2":
# Restar los números
    resultado = num1 - num2
# Mostrar el resultado
    print(f"La resta de {num1} y {num2} es {resultado}")

  elif opcion == "3":
# Multiplicar los números
    resultado = num1 * num2
# Mostrar el resultado
    print(f"La multiplicación de {num1} y {num2} es {resultado}")
  else:
# Dividir los números
# Verificar si el segundo número es cero
    if num2 == 0:
# Mostrar un mensaje de error
      print("No se puede dividir por cero")
    else:
# Calcular el resultado
      resultado = num1 / num2
# Mostrar el resultado
      print(f"La división de {num1} y {num2} es {resultado}")
      