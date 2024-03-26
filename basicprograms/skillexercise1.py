#-------------------
'''
n=int(input("Enter a Number"))
if n==0:
    print("wrong input")
else:
    for i in range(n,n+1):
        val=n*(n*1)
        print(val)
'''
#-------------
'''
x=0
str1= "thisismycountryindia"
for i in str1:
    x=x+1
    print(str1[0:x])
for i in str1:
    x=x-1
    print(str1[0:x])
'''
#---------------
'''
n=int(input("enter a number"))
for i in range(0,n):
    for j in range(0,i+1):
        print("* ", end="")
    print("\r")
for i in range(n, 0, -1):
    for j in range(0, i):
        print("* ", end="")

    print("\r")
'''
#------------------
'''
a1=15
a2=format(a1,'b')
print(a2)
'''
#---------------
user_input = input("Enter an integer value: ")
converted_value = int(user_input)
print("Converted integer value:", converted_value)
