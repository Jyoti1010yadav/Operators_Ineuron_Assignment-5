#  1. Write a python script to remove the last digit from a given number. (for example, if user enters 2534 then your output should be 253)
num=int(input("Enter number\t"))
number=num//10
print("user enters",num," then your output should be ",number)
print()

# 2. Write a python script to get the last digit from a given number. (for example, if user enters 2089 then your output should be 9)

num=int(input("Enter number\t"))
out=num%10
print("last digit of your ",num,"is ",out)
print()

# 3. Write a python script to swap data of two variables
num1=int(input("Enter number1\t"))
num2=int(input("Enter number2\t"))
print("Before swap num1= ",num1)
print("Before swap num2= ",num2)
temp=num1
num1=num2
num2=temp
print("After swap num1 =",num1)
print("After swap num2 =",num2)
print()

# 4. Write a python script to find x power y, where values of x and y are given by user
x=int(input("Enter number1 "))
y=int(input("Enter number2 "))
print("the value of x is ",x)
print("the value of y is ",y)
print("power of x and y is ", x**y)
print()

#5. Write a python script which takes a three digit number from the user and displays only its first digit.
num1=int(input("Enter 3 digit number\t"))
first_digit=num1//100
print("three digit number",num1,"and only its first digit is ",first_digit)
print()

# 6. Write a python script which takes a three digit number from the user and displays only its middle digit.
number=int(input("Enter 3 digits number \n"))
middle_digits=(number//10)%10
print("Middle digits of ", number, "is ",middle_digits)
print()

# # 7. Write a python script which takes a three digit number from the user and displays only its last digit.
num=int(input("Enter number\t"))
last_digit=num%10
print("Last digits of ", num, "is ",last_digit)
print()

# 8. Write a python script to use IN operator to display the data present in the list
LIST=["rahul","jyoti","ashu"]
print(LIST)
search=input("Enter the name you want to search ")
print("search elements",search,search in LIST)
print()

# 9. Write a python script to use NOT IN operator to display the data not present in list
list=[1,5,896,45.6,78]
print(list)
not_find=int(input("Enter the number..."))
print("elements not in list is ",not_find,not_find not in list)
print()

# 10. Write a python script to use IS operator to display if both variables are the same object or not
obj1=int(input("Enter any 1st digit "))
OBJ2=int(input("Enter any 2nd digit "))
print("obj1",obj1)
print("OBJ2",OBJ2)
print(obj1 is OBJ2)
print()
