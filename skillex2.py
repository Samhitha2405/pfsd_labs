
#a=int(input("enter your number: "))
#if(a%2==0):
 #   print("even number")
#else:
   # print("odd number")
'''
a=10
b=20
c=30
if(a<b):
    if(a>c):
        print("A is Big")
    else:
        print("C is Big")
elif(b>c):
        print("B is Big")
else:
    print("C is Big")
'''
'''
number = int(input("Enter a number to calculate its factorial: "))
factorial_result = 1
for i in range(1, number + 1):
    factorial_result *= i
print(f"The factorial of {number} is: {factorial_result}")
'''
'''
for i in range(1, 8):
    multiple = 7 * i
    print(f"{i}th multiple of 7: {multiple}")
    '''
'''
side1 = float(input("Enter the length of side 1: "))
side2 = float(input("Enter the length of side 2: "))
side3 = float(input("Enter the length of side 3: "))

is_right_triangle = side1**2 + side2**2 == side3**2 or \
                     side1**2 + side3**2 == side2**2 or \
                     side2**2 + side3**2 == side1**2
if is_right_triangle:
    print("It is a right triangle.")
else:
    print("It is not a right triangle.")
    '''
'''
num_rows = 5
for i in range(num_rows):
    for j in range(i + 1):
        print("*", end=" ")
    print()
for i in range(num_rows - 1, 0, -1):
    for j in range(i):
        print("*", end=" ")
    print()
'''
'''
binary_sequence = input("Enter comma-separated 4-digit binary numbers: ")
binary_numbers = binary_sequence.split(',')
divisible_by_5 = []
for binary_number in binary_numbers:
    decimal_number = int(binary_number, 2)
    if decimal_number % 5 == 0:
        divisible_by_5.append(binary_number)
print("Numbers divisible by 5:", ', '.join(divisible_by_5))
'''


