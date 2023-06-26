# Data Type of Python
This repository contains all the data types of python and all methods of data types with examples. These functions or methods will help you to build different types of short programmes
or run operations on huge database. I hope I could teach you something 🤗🙂.


## Strings
There are 47 methods or functions for strings. Strings are a group of characters(a, b, c, 1, 2, !, &). They are surrounded by quotes. They are often used to store names, passwords etc. 
For example, "Ron", "Jil", "S*q15~" ect. They all are strings.


### 1. capitalize()
This function will capitalize the whole string. Suppose there is a variable named 'text', which contains a string, "hello EVERYONE". Now when you print the variable 'text', we will 
place a dot then we will call the capitalize function by writing `capitalize()`. Your code may look like this ⬇
``` python
text = "hello EVERYONE"
print(text.capitalize())
```
NOW run the code. You will see
``` pyhon
"Hello Everyone"
```

### 2. casefold()
This function will turn a string in a format, which we can easily use in the program without any errors. Suppose there are two variable named 'text1' and 'text2', text1 contains "heLLo"
and text2 contains "HELlo". Now when you print the variable 'text1', we will place a dot then we will call the casefold function by writing `casefold()` and same for 'text2'. Your code 
may look like this ⬇
``` python
text1 = "heLLo"
text1 = "HELlo"
print(text1.casefold())
print(text2.casefold())
```
NOW run the code. You will see
``` pyhon
'hello'
'hello'
```

### 3. center()
This function will align the text center. We have give it a full-integer value, so it surround the text with space or we giv it anything like "_". Suppose there is a variable named 
'tex3', text3 contains "DJ". Now when you print the variable 'text3', we will place a dot then we will call the center function by writing `center()`. Then we will give a value like 20 in the brackets. Your code may look like this ⬇
``` python
text3 = "DJ"
print(text3.center(20, "_"))
```
NOW run the code. You will see
``` pyhon
_ _ _ _ _ _ _ _ _ DJ _ _ _ _ _ _ _ _ _
```

### 4. count()
This function will count the appearance of a string in a string. Suppose there is a variable named 'tex4', text4 contains "abc_abc_abc_abc_abc". Now when you print the variable 'text4', 
we will place a dot then we will call the center function by writing `count()`.Then we will give the string in the brackets. Your code may look like this ⬇
``` python
text4 = "abc_abc_abc_abc_abc"
print(text4.center(ab))
```
NOW run the code. You will see
``` pyhon
5
```
