class DynamicIntArray:
    def __init__(self, capacity=2):
        if capacity <= 0:
            raise ValueError("Capacidade inicial deve ser maior que 0.")
        self.capacity = capacity        # Tamanho real do array interno
        self.size = 0                   # Quantos elementos o usuário colocou
        self.data = [0] * self.capacity # Cria Array estático interno (só de inteiros)

    def is_empty(self):
        """
        Indica se o array está vazio.

        Retorno:
            bool: True se não há elementos (size), False caso contrário.
        """
        # SEU CÓDIGO AQUI.

    def get(self, index):
        """
        Retorna o elemento no índice informado.

        Parâmetros:
            index (int): Índice do elemento (0 <= index < size).

        Retorno:
            int: Valor armazenado naquele índice.

        Exceções:
            IndexError("Indice Fora dos Limites."): se index estiver fora dos limites.
        """
        # SEU CÓDIGO AQUI.

    def set(self, index, value):
        """
        Substitui o valor no índice informado por um novo valor inteiro.

        Parâmetros:
            index (int): Índice alvo (0 <= index < size).
            value (int): Novo valor a ser armazenado.

        Exceções:
            IndexError("Indice Fora dos Limites."): se index estiver fora dos limites.
        """
        # SEU CÓDIGO AQUI.

    def append(self, value):
        """
        Insere um valor inteiro ao final do array, redimensionando se preciso.
        O Redimensionamento é feito dobrando o tamanho do array, chamando _resize.

        Parâmetros:
            value (int): Valor a ser adicionado no fim.
        """
        # SEU CÓDIGO AQUI.

    def _resize(self, new_capacity): 
        """
        Redimensiona o array interno para new_capacity, copiando os elementos existentes.

        Parâmetros:
            new_capacity (int): Nova capacidade interna (>= 2 em reduções).

        Observações:
            - Este método preserva a ordem dos elementos.
            - Em crescimento, normal dobrar a capacidade.
            - Em redução, encolhe pela metade quando size <= 1/4 da capacity, 
            mas nunca abaixo de 2.
        """
        # SEU CÓDIGO AQUI.

    def __str__(self):
        return str(self.data[:self.size])

    def remove_at(self, index):
        """
        Remove e retorna o elemento no índice informado, deslocando os seguintes à esquerda.

        Parâmetros:
            index (int): Índice do elemento a remover (0 <= index < size).

        Retorno:
            int: Valor removido.

        Exceções:
            IndexError: se index estiver fora dos limites.

        Detalhes:
            - Após remover, se size <= 1/4 capacity (mínimo 2) chama _resize.
        """
        # SEU CÓDIGO AQUI.
    
    def index_of(self, value):
        """
        Procura a primeira ocorrência de um valor e retorna seu índice.

        Parâmetros:
            value (int): Valor a procurar.

        Retorno:
            int: Índice da primeira ocorrência ou -1 se não encontrado.
        """
        # SEU CÓDIGO AQUI.
    
    def remove(self, value):
        """
        Remove a primeira ocorrência de um valor, se existir.
        Utiliza as funções index_of e remove_at já criadas.

        Parâmetros:
            value (int): Valor a ser removido.

        Retorno:
            bool: True se removeu, False se o valor não estava no array.
        """
        # SEU CÓDIGO AQUI.

    def contains(self, value):
        """
        Verifica se o valor existe no array.
        Dá pra ser feito uma linha simples usando a função index_of.

        Parâmetros:
            value (int): Valor a verificar.

        Retorno:
            bool: True se existir, False caso contrário.
        """
        # SEU CÓDIGO AQUI.
    
    def insert(self, index, value):
        """
        Insere um valor na posição desejada, deslocando os elementos à direita.

        Parâmetros:
            index (int): Posição de inserção (0 <= index <= size).
                         Observação: index == size equivale a append.
            value (int): Valor inteiro a inserir.

        Exceções:
            IndexError: se index < 0 ou index > size.

        Detalhes:
            - Redimensiona (dobra) se estiver cheio.
            - Elementos a partir de index são deslocados uma posição à direita.
            Dica, pode usar o for i in range para andar de trás pra frente (-1).
        """
        # SEU CÓDIGO AQUI.


lista = DynamicIntArray()


#============ SAIDAS DE TESTE ============

# Saída: Lista vazia!
if lista.is_empty():
    print("Lista vazia!")
else:
    print("Lista tem elementos.")

print("Adicionando o 10;")
lista.append(10)
#Saída: Lista:  [10] 
print("Lista: ", lista) 

print("Verificando se 100 existe;")
#Saída: "100 existe na lista? Não" 
print("100 existe na lista? ", "Sim" if lista.contains(100) else "Não")

print("Adicionando o 20;")
lista.append(20)
#Saída: Lista:  [10, 20] 
print("Lista: ", lista)

print("Verificando o index do 20;")
#Saída: "Index do 20 é: 1" 
print("Index do 20 é: ", lista.index_of(20))

print("Verificando se 20 existe;")
#Saída: "20 existe na lista? Sim" 
print("20 existe na lista? ", "Sim" if lista.contains(20) else "Não")

print("Adicionando o 30;")
lista.append(30)
print("Lista: ", lista)
print("Tamanho da Lista para o usuário: ", lista.size)
print("Tamanho real (capacidade) da Lista internamente: ", lista.capacity)

print("Adicionando o 40;")
lista.append(40)
print("Lista: ", lista)

print("Adicionando o 50;")
lista.append(50)
# Saída: [10, 20, 30, 40, 50]   
print("Lista: ", lista)        

# Buscar Elemento no índice 2 
# Saída: 30  
print("Elemento na posição 2: ", lista.get(2))    

# Trocar Elemento no índice 2 para 99
# Saída: [10, 20, 99, 40, 50]
print("Trocando elemento no índice 2 para 99.")   
lista.set(2, 99)
print("Lista: ", lista)       

# Remover Elemento 40 se existir 
# Saída: [10, 20, 99, 50]
print("Removendo elemento 40 se existir.") 
lista.remove(40)
print("Lista: ", lista)

print("Removendo elemento no indice 1 se existir.") 
# Saída: [10, 99, 50]
lista.remove_at(1) 
print("Lista: ", lista)

print("Removendo mais um elementos no indice 2.") 
# Saída: Redimensionando de 8 para 4
# Saída: [10, 99]
lista.remove_at(2)
print("Lista: ", lista)

print("Removendo mais um elementos no indice 0.") 
# Saída: Redimensionando de 4 para 2
# Saída: [10]
lista.remove_at(1)
print("Lista: ", lista)

# Saída: [10, 47]
print("Adicionando o 47 na posição 1;")
lista.insert(1, 47)
print("Lista: ", lista)

# Saída: Redimensionando de 2 para 4
# Saída: [10, 99, 47]
print("Adicionando o 99 na posição 1;")
lista.insert(1, 99)
print("Lista: ", lista)
