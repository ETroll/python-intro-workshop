# Python for developers - Cheat sheet

//TODO: Write a few lines about python. The main difference is a 4 spaces indentations instead of 
curly brackets to create code blocks / scopes.

This simple cheat sheet is created for Python 3.6.x and above. Some of the language basics shown here is not available for earlier versions of Python.

## Language basics
It all begins with a simple hello world. Since Python just interprets a script top down, I recommend writing a test to se if the file interpreted is the main file. (The file started directly using `python filename.py` and not a imported file) Python will set the value of one of the ***dunder*** ([Ref](#Dunder)) variables to `__main__`

Python 3 introduced the print function. In earlier versions of python print was a statement. So when googling you will come across code using the `print` statement. If you want to use this code in Python 3 just replace it with `print()` and that older Python 2 code should work fine.

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

Note: For loop works somewhat different. There is no `for(;;)` in Python. For loops over iterators. So instead of writing `for(int i = 0; i<10; i++) { /* Something */}` that us Java / C# developers are used to we need to create a list a list containing the numbers 0 to 9. This can be done by using the `range([start: int = 0,] stop: int [, step: int = 1]) -> list` function. This returns a list with the numbers from `start` to `stop` with the `step` between the numbers.

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





## Modules

## Packages and Pip

## Virtual Environments (`venv`)

## PEP8


``` Python


```
 - Language basics



    - Other
        - Try / catch
        - With
        - Slicing of lists
            - Negative indexing
                - a[-X] can be viewed as a[len(a)-X]
            - Show example of slicing where negative step (::-1) is used
        - Pass - the "null/noop operation".

    - Math
        - Most notably difference: ** is power of. Not ^ as others
        - Integer division quirk. 3/4 => 0, 3/4. => 0.75. (Use // - Only Python 3)

    - None == NULL
    - Functions
        - Def keyword
        - Default parameters
    - Objects and classes
        - object
        - dunder init (ctor) `__init__`
        - self is first paramter of all class methods
        - inheritance => subclassing
    - File IO
        - open/close
        - use the with keyword for implicit closing of io :)
    - Lambdas
    - PEP 8 (Have a read, but we will not go into details here now)
 - Modules
 - Pip / Packages
 - Venv
 - Common "gotcha's" for java/c# devs
  - No ++ operator!