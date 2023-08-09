def f (x , y):
    x = x + 1
    y.append(4)

x = 1
y = [1, 2, 3]

print("Antes x:", x)
print("Antes y:", y)

f(x, y)

print("Depois x:", x)
print("Depois y:", y)


def f():
    a = 5
    print('a:', a)
    return a

a = 3
print(a)
a = f()
print(a)


def soma(a, b):
    soma = a + b
    return soma

soma_n = soma(12, 17)
print("Resultado:", soma_n)

