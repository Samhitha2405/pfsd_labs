'''
print("enter the values")
val=[1,2,3,4,5]
avg=sum(val)/len(val)
print(avg)

num=int(input("enter your value:"))
print(num)

sam= input("enter your name:")
print(sam)

a=1+3j
b=2+4j
print(a+b)

vala=[9,4,9,0,7,9,9,2,1,1]
mean=sum(vala)/len(vala)
print(mean)

h=float(input("enter:"))
print(h)

val.reverse()
print(val)
'''

'''
num_elements = int(input("Enter the number of elements: "))
numbers = []
for i in range(num_elements):
    num = float(input(f"Enter number {i + 1}: "))
    numbers.append(num)
average = sum(numbers) / len(numbers)
print(f"The average is: {average}")
'''

'''
user_input = input("Enter an integer: ")
try:
    integer_value = int(user_input)
    print(f"You entered: {integer_value}")
except ValueError:
    print("Invalid input. Please enter a valid integer.")
    '''
'''
complex_num1 = 2.5 + 3.7j
complex_num2 = 1.2 + 0.8j
result_complex = complex_num1 + complex_num2
float_num1= 4.5
float_num2 = 3
result_float = float_num1 + float_num2
int_num1 = 5
int_num2 = 2
result_integer = int_num1 + int_num2
print("Complex Number Addition:", result_complex)
print("Float Number Addition:", result_float)
print("Integer Number Addition:", result_integer)
'''
'''
integer_input = int(input("Enter an integer: "))
float_result = float(integer_input)
print(f"The integer {integer_input} as a float is: {float_result}")

'''
'''
string_input = input("Enter a string: ")
integer_input = int(input("Enter an integer: "))

try:
    string_as_integer = int(string_input)
    result = string_as_integer + integer_input
    print(f"The sum of {string_as_integer} and {integer_input} is: {result}")

except ValueError:
    print("Invalid input. Please enter a valid integer.")

'''