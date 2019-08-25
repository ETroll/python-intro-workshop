# Python for developers - Cheat sheet


**DISCLAIMER:** I am normally a C# developer and my style of coding might not always be following the _"pythonic"_ way. I am no fan of snake case and prefer camelCase for functions and variables and PascalCase for Classes. Even if this might shine trough in this document, you can write the code however you like. If you want to learn Python the _"pythonic"_ way, then use snake case for variables and functions.

This simple cheat sheet is created for Python 3.6.x and above. Some of the language basics shown here is not available for earlier versions of Python.

Python documentation can be found at [docs.python.org](https://docs.python.org/3/). For a reference of the standard library then you can visit the [The Python Standard Library](https://docs.python.org/3/library/index.html). And for a complete reference on the language itself, then [The Python Language Reference](https://docs.python.org/3/reference/index.html) is the place to visit.

## Language basics
It all begins with a simple hello world. Since Python just interprets a script top down, I recommend writing a test to se if the file interpreted is the main file. (The file started directly using `python filename.py` and not a imported file) Python will set the value of one of the ***dunder*** ([Ref](#The-lack-of-private)) variables to `__main__`

Python 3 introduced the print function. In earlier versions of python print was a statement. So when googling you will come across code using the `print` statement. If you want to use this code in Python 3 just replace it with `print()` and that older Python 2 code should work fine.

One of the more larger differences and the most visible one when you come from other languages that follows the C-syntax. Is the lack of curly brackets. In Python different blocks of code are separated by indentations. The official docs says that the indentation should be 4 spaces long. A `tab` will work, but you will be more error prone to the "dreaded" `inconsistent use of tabs and spaces in indentation` error. In this workshop the use of 4 spaces over 1 tab is encouraged.

### Starting scripts

To start the interpretation of a python script just write `python3 <script>.py`. Or if you are following this workshop using the VSCode Dev Container, then just press `F5`.

### Hello World
``` python
if __name__ == "__main__":
    print("Hello world")
```

### Comments
``` python
# Comments are written using the `#` (Pound / Number / Hash / whatever the kids call it today) sign
```

### Type checking
Python is a dynamically typed language. But later versions of python has introduced a option of declaring types for variables, function parameters and function return values. Using types is recommended. In this workshop I will use types in all examples. If you use `pylint` then typing errors will be discovered by the linter.

Python has the following built-in basic types: 
``` Python
str
float
int 
bool
dict
list
set
frozenset
tuple
bytes
```
**Also note** that Python does not have `NULL` but it does have the `None` type that functions in almost the same way.

### Variables
``` python
# Using static type checking
message : str = "Hello World"
print(message)

# Using the "old" dynamic typing
message = "Hello World"
print(message)
```

### Reading console input

``` Python
print("Write your name, finnish by hitting <ENTER>: ", end="")
message : str = input()
print(message)

```

### Concatenation and string interpolation

``` Python
print("Answer the questions. Finnish by hitting <ENTER>")
print("What is your name?: ", end="")
name : str = input()

print("How old are you?: ", end="")
age : str = input()

# Concatenation
print("Hi! " + name + " you are " + age + " years old.")

# String interpolation
print(f"Hi! {name} you are {age} years old.")

# Using str format method
print("Hi! {0} you are {1} years old.".format(name, age))
```

### Basic types
``` Python
# Tuples are immutable
position : tuple = (100, 200)

# Arrays and lists are very similar. Lists are more used.
# If you need to do arithmetic operations on the data, or
# it needs to be stored more efficiently. Use array. If not
# then use list. (Also, arrays are not a "standard" type
# and have to be imported)

# List (Can contain multiple types)
grocerylist : list = ["Milk", "Bread", "Eggs", 13] 

# Array (All items needs to be same type, and type is defined in first argument
#        This all looks like a bad design, and it is. So don't use unless needed for
#        speedy calculations.) Note that strings are not a allowed type. Only numerical
from array import array

groceryarray : array = array("d", [1, 2, 3])

# Set (Duplicate items not allowed so they are ignored)
groceryset : set = set(["Milk", "Bread", "Eggs", "Eggs", 1])
print(groceryset)

# Dictionary
grocerydict : dict = {
    "list": grocerylist,
    "array": groceryarray
}

# Boolean (Note the upper case on the first letter)
needToShop : bool = True #or False

# Float
moneyAvailable : float = 100.50

# Int
numGroceryItems : int = 3

# Str
grocery : str = "Milk"
```

### Conditionals

Conditionals can be written using `if`, `elif` and `else`. You can write the test inside a parenthesis or not. They are optional. In this workshop I will show a test without parenthesis once. All other future conditional tests written will be using parenthesis. This is a matter of personal taste, but I recommend it for readability.

``` Python
testnum : int = 12

# Not using parenthesis   
if testnum == 12:
    print("Number is equal to 12")

if (testnum != 13):
    print("Number is not 13")

if (testnum > 10):
    print("Number is greater than 10")

if (testnum >= 10):
    print("Number is greater or equal to 10")

if (testnum < 20):
    print("Number is less than 20")

if (testnum <= 20):
    print("Number is less than or equal to 20")

if (testnum == 13):
    print("Number is 13")
elif (testnum > 13):
    print("Number is greater than 13")
else:
    print("Number is not equal or greater than 13")
```

#### Lists and "Contains" (`in` and `not in`)
``` Python
grocerylist : list = ["Milk", "Bread", "Eggs", 13] 

if ("Milk" in grocerylist):
    print("Milk is in the grocery list")
else:
    print("Uh oh! You forgot something..")

if ("Butter" not in grocerylist):
    print("You forgot the butter!")
```

#### Boolean operators
Python uses `and` and `or` instead of `&&` and `||`. 
``` Python
testnum : int = 12
teststring : str = "test"

if (testnum > 10 and testnum < 15):
    print("Number is larger than 10 and less than 15")

# Same as above written using "Chained comparison"
if (15 > testnum > 10):
    print("Number is larger than 10 and less than 15")

if (testnum != 10 or teststring != "test"):
    print("Either the number is not 10 or string is not test")

if (testnum != 10 and teststring != "test"):
    print("Number is not 10 and string is not \"test\"")

if(testnum == 12 and teststring == "test"):
    print("Number is 12 and string is \"test\"")
```

### Looping

Note: For loop works somewhat different. There is no `for(;;)` in Python. The `for` keyword loops over iterators. So instead of writing `for(int i = 0; i<10; i++) { /* Something */}` that us Java / C# developers are used to we need to create a list a list containing the numbers 0 to 9. This can be done by using the `range([start: int = 0,] stop: int [, step: int = 1]) -> list` function. This returns a list with the numbers from `start` to `stop` with the `step` between the numbers.

``` Python
grocerylist : list = ["Milk", "Bread", "Eggs", 13]
grocerydict : dict = {
    "list": grocerylist,
    "set": set([1,2,3,4,5])
}

for i in range(10):
    print(i)

for grocery in grocerylist:
    print(grocery)

# Using enumerate()
for index, grocery in enumerate(grocerylist):
    print(f"{grocery} at index {index}")

# NOTE: the ++ operator does not exist in Python.
#       This is a small "gotcha" for many. Use += or -=

i = 0
while i < 10:
    print(i)
    i += 1

# Iterate trough a dictionary using keys
for key in grocerydict.keys():
    print(grocerydict[key])

# Iterate trough a dictionary using items
for key, value in grocerydict.items():
    print(f"{key}: {value}")
```

#### `break` and `continue`

The break and continue keywords, that we are all used to, works just the same in python.

``` Python
for i in range(10):
    if i == 5:
        continue
    print(i)

for i in range(10):
    if i == 5:
        break
    print(i)
```

### Slicing

In Python you can easily slice a list/array/tuple (sequences really, but we will not go into details here) and get sections from it. It is also very easy to reverse it.

To slice a list the following syntax is used: `somelist[start:stop:step]`

``` Python
grocerylist : list = ["Milk", "Bread", "Eggs", "Butter", "Chocolate"] 

# Get first item in list
print(grocerylist[0])

# Use negative indexing to get last item in list
# NOTE: a[-x] can be viewed as a[len(a)-x], this is called "negative indexing"
print(grocerylist[-1])

# Get the two first items in the list
print(grocerylist[:2]) # Same as writing grocerylist[0:2]

# Get every second element
print(grocerylist[0::2])

# Use negative indexing to reverse the list
print(grocerylist[::-1])
```

### Functions

A function is defined using the `def` keyword and the block of code that the function consists of are indented `4 spaces` from the function declaration.

A _"type hint"_ can also be added as a part of the function definition. This will give a "hint" to the users of the function about what type it returns. If you have a linter enabled, then the linter will give you warnings or errors if you are not using correct types. As with typing and variables this is all optional and one of the newer language features.

``` Python
def myFunction() -> None:
    print("Hello from my function")

def addInteger(first: int, second: int) -> int:
    # return keyword just as we are used to
    return first + second

def defaultValues(first: str = "Hello", second: str = "World") -> None:
    print(f"{first} {second}")

if __name__ == "__main__":
    myFunction()
    print(addInteger(2,2))

    defaultValues()
    defaultValues("Learning", "Python")

    # Use arguments out of order by naming the parameter name
    defaultValues(second="Webstep")
```

### Lambdas

Python have recently got support for lambdas expressions. This is not full lambda functions as we are used to in C# and Java. It is used using the `lambda` keyword and the following syntax: `lambda <var>: <body> and returns a anonymous function.

Lambdas is often used together with the built-in `map()`, `filter()` and `reduce()` functions. 

``` Python
numbers : list = [10, 2, 7, 6]

# Add all numbers in the list by one, then create a new list
print(list(map(lambda x: x + 1, numbers)))

# Same as above, just using a anonymous function
lambdaExample = lambda x: x + 1
print(list(map(lambdaExample, numbers)))

# Get all numbers divisible by 2
print(list(filter(lambda x: x % 2 == 0, numbers)))

# Sum all the numbers using reduce
from functools import reduce
print(reduce(lambda sum, num: sum + num, numbers))
```

### List comprehensions

Many of the situations one would use `map()` with `lambda` one could use the more clean list comprehension syntax. The syntax is as follows: `newList = [expression(x) for x in oldList if filter(x)]`. In many cases the filter is not needed and we can simplify it as follows: `newList = [expression(x) for x in oldList]`

``` Python
# Add all numbers in the list by one
print([x + 1 for x in numbers])

# Add all numbers in the list by one if it is divisible by 2
print([x + 1 for x in numbers if x % 2 == 0])
```

### Classes

Python supports both procedural oriented programming as well as object oriented programming.

Classes are declared using the `class` keyword and is very similar to a function definition in that it are declared using parenthesis and can take a optional argument. The optional argument is another class definition that the class will be "inheriting" from.

The constructor is created using the `__init__` dunder method. All class methods has a first parameter named `self` that is a reference to the object instance. This is similar to the `this` keyword in C# and Java, but it is automatically passed as the first argument on any class method. 

Class properties are not declared in advance. They are available as soon as they are used.

#### The lack of private
There is no `public`, `private`, `protected`, etc keywords in Python. All properties and methods of a class is available as `public`. Instead a convention is used to "message" the users that a method or parameter is "private". This is done by encapsulating the property or method name with a double underscore (a "***dunder***"). So a method named `__somePrivateMethod(self, data)__` is considered `private` because of the **dunder** convention. This is same with properties like `self.__somePrivateProperty__ : int = 10`. Most linters will give you a error or a warning if you use any dunder methods outside its "allowed scope". 

``` Python
class Animal():
    def __init__(self, name: str):
        self.name = name

    def makeSound(self):
        print("Unknown sound")

# Dog "inherits" Animal
class Dog(Animal):
    def __init__(self, name: str):
        super().__init__(name)
    
    # Override base method
    def makeSound(self):
        print("Woof")

if __name__ == "__main__":
    dog : Animal = Dog("Balto")

    dog.makeSound()
    print(f"The animals name is: {dog.name}")
```

### Error (Exception) handling

Python handles exceptions using the `try`, `except` and `else` keywords. Code that should run when an exception occurs are put in the `except` block. And code that should only be run if there are no exceptions should be put in the `else` block.

`except` passes an argument that inherits the `BaseException` type. For more information about the Exception and Error types that are built-in you can visit the [Built-in Exceptions](https://docs.python.org/3/library/exceptions.html) page on docs.python.org.

``` Python
prompt: str = "How old are you? " 
agestr: str = input(prompt) 

try: 
    age: int = int(agestr) 
except ValueError: 
    print("You did not enter a integer")      
else: 
    print(f"You are {age} years old")
```

### Math

Python has its own math module as a part of its standard library just as most other languages. There are however some quirks that are original to Python that needs to be addressed. Except for these quirks the math module works as one would expect and is imported using the following import statement: `import math`

In most other languages the power-of operator is the `^` sign. But for Python it is double asterisk `**` signs.

In python you can do "floor division" using the integer division operator `//` directly instead of using `math.floor()` (Not available in Python 2)

``` Python
# One main difference / quirk is how "Power of" is written.
print(f"The 2 in the power of 4 is {2**4}")

# Integer division.
print(f"3 / 4 is {3/4} but using integer division it is {3//4}")
```

### Import system

To import modules and classes from files the `import` keyword is used like this `import X`. To import a specific class (or variable) from a file or module you can use the `from X import Y` syntax. If you want to use an alias for a file, module or a imported part you can use the `as` keyword as such: `import X as Y` or `from X import Y as Z`

``` Python
# Import a module called animals or local file called animals.py
import animals

dog : animals.Animal = animals.Dog("Balto")
dog.makeSound()
print(f"The animals name is: {dog.name}")
```

``` Python
# Import Dog and Animal class from animals.py
from animals import Dog, Animal

dog : Animal = Dog("Balto")
dog.makeSound()
```

``` Python
# Import Dog class aliased as MyDog from animals.py
from animals import Dog as MyDog

dog : MyDog = MyDog("Balto")
dog.makeSound()
```

``` Python
# Import animals.py (or animals module) aliased as A
import animals as A

dog : A.Animal = A.Dog("Balto")
dog.makeSound()
```

More information about import can be read at [The import system](https://docs.python.org/3/reference/import.html) at docs.python.org.

### File IO

As most (if not all?) other languages, Python has built-in IO functions. To open and read or write to files you can use the `open()`, `close()`, `read()` and `write()` functions in a way that is not too unfamiliar if you have ever programmed in C. All files that are opened needs to be closed. But using the `with` keyword Python can automatically close the file when the execution gets out of the scope defined by the `with` keyword.

 ``` Python
file : str = "hello.txt"

# Overwrite the file if it exists
with open(file, "w+") as fileobj:
    fileobj.write("Hello world\n")

with open(file, "r") as fileobj:
    print(fileobj.readlines())

# Append to file
with open(file, "a") as fileobj:
    fileobj.write("Hello again\n")

# Read all lines as a list
with open(file, "r") as fileobj:
    print(fileobj.readlines())

# Read line by line
with open(file, "r") as fileobj:
    for line in fileobj:
        print(line)
```

## Modules

In Python we package our libraries in modules. Modules are in essence just a folder that follows some conventions. Like having a `__init__.py` file that defines the classes, functions and variables that can be imported. But it is mostly based on convention. So if the `__init__.py` file is empty it will still work. (Although the import statement will not be that "clean" and "_pythonic_".)

Covering modules and details about how to best organize your code when writing Python is not in the scope of this workshop. If you want to learn more about modules you can visit the [Modules](https://docs.python.org/3/tutorial/modules.html) site on docs.python.org.

## Packages and Pip

Pip is the defacto package manager for Python. It is used to download libraries and other modules packaged as pip packages. To install a package in your Python environment you can just use the command: `pip install <package>`. For help on how to use pip just type `pip` in your terminal and a helpful help text will be printed in the console.

## Virtual Environments (`venv`)

Virtual Environments are an isolated Python environment that allows packages to be installed for use by a particular application, rather than being installed system wide. So using a Virtual Environment helps us avoid the hassle of conflicts that can arise if you install all your pip packages system wide. Using a Virtual Environment you get a "clean" Python environment to play around with for each project.

You can easily create a new Virtual Environment for your project using the `venv` module shipped in Python 3. The following snippet will create a new Virtual Environment named _devenv_ in the current working folder: `python -m venv devenv` (If multiple versions of Python is install replace `python`with `python3`)

To activate and use the newly created Virtual Environment you need to run the `activate`script suitable for your system. So for Windows based system using CMD you would run `devenv\Scripts\activate.bat`.

For more information about Virtual Environment visit [Creating Virtual Environments](https://packaging.python.org/tutorials/installing-packages/#creating-and-using-virtual-environments) on packaging.python.org.

## Type hints

In this document all functions and variables have been typed using type hints. This is just a personal preference, but I believe that it helps writing less error prone code. If you want to learn more about the support for type hints in Python than these PEPs will give more information:

 - [PEP 483 - The Theory of Type Hints](https://www.python.org/dev/peps/pep-0483)
 - [PEP 484 - Type Hints](https://www.python.org/dev/peps/pep-0484)
 - [PEP 526 - Syntax for Variable Annotations](https://www.python.org/dev/peps/pep-0526)

There is also a more general information available at the official Python documentation:
 
 - [Support for type hints](https://docs.python.org/3/library/typing.html)

## PEP8

PEP8 is the official style guide for Python code. Most linters use this. I personally don't follow PEP8 all the time, but most of its content is very good. Most Python code I have read use this as a guide.

If you want more information and read the guide then you can find it here at [PEP 8 - Style Guide for Python Code](https://www.python.org/dev/peps/pep-0008/).