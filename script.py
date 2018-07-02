from lista_ordenada import lista_ordenada 
from arbol_binario_de_busqueda import arbol_binario_de_busqueda
from AVL import arbol_avl 
from hash2 import hash_contactos
import random
from time import time


if __name__ == '__main__':
	opcion = 0
	while opcion != 6:
		print("Escoger una estructura:")
		print("1.- lista ordenada")
		print("2.- arbol binario de busqueda")
		print("3.- avl")
		print("4.- arbol 2-3")
		print("5.- hash_table")
		print("6.- salir")
		opcion = input()

		random.seed()

		if opcion == 1:
			print("cuantos contactos?")
			tam =input()
			temp = lista_ordenada()
			resp = 1
			while resp != 5:
				print("-----Seleccionar una accion: ")
				print("-----1.- insertar")
				print("-----2.- eliminar")
				print("-----3.- buscar")
				print("-----4.- imprimir")
				print("-----5.- salir")

				resp = input()

				if resp == 1:
					start_time = time()										#INICIO DEL TIEMPO
					for x in range(1,tam):
						temp.agregar(x+1,x+1,123123123,"nombre@mail.cl")
					elapsed_time = time() - start_time 						#TERMINO DEL TIEMPO
					
					print("-------------------------------")
					print("tiempo de ejecucion: ")
					print(elapsed_time)		
					print("-------------------------------")
				elif resp == 2:
					print("cual desea eliminar?")
					eliminado = input()

					start_time = time()										#INICIO DEL TIEMPO
					temp.eliminar(eliminado)
					elapsed_time = time() - start_time 						#TERMINO DEL TIEMPO
					
					print("-------------------------------")
					print("tiempo de ejecucion: ")
					print(elapsed_time)		
					print("-------------------------------")
				elif resp == 3:
					print("cual desea buscar?")
					buscado = input()

					start_time = time()										#INICIO DEL TIEMPO
					print(temp.buscar(buscado))
					elapsed_time = time() - start_time 						#TERMINO DEL TIEMPO
					
					print("-------------------------------")
					print("tiempo de ejecucion: ")
					print(elapsed_time)		
					print("-------------------------------")
				elif resp == 4:
					start_time = time()										#INICIO DEL TIEMPO
					temp.imprimir()
					elapsed_time = time() - start_time 						#TERMINO DEL TIEMPO
					
					print("-------------------------------")
					print("tiempo de ejecucion: ")
					print(elapsed_time)		
					print("-------------------------------")
				elif resp == 5:
					print("saliendo...")
				else:
					print("ingresar opcion valida")


		elif opcion == 2:
			print("cuantos contactos?")
			tam =input()
			temp = arbol_binario_de_busqueda()

			resp = 1
			while resp != 5:
				print("-----Seleccionar una accion: ")
				print("-----1.- insertar")
				print("-----2.- eliminar")
				print("-----3.- buscar")
				print("-----4.- imprimir")
				print("-----5.- salir")

				resp = input()

				if resp == 1:
					start_time = time()										#INICIO DEL TIEMPO
					for x in range(1,tam):
						temp.insertar(x+1,x+1,123123123,"nombre@mail.cl")
					elapsed_time = time() - start_time 						#TERMINO DEL TIEMPO
					
					print("-------------------------------")
					print("tiempo de ejecucion: ")
					print(elapsed_time)		
					print("-------------------------------")
				elif resp == 2:
					print("cual desea eliminar?")
					eliminado = input()

					start_time = time()										#INICIO DEL TIEMPO
					temp.eliminarse(eliminado)
					elapsed_time = time() - start_time 						#TERMINO DEL TIEMPO
					
					print("-------------------------------")
					print("tiempo de ejecucion: ")
					print(elapsed_time)		
					print("-------------------------------")
				elif resp == 3:
					print("cual desea buscar?")
					buscado = input()

					start_time = time()										#INICIO DEL TIEMPO
					print(temp.buscar(buscado))
					elapsed_time = time() - start_time 						#TERMINO DEL TIEMPO
					
					print("-------------------------------")
					print("tiempo de ejecucion: ")
					print(elapsed_time)		
					print("-------------------------------")
				elif resp == 4:
					start_time = time()										#INICIO DEL TIEMPO
					temp.inorder()
					elapsed_time = time() - start_time 						#TERMINO DEL TIEMPO
					
					print("-------------------------------")
					print("tiempo de ejecucion: ")
					print(elapsed_time)		
					print("-------------------------------")
				elif resp == 5:
					print("saliendo...")
				else:
					print("ingresar opcion valida")

		elif opcion == 3:
			print("cuantos contactos?")
			tam =input()
			temp = arbol_avl()

			resp = 1
			while resp != 5:
				print("-----Seleccionar una accion: ")
				print("-----1.- insertar")
				print("-----2.- eliminar")
				print("-----3.- buscar")
				print("-----4.- imprimir")
				print("-----5.- salir")

				resp = input()

				if resp == 1:
					start_time = time()										#INICIO DEL TIEMPO
					for x in range(1,tam):
						temp.insertar(x+1,x+1,123123123,"nombre@mail.cl")
					elapsed_time = time() - start_time 						#TERMINO DEL TIEMPO
					
					print("-------------------------------")
					print("tiempo de ejecucion: ")
					print(elapsed_time)		
					print("-------------------------------")
				elif resp == 2:
					print("cual desea eliminar?")
					eliminado = input()

					start_time = time()										#INICIO DEL TIEMPO
					temp.eliminar(eliminado)
					elapsed_time = time() - start_time 						#TERMINO DEL TIEMPO
					
					print("-------------------------------")
					print("tiempo de ejecucion: ")
					print(elapsed_time)		
					print("-------------------------------")
				elif resp == 3:
					print("cual desea buscar?")
					buscado = input()

					start_time = time()										#INICIO DEL TIEMPO
					print(temp.buscar(buscado))
					elapsed_time = time() - start_time 						#TERMINO DEL TIEMPO
					
					print("-------------------------------")
					print("tiempo de ejecucion: ")
					print(elapsed_time)		
					print("-------------------------------")
				elif resp == 4:
					start_time = time()										#INICIO DEL TIEMPO
					temp.imprimir()
					elapsed_time = time() - start_time 						#TERMINO DEL TIEMPO
					
					print("-------------------------------")
					print("tiempo de ejecucion: ")
					print(elapsed_time)		
					print("-------------------------------")
				elif resp == 5:
					print("saliendo...")
				else:
					print("ingresar opcion valida")
		elif opcion == 4:
			print("opcion no lograda")
	

		elif opcion == 5:
			print("cuantos contactos?")
			tam = input()
			temp = hash_contactos(tam)

			resp = 1
			while resp != 5:
				print("-----Seleccionar una accion: ")
				print("-----1.- insertar")
				print("-----2.- eliminar")
				print("-----3.- buscar")
				print("-----4.- imprimir")
				print("-----5.- salir")

				resp = input()

				if resp == 1:
					start_time = time()										#INICIO DEL TIEMPO
					for x in range(1,tam):
						aux = str(x+1)
						print(aux)
						temp.agregar(x+1,aux,123123123,"nombre@mail.cl")
					elapsed_time = time() - start_time 						#TERMINO DEL TIEMPO
					
					print("-------------------------------")
					print("tiempo de ejecucion: ")
					print(elapsed_time)		
					print("-------------------------------")
				elif resp == 2:
					print("cual desea eliminar? (insertar el nombre entre comillas simples)")
					eliminado = input()

					start_time = time()										#INICIO DEL TIEMPO
					temp.eliminar(eliminado)
					elapsed_time = time() - start_time 						#TERMINO DEL TIEMPO
					
					print("-------------------------------")
					print("tiempo de ejecucion: ")
					print(elapsed_time)		
					print("-------------------------------")
				elif resp == 3:
					print("cual desea buscar? (insertar el nombre entre comillas simples)")
					buscado = input()

					start_time = time()										#INICIO DEL TIEMPO
					if temp.buscar(buscado):
						print (temp.buscar(buscado).apellido)
					elapsed_time = time() - start_time 						#TERMINO DEL TIEMPO
					
					print("-------------------------------")
					print("tiempo de ejecucion: ")
					print(elapsed_time)		
					print("-------------------------------")
				elif resp == 4:
					print("---------------------------------------------------------------------------------------")
					print("no existe, hash impide que se conozcan las llaves para acceder a la informacion")
					print("---------------------------------------------------------------------------------------")
				elif resp == 5:
					print("saliendo...")
				else:
					print("ingresar opcion valida")
		elif opcion == 6:
			print("-----")
			print("adios")
			print("-----")
		else:
			print("------------------------")
			print("introducir opcion valida")
			print("------------------------")
