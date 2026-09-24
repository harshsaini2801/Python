a = int(input("Enter a age: "))
print("Your age is :",a)

'''conditional operators are <, >, <= , >= , == ,!=
print(a>18)
print(a<=18)
print(a==18)
print(a!=18) '''

#1

if(a>18):
    print("You are eligible for voting")
else:
    print("You are not eligible for voting")

#2

num = int(input("Enter a no. : "))
print("Your number is :",num)
if (num < 0):
    print("Number is negative.")
elif (num == 0):
    print("Number is Zero.")
elif(num == 999):
    print("Your number is special")    
else:
    print("Number is positive.")

print("I am happy now")

#Nested if else statement

num = 18
if (num < 0):
    print("Number is negative.")
elif (num > 0):
    if (num <= 10):
        print("Number is between 1-10")
    elif (num > 10 and num <= 20):
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")

    