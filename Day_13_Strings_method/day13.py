#strings are immutable
a = "!!!Harsh!!!!!!!"
print(a)
print(len(a))
print(a.upper())
print(a.lower())
print(a.rstrip("!"))#this only remove ! of only after the string not before the string
print(a.replace("Harsh", "John"))

b = "!!!Harsh! !!!!!!!!!! Harsh"
print(b.split(" "))
heading = "introduction to python"
print(heading.capitalize())

str1 = "Welcome to the Console!!!"
print(str1.center(50))# give 50 spaces and center the string in that space
print(len(str1))# output the length of str1 string is 25
print(len(str1.center(50)))#now output of this is 50 because we have given 50 spaces to center the string in that space

print(a.count("Harsh"))
print(str1.endswith("!!!"))
print(str1.endswith("to", 4, 10))

str2 = "He's name is Dan. He is an honest man."
print(str2.find("is"))

str3 = "He's name is Dan. Dan is an honest man."
print(str3.index("Dan"))

str4 = "WelcomeToTheConsole"
print(str4.isalnum())

str5 = "Welcome"
print(str5.isalpha())

str6 = "We56lcome"
print(str6.isalpha())

str7 = "hello world"
print(str7.islower())

str8 = "hello worLd"
print(str8.islower())

str9 = "We wish you a Merry Christmas"
print(str9.isprintable())

str10 = "We wish you a Merry Christmas\n"
print(str10)
print(str10.isprintable())

str11 = "        "       #using Spacebar
print(str11.isspace())
str12 = "        "       #using Tab
print(str12.isspace())

strr1 = "World Health Organization" 
print(strr1.istitle())

strr2 = "To kill a Mocking bird"
print(strr2.istitle())

strr3 = "WORLD HEALTH ORGANIZATION" 
print(strr3.isupper())

strr4 = "Python is a Interpreted Language" 
print(strr4.startswith("Python"))

strr5 = "Python is a Interpreted Language" 
print(strr5.swapcase())

strr6 = "His name is Dan. Dan is an honest man."
print(strr6.title())

'''
output:
!!!Harsh!!!!!!!
15
!!!HARSH!!!!!!!
!!!harsh!!!!!!!
!!!Harsh
!!!John!!!!!!!
['!!!Harsh!', '!!!!!!!!!!', 'Harsh']
Introduction to python
            Welcome to the Console!!!             
25
50
1
True
True
10
13
True
True
False
True
False
True
We wish you a Merry Christmas

False
True
True
True
False
True
True
pYTHON IS A iNTERPRETED lANGUAGE
His Name Is Dan. Dan Is An Honest Man.
'''
