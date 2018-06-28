from contacto import *

def hash_function(llave_str, size):
    return sum([ord(c) for c in llave_str]) % size

class tabla_hash:
    def __init__(self, capacidad=1000):
        self.capacidad = capacidad
        self.size = 0
        self._llaves = []
        self.data = [[] for _ in range(capacidad)]

    def encontrar_por_llave(self, llave, find_result_func):
        index = hash_function(llave, self.capacidad)
        hash_table_cell = self.data[index]
        encontrado = None
        for item in hash_table_cell:
            if item[0] == llave:
                encontrado = item
                break
        return find_result_func(encontrado, hash_table_cell)

    def set(self, llave, obj):
        def find_result_func(encontrado, hash_table_cell):
            if encontrado:
                encontrado[1] = obj
            else:
                hash_table_cell.append([llave, obj])
                self.size += 1
                self._llaves.append(llave)

        self.encontrar_por_llave(llave, find_result_func)
        return self

    def get(self, llave):
        def find_result_func(encontrado, _):
            if encontrado:
                return encontrado[1]
            else:
                print("error")

        return self.encontrar_por_llave(llave, find_result_func)

    def remove(self, llave):
        def find_result_func(encontrado, hash_table_cell):
            if encontrado:
                hash_table_cell.remove(encontrado)
                self._llaves.remove(llave)
                self.size -= 1
                return encontrado[1]
            else:
                print("error")

        return self.encontrar_por_llave(llave, find_result_func)

    def llaves(self):
        return self._llaves

    def __setitem__(self, llave, value):
        self.set(llave, value)

    def __getitem__(self, llave):
        return self.get(llave)

class hash_contactos:
	def __init__(self, capacidad):
		self.tabla = tabla_hash(capacidad)

	def agregar(self, nombre, apellido, telefono, mail):					#AGREGAR ELEMENTOS
		self.tabla[apellido] = contacto( nombre, apellido, telefono, mail)

	def eliminar(self,apellido):											#ELIMINAR
		self.tabla.remove(apellido)

	def buscar(self,apellido):												#BUSCAR
		return self.tabla[apellido]

if __name__ == "__main__":
	temp = hash_contactos(30)
	temp.agregar("a","a",123123,"hola@gogel.com")
	temp.agregar("b","b",123123,"hola@gogel.com")
	temp.agregar("c","c",123123,"hola@gogel.com")
	temp.agregar("d","d",123123,"hola@gogel.com")

	print(temp.buscar("b").getNombre())

	temp.eliminar("b")

	print(temp.buscar("b"))