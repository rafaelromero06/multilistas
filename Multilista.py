class Node:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.next = None
        self.prev = None
        self.sub_list = None

    def __repr__(self):
        return f"{self.tipo}: {self.nombre}"


class Multilista:
    def __init__(self):
        self.primero = None

    def insertar(self, nombre, tipo):
        nuevo = Node(nombre, tipo)
        if not self.primero:
            self.primero = nuevo
        else:
            actual = self.primero
            while actual.next:
                actual = actual.next
            actual.next = nuevo
        return nuevo

    def buscar(self, nombre):
        actual = self.primero
        while actual:
            if actual.nombre == nombre:
                return actual
            actual = actual.next
        return None

    def mostrar(self, nivel=0):
        actual = self.primero
        while actual:
            print("   " * nivel + f"├── {actual.tipo}: {actual.nombre}")
            if actual.sub_list:
                actual.sub_list.mostrar(nivel + 1)
            actual = actual.next