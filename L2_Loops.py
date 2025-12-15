# printing numbers from 1 to 10

print ("\n == 1 to 10 reverse order == \n")

print ("\n using 'while' loop")
n = 10
while (n > 0):
    print(n)
    n -= 1
print ("\n using 'for' loop")
for i in range(10,0,-1):
    print(i)
    




# printing squares of first five numbers

print ("\n == squares of first five numbers == \n")

print ("\n using 'while' loop")
n = 1
while (n < 6 ):
    print (n*n)
    n += 1

print ("\n using 'for' loop")
for i in range(1,6):
    print(i*i)
 
    
 
    
# even numbers from 0 to 10

print ("\n == even numbers from 0 to 10, and their sum == \n")

print ("\n using 'while' loop")
sum = 0
n = 0
while (n < 11):
    if (n % 2 == 0):
        print (n)
        sum += n
    n += 1
print ("sum of even numbers = ", sum)    

print ("\n using 'for' loop")
sum = 0
for i in range  (11):
    if (i % 2 == 0):
        print (i)
        sum += i
print ("sum of even numbers = ", sum)



print ("\n using 'while' loop")
n = 1
sum = 0
while (n <= 20):
    if ( n % 2 != 0 and n%3 != 0 and n%5 != 0):
        print (n)
        sum += n
    n += 1
print ("sum of numbers 1 to 20 not divisible by 2,3 or 5 are: ", sum)


print ("\n using for loop")

sum = 0 
for i in range(21):
    if ( i % 2 != 0 and i%3 != 0 and i%5 != 0):
        print (i)
        sum += i
print ("sum of numbers 1 to 20 not divisible by 2,3 or 5 are: ", sum)
    




print ("\n using 'while' loop")
first_num = 0
sec_num = 1

print (first_num)
print (sec_num)
n = 0
while ( n < 8-2):

    series = first_num + sec_num
    print(series)
    
    first_num = sec_num
    sec_num = series
    
    n += 1

print ("\n using 'for' loop")
first_num = 0
sec_num = 1

print (first_num)
print (sec_num)
for i in range(8-2):
    series = first_num + sec_num
    print(series)
    
    first_num = sec_num
    sec_num = series









print (" Using while loop")
char = ord('A')
n = 0
while (n<26):
    print(chr(char+n))
    n += 1

print (" Using for loop")
char = ord('A')
for i in range (26):
    print(chr(char+i))






print("Using while loop")
numbers = []
n = 0
while (n<4):
    a = int(input(f"Enter number {n+1}: "))
    numbers.append(a)
    n += 1
numbers.sort()
print("Largest numbers is: " , numbers[-1])

print("using for loop")
numbers = []
for i in range(4):
    a = int(input(f"Enter number {i+1}: "))
    numbers.append(a)
numbers.sort()
print("Largest numbers is: " , numbers[-1])




print ("using for loop\n")
n = 5
for i in range(5):
        a = n-i
        print ("* "*a)
        
print("using while loop\n")
n = 5
while (n>0):
    print ("* "*n)
    n -= 1


print ("using for loop\n")
n = 5
for i in range(5):
        a = n-i
        print ("* "*(i+1))
print("using while loop\n")
n = 1
while (n<=5):
    print ("* "*n)
    n += 1





print (" using for loop \n")
for i in range (4):
    for j in range (i+1):
        print (j+1, end= " ")
    print()
for i in range(3,0,-1):
    for j in range(i):
        print(j+1, end = " ")
    print()

print ("\nusing while loop \n")
i = 0
while (i<4):
    j = 0
    while(j<i+1):
        print(j+1, end = " ")
        j += 1
    print()
    i += 1    

i = 3
while (i>0):
    j = 0
    while (j<i):
        print(j+1,end = " ")
        j += 1
    print()
    i -= 1































