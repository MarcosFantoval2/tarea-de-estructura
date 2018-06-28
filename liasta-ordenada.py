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
		if self.head == None:
			return

		aux = self.head
		prev = aux

		if aux.getApellido() == dato:
			self.head = aux.getNext()

		while aux != None:
			if aux.getApellido() == dato:
				prev.setNext(aux.getNext())
				return
			else:
				prev = aux
				aux = aux.getNext()

	def imprimir(self):
		aux = self.head
		while aux:
			aux.mostrar()
			aux = aux.getNext()
	def getHead(self):
		return self.head

# temp = lista_ordenada()
# temp.agregar("a","a",123123,"hola@gogel.com")
# temp.agregar("b","b",123123,"hola@gogel.com")
# temp.agregar("c","c",123123,"hola@gogel.com")
# temp.agregar("d","d",123123,"hola@gogel.com")
# temp.imprimir()
# temp.eliminar("c")
# print("---------------")
# temp.imprimir()