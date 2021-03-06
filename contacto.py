class contacto:
    def __init__(self, n_nombre, n_apellido, n_telefono, n_mail):
        self.nombre = n_nombre
        self.apellido = n_apellido
        self.telefono = n_telefono
        self.mail = n_mail
        self.next = None
        self.left = None
        self.right = None
 
    def getNombre(self):            #GETS DEL NODO
        return self.nombre
 
    def getApellido(self):
        return self.apellido
 
    def getTelefono(self):
        return self.telefono
 
    def getMail(self):
        return self.mail
 
    def getNext(self):
        return self.next

    def getLeft(self):
        return self.left 

    def getRight(self):
        return self.right
 
    def setNombre(self,dato):       #SETS DEL NODO
        self.nombre = dato
 
    def setApellido(self,dato):
        self.apellido = dato
 
    def setTelefono(self,dato):
        self.telefono = dato
 
    def setMail(self,dato):
        self.mail = dato
 
    def setNext(self,dato):
        self.next = dato

    def setLeft(self,dato):
        self.left = dato

    def setRight(self,dato):
        self.right = dato

    def setVacioIzq(self):
        self.left = None

    def setVacioDer(self):
        self.right = None

    def mostrar(self):
        print(self.nombre)
        print(self.apellido)
        print(self.telefono)
        print(self.mail)