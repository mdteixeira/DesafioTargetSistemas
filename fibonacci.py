# Calcula a sequência de Fibonacci recursivamente
def fibonacci_of(n):
    if n in (0, 1):  # Verifica se n é 0 ou 1
        return n
    return fibonacci_of(n - 1) + fibonacci_of(n - 2)


# Verifica se o valor passado está na sequência de Fibonacci
def pertence(n):

    lista = [0]
    i = 0

    # Verifica se o último valor é maior que n para limitar o número de repetições
    while lista[-1] < n:
        lista.append(fibonacci_of(i))
        i += 1

    # Verifica se há mais de 0 ocorrências de 0 na lista
    return lista.count(n) != 0


# Exemplo com o número 34
print(pertence(34))  # True


entrada: int = int(input("Insira um número inteiro: "))

print(pertence(entrada))
