'''
class BankAccount:
    def __init__(self,accountNumber,name,balance):
        self.accountNumber=accountNumber
        self.name=name
        self.balance=balance

    def deposit(self,amount):
        if amount>0:
            self.balance += amount
            print(f"Deposit of Rs.{amount} successful.")
        else:
            print("Invalid deposit amount.")

    def withdrawal(self,amount):
        if 0<amount <=self.balance:
            self.balance -= amount
            print(f"withdrawal of Rs.{amount} successful.")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

    def bank_fees(self):
        fees=0.05*self.balance
        self.balance -= fees
        print(f"Bank fees of Rs.{fees} applied.")

    def display(self):
        print(f"Account number:{self.accountNumber}")
        print(f"Account Holder:{self.name}")
        print(f"Balance: Rs.{self.balance}")

account1 = BankAccount(accountNumber=123456, name="samhitha", balance=10000)

account1.display()
account1.deposit(500)
account1.withdrawal(200)
account1.bank_fees()
account1.display()
'''
'''
class MyClass:
    class_variable = "I am a class variable"

    def init(self, instance_variable):
        self.instance_variable = instance_variable
class_namespace = dir(MyClass)
print("Namespace of MyClass:")
print(class_namespace)
obj = MyClass()
instance_namespace = dir(obj)
print("\nNamespace of the instance:")
print(instance_namespace)
'''

'''
class Student:
    def _init_(self, student_id, student_name):
        self.student_id = student_id
        self.student_name = student_name

    def display_attributes(self):
        print("Attributes and their values:")
        print(f"student_id: {self.student_id}")
        print(f"student_name: {self.student_name}")
        print()

    def remove_attribute(self, attribute_name):
        if hasattr(self, attribute_name):
            delattr(self, attribute_name)
            print(f"{attribute_name} removed successfully.")
        else:
            print(f"{attribute_name} does not exist in the attributes.")


student1 = Student()
student1.display_attributes()
student1.student_class = "Class A"
student1.display_attributes()
student1.remove_attribute("student_name")
student1.display_attributes()

'''