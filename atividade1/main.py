from DynamicIntArray import DynamicIntArray

lista = DynamicIntArray()


# Saída: Lista vazia!
if lista.is_empty():
    print("Lista vazia!")
else:
    print("Lista tem elementos.")
print()


print("Adicionando o 10;")
lista.append(10)
#Saída: Lista:  [10] 
print("Lista: ", lista)
print()


print("Verificando se 0 existe;")
#Saída: "0 existe na lista? Não" 
print("0 existe na lista? ", "Sim" if lista.contains(0) else "Não")
print()


print("Adicionando o 20;")
lista.append(20)
#Saída: Lista:  [10, 20] 
print("Lista: ", lista)
print()


print("Verificando o index do 20;")
#Saída: "Index do 20 é: 1" 
print("Index do 20 é: ", lista.index_of(20))
print()


print("Verificando se 20 existe;")
#Saída: "20 existe na lista? Sim" 
print("20 existe na lista? ", "Sim" if lista.contains(20) else "Não")
print()


print("Adicionando o 30;")
lista.append(30)
print("Lista: ", lista)
print()


print("Tamanho da Lista para o usuário: ", lista.size)
print()


print("Tamanho real da Lista internamente: ", lista.capacity)
print()


print("Adicionando o 40;")
lista.append(40)
print("Lista: ", lista)
print()


print("Adicionando o 50;")
lista.append(50)
# Saída: [10, 20, 30, 40, 50]   
print("Lista: ", lista)      
print()  


# Buscar Elemento no índice 2 
# Saída: 30  
print("Elemento na posição 2: ", lista.get(2))    
print()


# Trocar Elemento no índice 2 para 99
# Saída: [10, 20, 99, 40, 50]
print("Trocando elemento no índice 2 para 99.")  
lista.set(2, 99)
print("Lista: ", lista)      
print()


# Remover Elemento 40 se existir 
# Saída: [10, 20, 99, 50]
print("Removendo elemento 40 se existir.")
lista.remove(40)
print("Lista: ", lista)
print()


print("Removendo elemento no indice 1 se existir.")
# Saída: [10, 99, 50]
lista.remove_at(1)
print("Lista: ", lista)
print()


print("Removendo mais um elementos no indice 2.")
# Saída: Redimensionando de 8 para 4
# Saída: [10, 99]
lista.remove_at(2)
print("Lista: ", lista)
print()


print("Removendo mais um elementos no indice 0.")
# Saída: Redimensionando de 4 para 2
# Saída: [10]
#Essa saída está incorreta, pois o valor no index 0 é o 10, então a saída é [99]
lista.remove_at(0)
print("Lista: ", lista)
print()