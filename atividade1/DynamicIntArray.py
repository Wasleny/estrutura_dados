
# Implementação de Lista Dinâmica: 

# Complete o programa abaixo para que funcione a implementação de lista dinâmica.
# Foram adicionadas saídas esperadas que devem ser cumpridas como testes.

class DynamicIntArray:

    def __init__(self, capacity=2):
        if capacity <= 0:
            raise ValueError("Capacidade inicial deve ser maior que 0.")

        self.capacity = capacity        # Tamanho real do array interno
        self.size = 0                   # Quantos elementos o usuário colocou
        self.data = [0] * self.capacity # Cria Array estático interno (só de inteiros)

    # is_empty
    def is_empty(self):
        if self.size == 0:
            return 1
        
        return 0
    
    def position_exists(self, index):
        if 0 <= index < self.size:
            return 1
        
        print("Essa posição não existe no array")
        return 1


    # get (faça validação de index fora dos limites.)
    def get(self, index):
        if self.position_exists(index):
            return self.data[index]
        
        return

    # set (faça validação de index fora dos limites.)
    def set(self, index, value):
        if self.position_exists(index):
            self.data[index] = value
        
        return

    def append(self, value):
        if self.size == self.capacity:
            self._resize(2 * self.capacity, f"⏫ Redimensionando de {self.capacity} para {2 * self.capacity}")

        self.data[self.size] = value
        self.size += 1

    def _resize(self, new_capacity, message):
        print(f"{message}")

        new_data = [0] * new_capacity

        for i in range(self.size):
            new_data[i] = self.data[i]

        self.data = new_data
        self.capacity = new_capacity

    # remove_at 
    # remover elemento no index passado.
    # Reduzir a capacidade da Lista pela metade se 25% ou menos (<= 25%) do seu espaço estiver sendo usado
    # Exemplo, na lista de capacidade 8 com os seguintes valores [10, 99, 50],
    # ao remover um elemento sua capacidade deve cair de 8 para 4 e a lista ficar [10, 99] com capacidade 4. 
    # validar index fora dos limites.
    # retornar o valor removido.
    # Imprimir a seguinte mensagem quando for o caso: ⏬ Redimensionando de {self.capacity} para {new_capacity}
    def remove_at(self, index):
        value = -1
        if self.position_exists(index):
            value = self.data[index]

            for i in range(index, self.size - 1):
                self.data[i] = self.data[i + 1]
            
            self.data[self.size - 1] = 0
            self.size -= 1

            if self.size / self.capacity <= 0.25:
                self._resize(int(self.capacity / 2), f"⏬ Redimensionando de {self.capacity} para {int(self.capacity / 2)}")
        
        return value

    # remove
    # remove o elemento buscado caso exista.
    # mesmas regras do remove_at.
    def remove(self, value):
        for i in range(self.size):
            if self.data[i] == value:
                self.remove_at(i)
        
        return

    # insert_at
    # com os parametros de index e valor a ser inserido.
    # respeitando as regras de aumento da lista.
    def insert_at(self, index, value):
        if self.position_exists(index):
            if self.size == self.capacity:
                self._resize(2 * self.capacity, f"⏫ Redimensionando de {self.capacity} para {2 * self.capacity}")

            for i in range(self.size, index, -1):
                self.data[i] = self.data[i - 1]
            
            self.data[index] = value
            self.size += 1

        return

    # index_of
    # retorna o index do valor buscado ou -1 caso não exista.
    def index_of(self, value):
        for i in range(self.size):
            if self.data[i] == value:
                return i
        
        return -1

    # contains
    # retorna True ou False se encontrou ou não o valor buscado.
    def contains(self, value):
        for i in range(self.size):
            if self.data[i] == value:
                return True
        
        return False


    def __str__(self):

        return str(self.data[:self.size])
