'''

funktionel programmering = instead of f(x) = y, we have f(x) = g(h(x)) = y

Ex 1: recursion
5! = 5 * 4 * 3 * 2 * 1 = 120 = 5 * 4! = 5 * 4 * 3! = 5 * 4 * 3 * 2! = 5 * 4 * 3 * 2 * 1! = 5 * 4 * 3 * 2 * 1

def fac(n):
    result = 1
    for x in range(n, 0, -1):
        result *= x
    return result

def fac(n):
    if n == 0:
        return 1
    else:
        return n * fac(n - 1)

fac(3)
3 \neq 0
3 * fac(2)

fac(2)
2 \neq 0
2 * fac(1)

fac(1)
1 \neq 0
1 * fac(0)

fac(0)
0 == 0
return 1

go back to fac(3) = 3 *2 *1 *1

Ex 2: fibonacci

0,1,1 -> 2,3,5,8,13,21,34,55,89,144
base case: fib(0) = 0, fib(1) = 1

ex output: fib(4)
0
1
1
2
3

def fib(n):
    # Base cases
    if n == 0:
        return 0
    if n == 1:
        return 1

    else:
        # sum up the last last and the last number 
        return fib(n - 1) + fib(n - 2)

for x in range(5):
    print(fib(x))

Ex 3: GCD 
for ex: 6/8 then gcd(6, 8) = 2
6 has divisors 1, 2, 3, 6
8 has divisors 1, 2, 4, 8
biggest nummer they share is 2 

def gcd(a, b):
    if b > a:
        print("a must be bigger than b in gcd(a,b)")
        return None
    r = a % b 
    while r != 0:
        a = b
        b = r
        r = a % b
    return b

Ex gcd(12, 4) = 4
12 > 4
12 mod 4 = 0 where 4 is the greatest common divisor
r = 12 mod 4 = 0
return 4

gcd(7, 3) = 1
r = 7 mod 3 = 1
a = 3
b = 1
r = 3 mod 1 = 0
return 1

def gcd(a,b):
    if b > a:
        print("a must be bigger than b in gcd(a,b)")
        return None
    r = a % b
    if r == 0:
        return b
    else:
        return gcd(b,r)

gcd(11, 7) -> 4 -> gcd(7, 4) -> 3 -> gcd(4, 3) -> 1 -> gcd(3, 1) -> 0 -> return 1

__________________________break____________________________

def recursion():
    if base case
        return
    else:
        return recursion()

WHILE LOOP -> RECURSION
def f(x):
    s = 0
    for i in range(x+1):
        s += i
    return s
f(5) 
0 to 5
-s=0
-s=0+1
-s=1+2
-s=3+3 
-s=6+4
-s=10+5
5+4+3+2+1 = 15

Becomes

def f_rec(x):
    if x == 0:
        return 0
    else:
        return x + f_rec(x-1)

f_rec(5)
return 5 + f_rec(4) = 5 + (4 + f_rec(3)) = 5 + (4 + (3 + f_rec(2))) = 5 + (4 + (3 + (2 + f_rec(1)))) = 5 + (4 + (3 + (2 + (1 + f_rec(0))))) = 5 + (4 + (3 + (2 + (1 + 0)))) = 15

f_rec(4)
return 4 + f_rec(3)

...

RECURSION OVER LISTS
# This function is to calculate the length of a list
def length(xs):
    # obs: lists behave as boolean values ([] is False)
    if xs:
        xs.pop()
        return (1 + length(xs))
    else:
        return 0

print(length([1,5,-1])) = 1 + length([1, 5]) = 1 + (1 + length([1])) = 1 + (1 + (1 + length([]))) = 1 + (1 + (1 + 0)) = 3


SORTING OF LISTS
Ex Quick sort: 
1. Välj ett element i listan (“pivotelementet”).
2. Dela upp listan i två dellistor: en med alla element som är mindre än pivotelementet och en med alla element som är större än pivotelementet.
3. Sortera dellistorna genom rekursion. Basfallet är tomma listan vilken redan är sorterad.
4. Sätt ihop listorna med pivotelementet i mitten.

[3, 1, 4, 2]
x = 3
[1, 2] and [4]


def smallereq(xs,v):
    res = []
    while xs:
        x = xs.pop()
        if x <= v:
            res.append(x)
    return res

def greater(xs,v):
    res = []
    while xs:
        x = xs.pop()
        if x > v:
            res.append(x)
    return res

def quicksort(xs):
    if xs == []:
        return xs
    p = xs.pop()
    s = quicksort(smallereq(xs.copy(),p)) # -> [7, 3, 8]
    g = quicksort(greater(xs.copy(),p)) # -> []
    return (s + [p] + g)

print(quicksort([8,3,7,99])) 

def quicksort(xs):
    if xs == []:
        return xs
    else:
        p = xs.pop()
        s = quicksort([ x for x in xs if x <= p ]) # ([for x in xs, if x <=p then save result in x])
        g = quicksort([ x for x in xs if x > p ])
        return (s + [p] + g)

print(quicksort([3, 1, 59, 8]))
p = 8
s = quicksort([3, 1, 59]) 

p=59 
s = quicksort([3, 1]) 

p=1 
s = quicksort([]) = [] 
g = quicksort([3]) = [3] 

return 

s = [] + [1] + [3] = [1, 3]
g = [] + [59] + [] = [59]
return [1, 3] + [8] + [59] = [1, 3, 8, 59]

_______________________________________________________lessons ends____________________________________________________________

Chapters

1) Intro to course

2) Intro to python

3) Lists and iterations

4) Files and dictionaries

5) Error handling and exceptions

6) Sequences and generators

7) Modules, libraries, program structure

8) Functional programming

9) OOP: classes

10) OOP: inheritance

11) OOP: more from last week

12) Defensive programming
'''
