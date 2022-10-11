# Python Semesters 

<details>

<summary> 

## UNIT 1:
</summary> 

### Explain the features of python.
- Easy-to-learn: Python has few keywords, simple structure, and a clearly defined syntax. This allows the student to pick up the language quickly.
- Python Supports functional and structured programming methods as well as OOP
- Easy-to-maintain: Python's source code is fairly easy-to-maintain
- A broad standard library: Python's bulk of the library is very portable and cross-platform compatible on UNIX, Windows, and Macintosh. 
- Interactive Mode: Python has support for an interactive mode which allows interactive testing and debugging of snippets of code. . 
- Databases: Python provides interfaces to all major commercial databases.
- Python can be dynamically typed which means we don’t need to declare data types in variables in advance like we do in C programming

### Explain debugging and error types in Python.

Programming is error-prone. For whimsical reasons, programming errors are called bugs and the process of tracking them down is called debugging.
Three kinds of errors can occur in a program: Syntax errors, Runtime errors, and Semantic errors.
- Syntax errors:
    - Python can only execute a program if the syntax is correct; otherwise, the interpreter displays an error message.
    - Syntax refers to the structure of a program and the rules about that structure.
    - For example, parentheses have to come in matching pairs, so (1 + 2) is legal, but 8) is a syntax error.

- Runtime errors:
    - A program with a runtime error is one that passed the interpreter’s syntax checks, and started to execute
    - However, during the execution of one of the statements in the program, an error occurred that caused the interpreter to stop executing the program and display an error message
    - Runtime errors are also called **exceptions** because they usually indicate that something exceptional (and bad) has happened.
    - Here are some examples of common runtime errorsr:
    - Misspelled or incorrectly capitalized variable and function names
    - Attempts to perform operations (such as math operations) on data of the wrong type (ex. attempting to subtract two variables that hold string values)

- Semantic errors:
    - The third type of error is the semantic error.
    - If there is a semantic error in your program, it will run successfully in the sense that the computer will not generate any error messages, but it will not do the right thing.
    - It will do something else. The problem is that the program you wrote is not the program you wanted to write.
    - The meaning of the program (its semantics) is wrong.
    - Identifying semantic errors can be tricky because it requires you to work backward by looking at the output of the program and trying to figure out what it is doing

### Write a short note on formal and natural languages.

| **Natural Language** | **Formal Language** |
| :--: | :--: |
| Natural languages are the languages that people speak, such as English, Spanish, Korean, and Mandarin Chinese. They were not designed by people (although people try to impose some order on them); they evolved naturally. | Formal languages are languages that are designed by people for specific applications. For example, the notation that mathematicians use is a formal language that is particularly good at denoting relationships among numbers and symbols. Chemists use a formal language to represent the chemical structure of molecules. |
| Natural languages are full of ambiguity, which people deal with by using contextual clues and other information | Formal languages are designed to be nearly or completely unambiguous, which means that any statement has exactly one meaning, regardless of context. |
| In order to make up for ambiguity and reduce misunderstandings, natural languages employ lots of redundancy. As a result, they are often verbose (lengthy/wordy). | Formal languages are less redundant and more concise | 
| Natural languages are full of idiom and metaphor. If I say, “The penny dropped,” there is probably no penny and nothing dropping (this idiom means that someone realized something after a period of confusion). | Formal languages mean exactly what they say. |



### Write a short note on Python Data Types.
### Explain operators in python with suitable example (5 opeerators)
### Write a program to use membership and Indetity operators.
### Explain Compilar and Interpreter.
### Short note on conditional statements. Write a short program to demonstrate the same.
### Short note on looping statemetns in python. Write a short program to demonstrate the same.
</details>

<details> 
<summary>

## UNIT 2:
</summary> 

### Explain any 5 math functions in Python in detail.
### Explain parameteres and arguments with proper example

