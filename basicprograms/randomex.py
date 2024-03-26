'''
import random
n=random.randbytes(1)
print(n)

print(random.randrange(1,100))

mylist=("samhitha","priya","vasavi","jagruti","Niharika")
mylist1={"samhitha","priya","vasavi","jagruti","Niharika"}
mylist2=["samhitha","priya","vasavi","jagruti","Niharika"]
print(random.shuffle(mylist2))
'''
import string
import random
s=10
ran=''.join(random.sample(string.ascii_uppercase+string.digits,k=s))
s1=4
ran1=''.join(random.sample(string.digits,k=6))
print(ran)
print(ran1)
