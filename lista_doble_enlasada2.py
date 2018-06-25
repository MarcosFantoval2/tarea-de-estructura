from contacto import *


class lista_ordenada:
	def __init__(self):
		self.head = None

	def esVacia(self):										#REVISA SI LA LISTA ESTA VACIA
		if self.head == None:
			return True
		else:
			return False

	def agregar(self, nombre, apellido, telefono, mail):	#INSERTAR CONTACTO
		aux = self.head
		prev = None
		stop = False
		while aux != None and not stop:
		    if aux.getApellido() > apellido:
		        stop = True
		    else:
		        prev = aux
		        aux = aux.getNext()

		nuevo = contacto(nombre,apellido,telefono,mail)		#SE CREA EL CONTACTO

		if prev == None:
		    nuevo.setNext(self.head)
		    self.head = nuevo
		else:
		    nuevo.setNext(aux)
		    prev.setNext(nuevo)

	def buscar(self,dato):									#BUSCAR CONTACTO, ENTREGA EL CONTACTO O UN None EN CASO CONTRARIO
		aux = self.head
		while aux:
			if aux.getNombre() == dato or aux.getApellido() == dato or aux.getTelefono() == dato or aux.getMail() == dato:
				return aux
			else:
				aux = aux.getNext()
		return None

	def eliminar(self,dato):								#ELIMINA UN CONTACTO POR DATO
		aux = self.head
		prev = None
		while aux:
			if aux.getNombre() == dato or aux.getApellido() == dato or aux.getTelefono() == dato or aux.getMail() == dato:
				if aux == self.head:
					self.head = aux.getNext()
				else:
					prev.setNext(aux.getNext())
			else:
				prev = aux
				aux = aux.getNext()

	def imprimir(self):
		aux = self.head
		while aux:
			print(aux.getNombre())
			print(aux.getApellido())
			print(aux.getTelefono())
			print(aux.getMail())
			aux = aux.getNext()
print("hola putosssss")


