
def fibonacci (stop):
    a , b = 0 , 1
    while a <= stop:
        yield a
        a , b = b , a + b

print(list(fibonacci(15)))
for num in fibonacci(15):
    print(num)

try:
    for num in list(fibonacci(4)) :
        print (num)
except:
    raise Exception ("fibonacci is not an iterable")


x = 11

print(f"text {x=}") 

