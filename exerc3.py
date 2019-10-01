def numeros_fibonnaci(i):
    fib = 0
    fib1 = 1
   
    for n in range(0, i+1):
        if n == 0:
            fib = fib
            print('fib({}) = {}'.format(n, fib))
        else: 
            fib = fib + fib1
            fib1 = fib - fib1
            print('fib({}) = {}'.format(n, fib))
i = int(input('fib(n) | n = '))
numeros_fibonnaci(i)
