def fibonacci ( stop ) :
    a , b = 0 , 1
    while a <= stop :
        yield a # if you write return instead of yield, the function will return only the first value and then stop
        a , b = b , a + b

print(list(fibonacci(100)))