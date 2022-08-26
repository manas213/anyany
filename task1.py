#Q1
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))

def addition(num1, num2):
    add = num1+num2
    print(add)

addition(num1, num2)

#Q2
Brand_Name = input("Enter brand name: ")
Model_Name = input("Enter model name: ")
available_at_price = input("Enter available price: ")

def laptop(Brand_Name, Model_Name, available_at_price):
    print(f"The laptop is {Brand_Name}, {Model_Name} and the price is available at {available_at_price}")

laptop(Brand_Name, Model_Name, available_at_price)