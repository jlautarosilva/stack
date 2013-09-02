class Pila(object):
    def __init__(self):
        self.elementos = None

    def apilar(self, elemento):
	self.elementos = Nodo(elemento, self.elementos)

    def desapilar(self):
	aux = self.elementos.elemento
	self.elementos = self.elementos.next
	return aux

    def cima(self):
	return self.elementos.elemento

    def __len__(self):
	i=0
	aux = self.elementos
	while aux:
	    i += 1
	    aux = aux.next
	return i

class Nodo:
    def __init__(self, elemento=None, next=None):
        self.elemento = elemento
        self.next = next

if __name__ =='__main__':
    p = Pila()
    for i in range(10):p.push(i)
    for i in range(len(p)):print(p.pop())
