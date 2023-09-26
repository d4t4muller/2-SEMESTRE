from Stack import Stack



def fibonacci(n):
    sequencia = Stack()
    for i in range(n):
        if i <= 1:
            sequencia.push(i)
        else:
            primeiro = sequencia.pop()
            segundo = sequencia.pop()
            soma = primeiro + segundo
            sequencia.push(segundo)
            sequencia.push(primeiro)
            sequencia.push(soma)

    return sequencia


n = 15 
sequencia = fibonacci(n)
while not sequencia.is_empty():
    print(sequencia.pop(), end=" ")