def square_rt(n):
    return n**(1/2)
    
def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)
    
def sine(n):
    from math import sin
    return sin(n)
    
pi_val = 3.14159265359

import random

def random_5():
    a = []
    for i in range(5):
        a.append(random.randint(1,100))
    return a

def random_element_list(a):
    random_element = a[random.randint(0,4)]
    return random_element


