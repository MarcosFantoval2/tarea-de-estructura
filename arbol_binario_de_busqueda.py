import os
from contacto import *
from lista_ordenada import lista_ordenada

class arbol_binario_de_busqueda():
    def __init__(self):
        self.root = None
        
    def insertar_aux(self, a, nombre, apellido, telefono, mail):
        if apellido < a.getApellido():
            if a.getLeft() == None:
                a.setLeft(contacto(nombre,apellido,telefono,mail)) 
                return   
            self.insertar_aux(a.getLeft(),nombre,apellido,telefono,mail)
        else:
            if a.getRight() == None:
                a.setRight(contacto(nombre,apellido,telefono,mail))
                return
            self.insertar_aux(a.getRight(), nombre,apellido,telefono,mail)

    def insertar(self,nombre,apellido,telefono,mail):                #INSERTAR UN ELEMENTO
        if self.root == None:
            self.root = contacto(nombre,apellido,telefono,mail)
        self.insertar_aux(self.root,nombre,apellido,telefono,mail)

    def inorder_aux(self, aux):                                      #IMPRIMIR DE MENOR A MAYOR
        if aux == None:
            return None
        else:
            self.inorder_aux(aux.getLeft())
            print(aux.getApellido())
            self.inorder_aux(aux.getRight())

    def inorder(self):
        self.inorder_aux(self.root)

    def buscar_aux(self, a, dato):
        if a == None:
            return None
        else:
            if dato == a.getNombre() or dato == a.getApellido() or dato == a.getTelefono() or dato == a.getMail():
                return True
            else:
                self.buscar_aux(a.left,dato)
                self.buscar_aux(a.right,dato)

    def buscar(self,dato):                                           #BUSCAR UN ELEMENTO POR DATO
        if self.buscar_aux(self.root,dato):
            return True
        return False

    def insertar_rama(self, a):
        if a != None:
            self.insertar_rama(a.getLeft())
            self.insertar(a.getNombre(),a.getApellido(),a.getTelefono(),a.getMail())
            self.insertar_rama(a.getRight())

    def eliminar_aux(self, a, dato, cadena):
        if a == None:
            return None
        else:
            self.eliminar_aux(a.getRight(),dato,cadena)
            cadena.agregar(a.getNombre(),a.getApellido(),a.getTelefono(),a.getMail())
            self.eliminar_aux(a.getLeft(),dato,cadena)

    def eliminarse(self,dato):
        cadena = lista_ordenada()
        self.eliminar_aux(self.root, dato, cadena)
        cadena.eliminar(dato)
        print("hola")
        self.root = None
        aux = cadena.getHead()
        while aux != None:
            print (aux.getTelefono())
            self.insertar(aux.getNombre(),aux.getApellido(),aux.getTelefono(),aux.getMail())
            aux = aux.getNext()
            



temp = arbol_binario_de_busqueda()
temp.insertar(1,2,3,4)
temp.insertar(2,4,5,7)
temp.insertar(3,1,3,4)
temp.insertar(4,7,5,4)
temp.insertar(5,5,3,4)
temp.insertar(6,8,3,4)

temp.inorder()

temp.buscar(8)

temp.eliminarse(2)
temp.eliminarse(3)


temp.buscar(8)