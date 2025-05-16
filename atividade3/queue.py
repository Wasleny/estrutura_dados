from stack import Stack

class Queue:
    """
    Classe Queue (Fila) implementada sobre a Stack (Pilha).
    """
    def __init__(self):
        self.stack = Stack()
        self.aux = Stack()

    def enqueue(self, data):
        """
        Insere no final da fila.
        """

        self.aux.push(data)
        if self.aux.size() > 1:
            current = self.aux.singly_linked_list.top

            self.stack = Stack()

            while current is not None:
                self.stack.push(current.data)
                current = current.next
        else: 
            self.stack.push(data)
        
        return self.stack
    
    def dequeue(self):
        """
        Remover do início da fila.
        """

        self.stack.pop()
        current = self.stack.singly_linked_list.top
        self.aux = Stack()

        while current is not None:
            self.aux.push(current.data)
            current = current.next
        
        return self.aux
    
    def is_empty(self):
        """
        Verifica se a fila está vazia.
        """

        if self.stack.size() == 0:
            return True
        
        return False
    

fila = Queue()

print("Inserindo...")
fila.enqueue(1)
fila.enqueue(2)
fila.enqueue(3)
fila.enqueue(4)
fila.enqueue(5)
print(f"Fila após inserção:\n{fila.stack}")

print("Removendo...")
fila.dequeue()
fila.dequeue()
print(f"Fila após remoção:\n{fila.stack}")

print("Inserindo...")
fila.enqueue(6)
fila.enqueue(7)
print(f"Fila após inserção:\n{fila.stack}")

print("Removendo...")
fila.dequeue()
fila.dequeue()
print(f"Fila após remoção:\n{fila.stack}")

fila.dequeue()
fila.dequeue()
fila.dequeue()

print(fila.is_empty())