#Hello World

wlcomeMsg = "First Program in Python"
print(wlcomeMsg)

""" 
print("Basic Calculator Two variable: ")
num1 = input("first: ")
num2 = input("second: ")
sum = (float(num1) + float(num2))
product = (float(num1) * float(num2))
quotient = (float(num1) / float(num2))
difrence = (float(num1) - float(num2))

print("Answers: ")
print("Sum: " + str(sum))
print("Product: " + str(product))
print("Quotient: " + str(quotient))
print("Difference: " + str(difrence)) 
"""

print("--Welcome Python basic Calculator Console--")


#Recieve input from user with string contatination
""" 
TypeName = input('What is your name? ')
ageUser = input('Your Age Please: ')
gender = input('Gender: ')
print("Hi " + TypeName + "! " + "and your age is " + ageUser + " you're a " + gender + ".")

"""

#age = 2022 - int(str) string to int 
#birth_year = input ("Enter your birth year: ")
#age = 2022 - int(birth_year) 
#print(age)

#functions
def addition(num1, num2):
    total = num1 + num2
    return(total)
def divideFunc(num1 , num2):
    quot = num1 / num2
    return(quot)
def subtract(num1, num2):
    diff = num1 - num2
    return(diff)
def multiply(num1, num2):
    prod = num1 * num2
    return(prod)
def sqr_1st(num1):
    sqr1 = num1**2
    return(sqr1)
def sqr_2nd(num2):
    sqr2 = num2**2
    return(sqr2)


num1 = int(input('Enter 1st number : '))
num2 = int(input('Enter 2nd number : '))

print("Sum: " + str(addition(num1 , num2)))
print("Quotient: " + str(divideFunc(num1, num2)))
print("Difference: " + str(subtract(num1, num2)))
print("Product: " + str(multiply(num1, num2)))
print("Square of 1st number : " + str(sqr_1st(num1)))
print("Square of 2nd number: " + str(sqr_2nd(num2)))
print(tuple('dog'))
print(list('dog'))