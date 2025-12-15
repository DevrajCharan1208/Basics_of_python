a_real = int(input("Enter the real part of first number: "))
a_img = int(input("Enter the imaginary part of the first number: "))

b_real = int(input("Enter the real part of the second number: "))
b_img = int(input("Enter the imaginary part of the second number: "))

a = f"{a_real} + {a_img}i"
b = f"{b_real} + {b_img}i"

print ("c1 = ", a)
print ("c2 = ", b)

sum_real = a_real+b_real
sum_img = a_img+b_img
addition = f"{sum_real} + {sum_img}i"

print ("Addition = ", addition)

sub_real = a_real - b_real
sub_img = a_img - b_img
sub = f'{sub_real} + {sub_img}i'

print ("Subtraction = ", sub)

mul_real = (a_real*b_real) - (a_img*b_img)

mul_img = (a_real*b_img)+(a_img*b_real)

multiplication = f"{mul_real} + {mul_img}i"

print ("multiplication = ", multiplication)

if (a_real == b_real and a_img == b_img):
    print ("Both numbers are equal")
else:
    print("Both numbers are not equal")
    
mag_a = ((a_real*a_img)**(1/2))
mag_b = ((b_real*b_img )**(1/2))

if(mag_a > mag_b ):
    print ("C1 > C2")
elif(mag_a<mag_b):
    print("C1<C2")



class circle:
    def __init__(self, radius):
        self.radius = radius
        
    def area(self,radius):
        area = 2*3.14*radius
        print ("area of the circle is: ", area)
    def para(self,radius):
        para = 3.14*(radius**2)
        print ("parameter of the cicle: ", para)
obj1 = circle(2)
obj1.area(obj1.radius)
obj1.para(obj1.radius)

   
class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
        
        

















 
