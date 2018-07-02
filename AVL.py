from contacto import *

temp = contacto(1,2,3,4)
temp.getApellido()

class arbol_avl():
    def __init__(self):
        self.root = None 
        self.altura = -1  
        self.balance = 0

    def getAltura(self):
        if self.root: 
            return self.root.altura
        else: 
            return 0 
    
    def es_hoja(self):
        return (self.altura == 0) 
    
    def insertar(self, nombre, apellido, telefono, mail):                   #INSERTAR
        tree = self.root

        new_contacto = contacto(nombre,apellido,telefono,mail)
        
        if tree == None:
            self.root = new_contacto 
            self.root.left = arbol_avl() 
            self.root.right = arbol_avl()
        
            
        elif apellido > tree.getApellido(): 
            self.root.right.insertar(nombre,apellido,telefono,mail)
            
        else: 
            self.root.left.insertar(nombre,apellido,telefono,mail)
        self.rebalancear() 
        
    def rebalancear(self):
        self.update_alturas(False)
        self.update_balances(False)
        while self.balance < -1 or self.balance > 1: 
            if self.balance > 1:
                if self.root.left.balance < 0:  
                    self.root.left.left_rotate()
                    self.update_alturas()
                    self.update_balances()
                self.right_rotate()
                self.update_alturas()
                self.update_balances()
                
            if self.balance < -1:
                if self.root.right.balance > 0:  
                    self.root.right.right_rotate()
                    self.update_alturas()
                    self.update_balances()
                self.left_rotate()
                self.update_alturas()
                self.update_balances()


            
    def right_rotate(self): 
        base = self.root 
        izq = self.root.left.root 
        der = izq.right.root 
        self.root = izq 
        izq.right.root = base
        base.left.root = der 

    
    def left_rotate(self):
        base = self.root 
        der = self.root.right.root 
        izq = der.left.root 
        self.root = der 
        der.left.root = base 
        base.right.root = izq 
        
            
    def update_alturas(self, recurse=True):
        if not self.root == None: 
            if recurse: 
                if self.root.left != None: 
                    self.root.left.update_alturas()
                if self.root.right != None:
                    self.root.right.update_alturas()
            
            self.altura = max(self.root.left.altura,
                              self.root.right.altura) + 1 
        else: 
            self.altura = -1 
            
    def update_balances(self, recurse=True):
        if not self.root == None: 
            if recurse: 
                if self.root.left != None: 
                    self.root.left.update_balances()
                if self.root.right != None:
                    self.root.right.update_balances()

            self.balance = self.root.left.altura - self.root.right.altura 
        else: 
            self.balance = 0 

    def eliminar(self, dato):                                                   #ELIMINAR POR APELLIDO
        if self.root != None: 
            if self.root.getApellido() == dato: 
                if self.root.left.root == None and self.root.right.root == None: #ELIMINAR HOJAS 
                    self.root = None  
                elif self.root.left.root == None: 
                    self.root = self.root.right.root
                elif self.root.right.root == None: 
                    self.root = self.root.left.root
                else:  
                    replacement = self.sucesor(self.root)
                    if replacement != None:
                        self.root.setApellido(replacement.apellido)  
                        self.root.right.eliminar(replacement.apellido)              
                self.rebalancear()
                return  
            elif dato <= self.root.getApellido(): 
                self.root.left.eliminar(dato)  
            elif dato > self.root.getApellido(): 
                self.root.right.eliminar(dato)
                        
            self.rebalancear()
        else: 
            return 
    
    def sucesor(self, aux):
        aux = aux.right.root  
        if aux != None:
            while aux.left != None:
                if aux.left.root == None: 
                    return aux 
                else: 
                    aux = aux.left.root  
        return aux 

    def imprimir(self):                                                            #IMPRIMIR
        self.update_alturas()
        self.update_balances()
        if(self.root != None): 
            self.root.left.imprimir()
            print (self.root.getApellido())  
            self.root.right.imprimir()

    def buscar(self,dato):                                                          #BUSCAR
        if(self.root != None):
            if self.root.apellido == dato:
                print(True)
                return True
            self.root.left.buscar(dato)
            self.root.right.buscar(dato)
        return

temp = arbol_avl()
 
temp.insertar(1,2,3,4)
temp.insertar(2,3,3,4)
temp.insertar(3,6,3,4)
temp.insertar(4,8,3,4)
temp.insertar(5,1,3,4)
temp.insertar(1,2,3,4)
temp.insertar(2,4,5,7)
temp.insertar(3,1,3,4)
temp.insertar(4,7,5,4)
temp.insertar(5,5,3,4)
temp.insertar(6,8,3,4)

temp.imprimir()

print("----------------------")

temp.buscar(8)

temp.eliminar(8)
temp.eliminar(4)
temp.eliminar(5)
temp.eliminar(3)

print("----------------------")

temp.imprimir()