def max_num(a,b):
    if a > b:
        return a
    else:
        return b
print("To check the larger number")    
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

max  = max_num(a,b)
print(max)



def fact(n):
    if n == 0:
        return 1
    else:
        return n*fact(n-1)
print("Checking Factorial")    
print (fact(5))


def area_circle(r = 1, pi = 3.14): 
    area =  pi*(r**2)
    return area
print("Area of circle with deafult parameter")
print("area of circle with default parameter: ", area_circle())
print("area of circle with user given parameter: ", area_circle(5))


def greet():
    print ("'Hello, Python Learner!'.")
print("Using greet() function to greet")
greet()

def sum(a,b):
    return a + b
print("Adding two numbers")
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))

print (sum(a,b))



def is_even(n):
    if (n%2 == 0):
        return True
    else:
        return False
print("Checking even number")    
n = int(input("Enter the number: "))

print(is_even(n))


def square(n):
    return n*n
print("Squaring a number")
n = int(input("Enter the number: "))
print(square(n))



def max_of_three(a,b,c):
    if a > b:
        if a > c:
            return a
        else:
            return c
    else:
        if b > c:
            return b
        else:
            return c
print("findind largest of the three numbers")        
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))            
c = int(input("Enter the third number: "))

print(max_of_three(a, b, c))






def reverse_string(s):
    return s[::-1]

string = input("Enter the string to reverse: ")

print(reverse_string(string))



def count_vowels(s):
    count = 0
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    for i in s:
        if i in vowels:
            count += 1
    return count
string = input("Enter the string to count vowels: ")
print("number of vowels in the string are: ", count_vowels(string))
        
        



def is_palindrome(s):
    if (s[::-1] == s):
        return True
    else:
        return False
    
string = input("Enter the string to check palindrome: ")

print(is_palindrome(string))





def sum_of_list(numbers):
    sum = 0
    for i in numbers:
        sum += i
    return sum

print("Adding elements of a list (integers only)")
n = int(input("Enter number of elements in list: "))
numbers = []

for i in range(n):
    numbers.append(int(input(f"Enter element number {i+1}: ")))

print(numbers)
print("Sum of the list is: ", sum_of_list(numbers))




def find_min_max(numbers):
    numbers.sort()
    result = f"Min is {numbers[0]}, Max is {numbers[-1]} "
    return result
print("Finding minimum and maximum element of list (integers only)")
n = int(input("Enter number of elements in list: "))
numbers = []

for i in range(n):
    numbers.append(int(input(f"Enter element number {i+1}: ")))
print(numbers)
print(find_min_max(numbers))





def print_multiplication_table(n):
    for i in range (10):
        print (n*(i+1))
n = int(input("Enter the number whose table you want to print: "))
print_multiplication_table(n)




def fibonacci_series(n):
    a = 0 
    b = 1
    print(a, end = ' ')
    print(b, end = ' ')
    for i in range(n):
        next = a + b
        print (next, end = " ")
        a = b
        b = next
print("Fibonacci series till n terms")
n = (int(input("Enter value of 'n' for n terms of series: ")))
fibonacci_series(n)




def count_words(sentence):
    s = sentence.split(" ")
    return len(s)

sentence = (input("Enter your sentence to count words(should be splitted with ' ' spaces): "))
print(count_words(sentence))




def sum_natural(n):
    sum = 0
    if n == 0:
        return sum
    else:
        return sum+n+sum_natural(n-1)
    
n = int(input("Enter number of first natural numbers you want to add: "))
print(sum_natural(n))


def power(base, exp):
    return base**exp
print("Calculating exponent")
a = int(input("Enter the base: "))
b = int(input("Enter the power: "))
print(power(a,b))



def gcd(a,b):
    if a > b:
        n = a
    else:
        n = b
    while n > 0:
        if (a%n == 0 and b%n== 0):
            return n
        n = n-1
    return 0
print("Finding GCD og two numbers")
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print(gcd(a,b))




def nested_operations(a,b):
    def multiply():
        return a*b
    return multiply()
print("using nested functions to multiply two numbers")
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
print(nested_operations(a, b))


def draw_square():
    print("Drawing a square")
    n = int(input("Width of the box: "))
    print (' *'*n)
    print (' *', "  "*(n-3), ' *')
    print (' *', "  "*(n-3), ' *')
    print (' *'*n)


draw_square()

print("Solving a quadratic equation")
equation = (input("Enter equation in format ax2+bx+c : "))
def quad_roots(equation):
    terms = equation.split('+')
    values = []
    for i in terms:
        values.append(i.split('x'))
    a = int(values[0][0])
    b = int(values[1][0])
    c = int(values[2][0])
    print('a = ',a,'b = ',b,'c = ',c)
    D = (b**2) - (4*a*c)
    if (D == 0):
        return "The Equation has one Real Root"
    elif (D > 0):
        return "The Equation has two Real Roots"
    else:
        return "The Equation has two Complex Roots"


print(quad_roots(equation))




def decimal_to_binary(n):
    if n <= 1:
        return str(n)

    return decimal_to_binary(n // 2) + str(n % 2)

n = int(input("Enter the number to convert into binary: "))
print(f'binary representaion of {n} is: \n', decimal_to_binary(n))




def solve_linear_system():
    print("Solving linear system of equation")
    print("Enter coefficients for ax + by = e and cx + dy = f:")
    a = float(input("Enter a: "))
    b = float(input("Enter b: "))
    c = float(input("Enter c: "))
    d = float(input("Enter d: "))
    e = float(input("Enter e: "))
    f = float(input("Enter f: "))
    
    denominator = a * d - b * c
    if denominator == 0:
        print("No unique solution")
    else:
        x = (d * e - b * f) / denominator
        y = (a * f - c * e) / denominator
        print("Solution: x =", x, ", y =", y)


solve_linear_system()


def compound_interest():
    print("Finding Compount interest")
    p = float(input("Enter principal amount (P): "))
    r = float(input("Enter annual interest rate (r) (e.g., 0.05 for 5%): "))
    n = float(input("Enter number of years (n): "))
    t = float(input("Enter times interest compounded per year (t): "))
    
    if p <= 0 or r < 0 or n <= 0 or t <= 0:
        print("Invalid input: All values must be positive and rate non-negative.")
        return
    
    ci = p * ( (1 + r/t) ** (n*t) ) - p
    print("Compound Interest:", ci)

compound_interest()






