The terms parameter and argument can be used for the same thing: information that are passed into a function.
From a function's perspective:
- A parameter is the variable listed inside the parentheses in the function definition.
- An argument is the value that are sent to the function when it is called.
    Key Terms:
    - argument-A value provided as input to a function.
    - parameter-A variable identifier provided as input to a function.
eg:-
```py
def my_function(a,c):
	print(a + " " + c)
my_function("b")
```

### Explain the difference between import module and form module.
### Write a short program to demonstrate use of function returning value.
### Explain any 5 string methods or Explain any 5 built in functions.
### Explain the string operators with the help of different operator.
### Explain the use of "in" and "not" operator.
### Write a program to use various list methods and function.
### Explain any 5 built in list function methods.
### Explain any built list operators.

</details>



<details> 
<summary>

## UNIT 3:
</summary> 

### Explain indexing, negative indexing and slicing with respect to tuple.
### Write short note on built in tuple function.

- cmp(tuple1, tuple2) - It compares two tuples and returns true if tuple1 is greater than tuple2 otherwise false.
- len(tuple) - It calculates the length of the tuple.
- max(tuple) - It returns the maximum element of the tuple
- min(tuple - It returns the minimum element of the tuple.
- tuple(seq) - It converts the specified sequence to the tuple.

### Explain basic tuple operations.
### Explain tuple and dictionary with program.
### Explain built in dictionary function.

- cmp(dict1,dict2)-It compares the items of both the dictionary and returns true if the first dictionary values are greater than the second dictionary, otherwise it returnfalse.
- len(dict)-It is used to calculate the length of the dictionary.
- str(dict) -It converts the dictionary into the printable string representation.
- type(variable) -It is used to print the type of the passed variable.

### Explain any 5 built dictionary methods.

- dict.clear() It is used to delete all the items of the dictionary.
- dict.copy() It returns a shallow copy of the dictionary.
- dict.items() It returns all the key-value pairs as a tuple.
- dict.keys() It returns all the keys of the dictionary.
- dict.values() It returns all the values of the dictionary.

### Explain any 5 built in exception.

- ArithmeticError- Raised when an error occurs in numeric calculations
- FloatingPointError-Raised when a floating point calculation fails
- ImportError-Raised when an imported module does not exist
- KeyError-Raised when a key does not exist in a dictionary
- MemoryError-Raised when a program runs out of memory
- NameError-Raised when a variable does not exist
- SyntaxError-Raised when a syntax error occurs
- SystemExit-Raised when the sys.exit() function is called

### Explain exception with args with proper example.
### What is file & What are its operating modes.
### Write a short note to demonstate exception handling in python.
### What is directory? Which methods are available to deal with dierectories in python?
</details>


<details> 
<summary>

## UNIT 4:
</summary> 

### Explain match function. Give simple example.
### What is multithreading? Write a short note on thread module.
### Explain random module with its any five function.
### Explain time modue with any S function.
### What are modules? How is it used? What are its advantages?
### Write a short note on class and 
### what is OOPS? Explain a Concepts of OOP in short.
### List and explain built in class attributes.
### Explain the constructor.
### Write a short program to demonstrate the use of multiple inheritance.
</details>


<details> 
<summary>

## UNIT 5:
</summary> 

### What is GUI? Explain its advantage.
### Write a note on standard dimension attributes on tkinter module.
### Write a short note on anchor and relief attribute in python GUI.
### Write a short note on menu button.
### Explain entry and text widget with small example.
### What is message box? What are its types.
### Write a detailed note on canvas widget.
### What is layout management? What are geometry managers in python.
### How to connect MySQL database using python.
### Write a small porgram to create a table and insert values in MySQL data base using python GUI Application.
### write a small program to reterive value from MySQL database using python GUI application.
</details>


Install Python - <a href="https://www.python.org/downloads/">Python Download</a> 
<br>
<br>
Copyright (c) 2022 Reuben George under [MIT License](./license). 
