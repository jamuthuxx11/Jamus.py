#creating a function in python
def is_even(number):
    if number % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")


#calling  a function
is_even(80)

#function 2
def printEmobilis():
    for i in range(10):
        print(i+1,"Emobilis")

printEmobilis()


#function 3
def printName(x):
    for i in range(2):
        print(x)


printName("jude")
printName("jamu")

#function 4
def getModulous(y,x):
    return y%x

z =getModulous(6,9)  +20

print(z)

def find_largest_number(numbers):
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest

numbers = [11,25,32,46,55,60,7,81,0]
largest_numbers = find_largest_number(numbers)
print("The largest number in the list:",largest_numbers)


