
# generador
def fibonacci(max):
    a, b = 0, 1
    while a < max:
        yield a
        a, b = b, a + b

# cada generador se puede utilizar una vez, si se desea reutilizar se debe de crear una nueva instancia

fb1 = fibonacci(10)
fib_nums = [num for num in fb1]

doble_fib_nums = [num * 2 for num in fb1] # no funciona
doble_fib_nums_2 = [num * 2 for num in fibonacci(4)] # si funciona

print(fib_nums)
print(doble_fib_nums)
print(doble_fib_nums_2)