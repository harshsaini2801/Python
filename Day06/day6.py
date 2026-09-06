#Variables and Data Types
a = 1
b = True
c = "Harry"
d = None
a1 = 9
e = 1.9
f = complex(8, 2)#if i use print(f) it will print (8+2j) which is a complex number. Complex numbers are used in advanced mathematics and engineering applications. They are represented in the form of a + bi, where a is the real part and b is the imaginary part. In this case, 8 is the real part and 2 is the imaginary part.
print(f)
print(b)
print (a + a1)
print("The type of a is: ", type(a))
print("The type of b is: ", type(b))
print("The type of c is: ", type(c))
print("The type of d is: ", type(d))
print("The type of e is: ", type(e))
print("The type of f is: ", type(f))

list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]
print(list1)

tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"))
print(tuple1)

dict1 = {"name":"Sakshi", "age":20, "canVote":True}
print(dict1)
"""
OUTPUT:-
True
10
The type of a is:  <class 'int'>
The type of b is:  <class 'bool'>
The type of c is:  <class 'str'>
The type of d is:  <class 'NoneType'>
The type of e is:  <class 'float'>
The type of f is:  <class 'complex'>
[8, 2.3, [-4, 5], ['apple', 'banana']]
(('parrot', 'sparrow'), ('Lion', 'Tiger'))
{'name': 'Sakshi', 'age': 20, 'canVote': True}
"""