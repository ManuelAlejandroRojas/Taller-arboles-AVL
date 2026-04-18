import sys 

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.height = 1 


def getHeight(node):
    if not node:
        return 0
    return node.height

def getBalance(node):
    if not node:
        return 0
    return getHeight(node.left) - getHeight(node.right)

def updateHeight(node):
    if node:
        node.height = 1 + max(getHeight(node.left), getHeight(node.right))

def rotate_right(y):
    x = y.left
    T2 = x.right

    x.right = y
    y.left = T2

    updateHeight(y)
    updateHeight(x)

    return x

def rotate_left(x):
    y = x.right
    T2 = y.left

    y.left = x
    x.right = T2

    updateHeight(x)
    updateHeight(y)

    return y

class AVLTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        self.root = self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if not node:
            return Node(value)

        if value < node.value:
            node.left = self._insert_recursive(node.left, value)
        elif value > node.value:
            node.right = self._insert_recursive(node.right, value)
        else:
            return node 
        
        updateHeight(node)
        
        balance = getBalance(node)

        if balance > 1 and getBalance(node.left) >= 0:
             return rotate_right(node) 
        
        elif balance > 1 and getBalance(node.left) < 0:
            node.left = rotate_left(node.left)
            return rotate_right(node) 
        
        elif balance < -1 and getBalance(node.right) <= 0:
            return rotate_left(node)
        
        elif balance < -1 and getBalance(node.right) > 0:
            node.right = rotate_right(node.right)
            return rotate_left(node) 
        
        return node 

    def Obtener_Minimo_Total(self, node):
        N_actual = node

#Busco la izquierda izquierda
        while N_actual.left:
            N_actual = N_actual.izquierda

#Le devuelvo a la funcion que la use el nodo izquierdo total
        return N_actual


#Funcion principal que elimina un nodo, recibe el valor a eliminar
    def Eliminar_Nodo(self, valor):
        self.root = self.Eliminar_Nodo_recursiva(self.root, valor)  #La raiz se actualiza 


    def Eliminar_Nodo_recursiva(self, node, valor):
        #En caso de que no haya nodo
        if not node:
            return None #Por si no lo encuentra, al llegar a un nodo vacío, no hace nada y devuelve None
        

        #ahora, si el valor a eliminar es menor que el nodo actual, busco en la izquierda de manera recursiva, y si es mayor, busco en la derecha de manera recursiva
        if valor < node.value:
            node.left = self._Eliminar_Nodo_recursiva(node.left, valor)     #Aqui buscamos infinitamente hacia la izquierda cuando sea necesario
        elif valor > node.value:
            node.right = self._Eliminar_Nodo_recursiva(node.right, valor)   #Aqui buscamos infinitamente hacia la derecha cuando sea necesario
        else:
            
            #Cuando llegue al actual, se elimina el nodo

            #Si el nodo actual es un nodo con un solo hijo o sin hijos
            if not node.left:
                temporal = node.right
                node = None
                return temporal             #Aqui se elimina el nodo actual, y se devuelve el nodo derecho para que 
                                            #el padre del nodo actual apunte a ese nodo derecho, o None si no tiene hijo derecho
            
            elif not node.right:
                temporal = node.left
                node = None
                return temporal


            #En el caso de que tenga dos hijos, se obtiene el nodo con el valor mínimo del subárbol derecho, 
            # se copia su valor al nodo actual, y luego se elimina ese nodo mínimo del subárbol dereccho

            temporal = self.Obtener_Minimo_Total(node.right) #Obtengo el nodo con el valor mínimo del subárbol derecho
            node.value = temporal.value #Copio su valor al nodo actual
            node.right = self.Eliminar_Nodo_recursiva(node.right, temporal.value) #Elimino el nodo mínimo del subárbol derecho

            #Despues de elminar, las alturas cambian
            updateHeight(node)

            #Y se balancea el nodo actual
            balance = getBalance(node)

            #Uso las mismas condiciones de balanceo que al insertar, pero con el nodo actual después de eliminar
            if balance > 1 and getBalance(node.left) >= 0:
                return rotate_right(node)
            
            elif balance > 1 and getBalance(node.left) < 0:
                node.left = rotate_left(node.left)
                return rotate_right(node)
            
            elif balance < -1 and getBalance(node.right) <= 0:
                return rotate_left(node)
            
            elif balance < -1 and getBalance(node.right) > 0:
                node.right = rotate_right(node.right)
                return rotate_left(node)
            
        return node #Devuelvo el nodo actualizado después de eliminar y balancear, para que el padre del nodo actual apunte a este nodo actualizado
    

    #Agrego una funcion para leer el inorden y retornar en orden ascendente
    def leer_inorden(self, node, resultado):
        if not node:
            return
        
        #Me recomendaron usar una lista para guardar los resultados
        #Asi que hago una lista resultado, y voy agregando los valores en orden ascendente

        #RECORDAR: Izquierda -> Nodo -> Derecha
        inicio = self.Obtener_Minimo_Total(node) #Obtengo el nodo con el valor mínimo del subárbol actual
    

avl = AVLTree()
values_to_insert = [10, 20, 30, 40, 50, 25]

print("Insertando valores:", values_to_insert)
for val in values_to_insert:
    avl.insert(val)

print("\n--- Despues de inserciones ---")
