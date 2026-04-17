questions = {
    1: [   
        {
            "qnum": 1,
            "type": "mcq",
            "text": "How to print 'Hello World' in Python?",
            "options": {
                "a": 'HelloWorld("print")',
                "b": 'Print("Hello World")',
                "c": 'print("Hello World")',
                "d": 'print(Hello World)'
            },
            "correct": "c",
            "explanation": "print() must be lowercase and the message must be inside quotes."
        },
        {
            "qnum": 2,
            "type": "mcq",
            "text": "How to print the integer 5 in Python?",
            "options": {
                "a": "print int 5",
                "b": "print(5)",
                "c": "Print 5",
                "d": "display(5)"
            },
            "correct": "b",
            "explanation": "print(5) is the correct syntax for printing a number."
        },
        {
            "qnum": 3,
            "type": "mcq",
            "text": "How to correctly print a string and an integer?",
            "options": {
                "a": 'Print("The score is" 7)',
                "b": 'print("The score is", 7)',
                "c": 'print("The score is" 7)',
                "d": 'print("The score is" + 7)'
            },
            "correct": "b",
            "explanation": 'print("text", value) is the correct way.'
        }
    ],

    2: [   
        {
            "qnum": 1,
            "type": "mcq",
            "text": "Which is a valid syntax to define a variable in Python?",
            "options": {
                "a": 'user_name : "Alice"',
                "b": 'user_name == "Alice"',
                "c": 'user_name = "Alice"',
                "d": 'user_name - "Alice"'
            },
            "correct": "c",
            "explanation": "Variables are created using = for assignment."
        },
        {
            "qnum": 2,
            "type": "mcq",
            "text": "How do you create a constant variable in Python?",
            "options": {
                "a": "Capitalize the first letter only",
                "b": "Capitalize ALL letters, e.g., MAX_SPEED",
                "c": "Use the const keyword",
                "d": "Include at least one number in the name"
            },
            "correct": "b",
            "explanation": "Python has no true constants, but ALL_CAPS naming is the convention."
        },
        {
            "qnum": 3,
            "type": "mcq",
            "text": "What is a variable in Python?",
            "options": {
                "a": "A name that stores a value",
                "b": "An arithmetic operator",
                "c": "A number that never changes",
                "d": "A folder that stores your files"
            },
            "correct": "a",
            "explanation": "A variable is just a label referring to stored data."
        },
        {
            "qnum": 4,
            "type": "mcq",
            "text": "Which variable name follows proper Python naming rules?",
            "options": {
                "a": "2score",
                "b": "player-score",
                "c": "player_score",
                "d": "player score"
            },
            "correct": "c",
            "explanation": "Python variables must not start with a number and cannot contain spaces or hyphens."
        },
        {
            "qnum": 5,
            "type": "code",
            "text": 'Assign the value "Alice" to a variable called name.',
            "starter": "name = ",
            "test": "name == 'Alice'",
            "hint": "Remember: variables are assigned using = and strings require quotes.",
            "explanation": "Variables are assigned using = and strings use quotes."
        }

    ],
    3: [   
        {
            "qnum": 1,
            "type": "code",
            "text": "Assume that a variable called 'age' is defined. Write code to check if age is greater than 18, and print 'You are older than 18' if true.",
            "setup": "age = 20",
            "test": "('You are older than 18' in __output__) or (age > 18 and 'older' in __output__)",
            "hint": "Use: if age > 18:",
            "explanation": "Use a comparison operator (>) inside an if-statement."
        },
        {
            "qnum": 2,
            "type": "mcq",
            "text": "Which condition correctly checks if 'number' is between 0 and 100 (inclusive)?",
            "options": {
                "a": "if 0 <= number <= 100:",
                "b": "if 0 <= number:",
                "c": "if number <= 100:",
                "d": "if number >= 100:"
            },
            "correct": "a",
            "explanation": "Python allows chained comparisons like 0 <= number <= 100."
        },
        {
            "qnum": 3,
            "type": "code",
            "text": "Assume a variable called 'name' is defined. Check if the name is 'Alice' and print 'Hello Alice'.",
            "setup": "name = 'Alice'",
            "test": "('Hello Alice' in __output__) or (name == 'Alice' and 'Hello' in __output__)",
            "hint": "Use == for equality comparison.",
            "explanation": "Strings must match exactly, and == checks equality."
        }
    ],
    4: [
        {
            "qnum": 1,
            "type": "mcq",
            "text": "What is the correct while loop syntax in Python?",
            "options": {
                "a": "DoWhile condition:",
                "b": "While condition:",
                "c": "while condition:",
                "d": "while true condition:"
            },
            "correct": "c",
            "explanation": "Python uses lowercase 'while' followed by a condition and a colon."
        },
        {
            "qnum": 2,
            "type": "mcq",
            "text": "What can a bad condition cause in a while loop?",
            "options": {
                "a": "Infinite loop",
                "b": "The computer shuts down automatically",
                "c": "The loop prints random numbers",
                "d": "The program runs slowly"
            },
            "correct": "a",
            "explanation": "A condition that never becomes false causes an infinite loop."
        },
        {
            "qnum": 3,
            "type": "mcq",
            "text": "What is the correct way to increment a counter variable inside a while loop so the loop eventually stops?",
            "options": {
                "a": "counter ++",
                "b": "counter = 1",
                "c": "counter = counter + 1",
                "d": "counter ++ 1"
            },
            "correct": "c",
            "explanation": "counter = counter + 1 increases the value by 1 each loop."
        }
    ],
    5: [
        {
            "qnum": 1,
            "type": "mcq",
            "text": "What can a for loop iterate through?",
            "options": {
                "a": "an integer",
                "b": "a character",
                "c": "any iterable collection (lists, strings, etc.)",
                "d": "None of the above"
            },
            "correct": "c",
            "explanation": "A for loop iterates over any iterable object, such as lists, strings, tuples, etc."
        },
        {
            "qnum": 2,
            "type": "mcq",
            "text": "What is a valid for loop syntax?",
            "options": {
                "a": "for i in range 5",
                "b": "for i in range(10):",
                "c": "for i in while 10:",
                "d": "for i in 10"
            },
            "correct": "b",
            "explanation": "for i in range(10): uses correct Python loop syntax with parentheses and a colon."
        },
        {
            "qnum": 3,
            "type": "code",
            "text": "Print numbers 0, 1, 2 using a for loop",
            "setup": "",
            "test": "__output__.strip() == '0\\n1\\n2'",
            "hint": "range(3) produces 0, 1, 2.",
            "explanation": "range(3) generates 0, 1, and 2, so print(i) outputs them each on a new line."
        }
    ],
    6: [
        {
            "qnum": 1,
            "type": "mcq",
            "text": "What is a valid syntax to print two strings?",
            "options": {
                "a": 'print("Hello", "how are you?")',
                "b": 'print("Hello" - "how are you?")',
                "c": 'Print("hello", "how are you?")',
                "d": 'print("Hello" _ "how are you?")'
            },
            "correct": "a",
            "explanation": "print() accepts multiple arguments separated by commas."
        },
        {
            "qnum": 2,
            "type": "mcq",
            "text": "What can be printed in Python?",
            "options": {
                "a": "Variables",
                "b": "Strings",
                "c": "Integers",
                "d": "All of the above"
            },
            "correct": "d",
            "explanation": "Python can print variables, strings, integers, and many other data types."
        },
        {
            "qnum": 3,
            "type": "code",
            "text": 'Write code that prints "Hello World" in Python.',
            "setup": "",
            "test": "__output__.strip() == 'Hello World'",
            "hint": "Use the print() function.",
            "explanation": 'print("Hello World") is the correct syntax using double quotes.'
        }
    ],


    7: [
        {
            "qnum": 1,
            "type": "mcq",
            "text": "Which of the following is a Boolean variable?",
            "options": {
                "a": 'var = "True"',
                "b": "var = False",
                "c": "var = 20",
                "d": "var = 20.5"
            },
            "correct": "b",
            "explanation": "Booleans are True or False without quotes."
        },
        {
            "qnum": 2,
            "type": "mcq",
            "text": "Which of the following is an integer?",
            "options": {
                "a": "var = 17",
                "b": 'var = "17"',
                "c": "var = 17.0",
                "d": 'var = "17.0"'
            },
            "correct": "a",
            "explanation": "17 is a whole number without quotes or decimal."
        },
        {
            "qnum": 3,
            "type": "mcq",
            "text": "What are variables used for in Python?",
            "options": {
                "a": "printing data",
                "b": "storing data",
                "c": "displaying data",
                "d": "writing functions"
            },
            "correct": "b",
            "explanation": "Variables store data in memory so your program can use it later."
        }
    ],
    8: [
        {
            "qnum": 1,
            "type": "mcq",
            "text": 'Which operator in Python means "not equal to"?',
            "options": {
                "a": "==",
                "b": "!=",
                "c": "not ==",
                "d": "!=="
            },
            "correct": "b",
            "explanation": "!= is the correct operator for 'not equal to' in Python."
        },
        {
            "qnum": 2,
            "type": "mcq",
            "text": "What can you use if you need more than just one if and one else?",
            "options": {
                "a": "use elif",
                "b": "use multiple elses",
                "c": "use multiple ifs",
                "d": "none of the above"
            },
            "correct": "a",
            "explanation": "elif allows you to add additional conditions between if and else."
        },
        {
            "qnum": 3,
            "type": "code",
            "text": 'Assume variable "temperature" is defined. Use conditionals to print "It is warm outside" if temperature is greater than 25, else print "It is cold outside".',
            "setup": "temperature = 30",
            "test": "'It is warm outside' in __output__",
            "hint": "Start with: if temperature > 25:",
            "explanation": "Use if/else to check the temperature and print the appropriate message."
        }
    ], 
    9: [
        {
            "qnum": 1,
            "type": "mcq",
            "text": "What does a while loop do?",
            "options": {
                "a": "Run code only once",
                "b": "Repeats code as long as the condition is true",
                "c": "Only runs when the user presses a key",
                "d": "Stops the program immediately"
            },
            "correct": "b",
            "explanation": "A while loop continues running as long as its condition evaluates to True."
        },
        {
            "qnum": 2,
            "type": "code",
            "text": "Assume a variable 'counter' is defined and is a positive integer. Write a while loop that decrements counter by 1 until it reaches 0.",
            "setup": "counter = 3",
            "test": "counter == 0",
            "hint": "Use: while counter > 0: and then decrease it inside the loop.",
            "explanation": "A proper while loop must update the loop variable, otherwise it becomes infinite."
        },
        {
            "qnum": 3,
            "type": "mcq",
            "text": "What can cause an infinite while loop?",
            "options": {
                "a": "Using print() inside the loop",
                "b": "Changing the loop variable every time",
                "c": "Never changing the variable used in the loop's condition",
                "d": "Using a colon (:) after the while statement"
            },
            "correct": "c",
            "explanation": "If the loop variable never changes, the condition never becomes false, making the loop infinite."
        }
    ],
    10: [
        {
            "qnum": 1,
            "type": "mcq",
            "text": "What is the for loop used for?",
            "options": {
                "a": "Repeating a code an unknown number of times",
                "b": "Repeating a code a specific number of times or going through each item in a collection",
                "c": "Stopping a loop from running",
                "d": "Repeating code only once"
            },
            "correct": "b",
            "explanation": "For loops are ideal for looping a specific number of times or iterating through items in an iterable."
        },
        {
            "qnum": 2,
            "type": "code",
            "text": "Write a for loop that loops through a range of integers from 0 to 10 and prints each integer on a new line.",
            "setup": "",
            "test": "__output__.strip() == '0\\n1\\n2\\n3\\n4\\n5\\n6\\n7\\n8\\n9\\n10'",
            "hint": "Use: for i in range(0, 11):",
            "explanation": "range(0, 11) generates numbers 0 through 10 inclusive."
        },
        {
            "qnum": 3,
            "type": "mcq",
            "text": "What function is commonly used in the for loop?",
            "options": {
                "a": "min()",
                "b": "abs()",
                "c": "range()",
                "d": "max()"
            },
            "correct": "c",
            "explanation": "range() is used to generate a sequence of numbers for looping."
        }
    ],

    11: [
        {
            "qnum": 1,
            "type": "mcq",
            "text": 'What does the slice "This is a full sentence!"[10:14] return?',
            "options": {
                "a": '"sentence"',
                "b": '"full"',
                "c": '"This"',
                "d": '"is a"'
            },
            "correct": "b",
            "explanation": '"This is a full sentence!"[10:14] returns "full" because characters at index 10,11,12,13 spell "full".'
        },
        {
            "qnum": 2,
            "type": "mcq",
            "text": "What happens if you try to combine a string and an integer without casting the integer to a string?",
            "options": {
                "a": "An integer is automatically converted to a string by Python",
                "b": "It causes an error",
                "c": "The integer gets ignored",
                "d": "None of the above"
            },
            "correct": "b",
            "explanation": "Python does NOT automatically turn integers into strings. Trying to concatenate them causes a TypeError."
        },
        {
            "qnum": 3,
            "type": "code",
            "text": 'Assume a variable "name" is defined and has more than 10 characters. Use string slicing to print the first three characters of the string.',
            "setup": "name = 'abcdefghijk'",  
            "test": "__output__.strip() == name[:3]",
            "hint": "Use slicing: name[:3]",
            "explanation": "name[:3] returns the first three characters of the string."
        }
    ],

    12: [
        {
            "qnum": 1,
            "type": "mcq",
            "text": "What is the appropriate way to define an empty list?",
            "options": {
                "a": "newList = List()",
                "b": "newList = []",
                "c": "newList = [0]",
                "d": "newList is List(empty)"
            },
            "correct": "b",
            "explanation": "[] creates a new empty list in Python."
        },
        {
            "qnum": 2,
            "type": "mcq",
            "text": "How can we add an element to the end of a list?",
            "options": {
                "a": "Use .append()",
                "b": "Use .add()",
                "c": "Add the element to the list with an addition sign (+)",
                "d": "We can’t; there is no way to change a list once we created it."
            },
            "correct": "a",
            "explanation": ".append() adds a new element to the end of a list."
        },
        {
            "qnum": 3,
            "type": "mcq",
            "text": "How can you see the first element in a list?",
            "options": {
                "a": "myList[1]",
                "b": "myList.first()",
                "c": "myList[0]",
                "d": "firstIn(myList)"
            },
            "correct": "c",
            "explanation": "Lists are zero-indexed, so the first element is at index 0."
        }
    ],
    13: [
        {
            "qnum": 1,
            "type": "mcq",
            "text": "Assuming myDictionary is a real dictionary, what will the line myDictionary['banana'] = 'yellow' do?",
            "options": {
                "a": "Add a new key-value pair of 'banana': 'yellow'",
                "b": "Update the value of the key 'banana' to be 'yellow'",
                "c": "A or B are correct, depending on whether the key 'banana' exists yet",
                "d": "This line causes an error"
            },
            "correct": "c",
            "explanation": "If 'banana' doesn't exist, it creates the key. If it already exists, it updates it."
        },
        {
            "qnum": 2,
            "type": "mcq",
            "text": "What symbols do we use to hold a dictionary?",
            "options": {
                "a": "The square brackets [ ]",
                "b": "The parenthesis ( )",
                "c": "The curly braces { }",
                "d": "The angle symbols < >"
            },
            "correct": "c",
            "explanation": "Dictionaries in Python use curly braces: { key: value }"
        },
        {
            "qnum": 3,
            "type": "mcq",
            "text": "Which of the following is not valid to perform on a dictionary?",
            "options": {
                "a": "myDictionary.values()",
                "b": "myDictionary.keys()",
                "c": "myDictionary['someKey']",
                "d": "myDictionary.findKey('someKey')"
            },
            "correct": "d",
            "explanation": "Dictionaries do not have a method called findKey(). keys(), values(), and indexing are all valid."
        }
    ],
    14: [
        {
            "qnum": 1,
            "type": "mcq",
            "text": "What is the proper way to define a function called myFunction that takes no parameters?",
            "options": {
                "a": "def myFunction():",
                "b": "def myFunction(takes no parameters):",
                "c": "define function called myFunction:",
                "d": "def myFunction(None):"
            },
            "correct": "a",
            "explanation": "Functions in Python are defined using def functionName(): with parentheses even if empty."
        },
        {
            "qnum": 2,
            "type": "mcq",
            "text": "What is the keyword we use that allows the function to give something back to the rest of the program?",
            "options": {
                "a": "gives",
                "b": "return",
                "c": "respondsWith()",
                "d": "Functions cannot share any information"
            },
            "correct": "b",
            "explanation": "The return keyword sends a value back to the caller."
        },
        {
            "qnum": 3,
            "type": "mcq",
            "text": "How can I signal to Python that my function has an optional parameter?",
            "options": {
                "a": "Set the parameter equal to something, for example myFunc(parameter=0)",
                "b": "Put the default parameter directly in the parentheses, for example myFunc(param=0)",
                "c": "Put the optional parameter after the parentheses, for example myFunc(parameter) where parameter = 0",
                "d": "There is no way to make a parameter optional in Python"
            },
            "correct": "b",
            "explanation": "Optional parameters are created using default values inside the parentheses: def func(x=0)."
        }
    ],
    15: [
        {
            "qnum": 1,
            "type": "mcq",
            "text": "Which of the following correctly uses an f-string to print a variable 'name'?",
            "options": {
                "a": "print(\"Name: {name}\")",
                "b": "print(f\"Name: name\")",
                "c": "print(f\"Name: {name}\")",
                "d": "print(f:Name: {name})"
            },
            "correct": "c",
            "explanation": "F-strings require f\"...{variable}...\" to insert variables."
        },

        {
            "qnum": 2,
            "type": "mcq",
            "text": "What will the following code output: print(\"A\", \"B\", \"C\", sep=\"-\")?",
            "options": {
                "a": "A B C",
                "b": "A-B-C",
                "c": "A-B C",
                "d": "A B-C"
            },
            "correct": "b",
            "explanation": "The sep argument replaces spaces between printed items."
        },

        {
            "qnum": 3,
            "type": "mcq",
            "text": "Which escape character creates a new line in a printed string?",
            "options": {
                "a": "\"\\t\"",
                "b": "\"\\\\\"",
                "c": "\"\\n\"",
                "d": "\"\\new_line\""
            },
            "correct": "c",
            "explanation": "\\n is the escape sequence for a new line."
        }

    ],
    16: [
        {
            "qnum": 1,
            "type": "mcq",
            "text": "Which data type is stored in the following variable: status = True?",
            "options": {
                "a": "Integer",
                "b": "Boolean",
                "c": "String",
                "d": "Float"
            },
            "correct": "b",
            "explanation": "True and False are Boolean values in Python."
        },

        {
            "qnum": 2,
            "type": "mcq",
            "text": "Which line of code assigns three variables at once correctly?",
            "options": {
                "a": "x = 1; y = 2; 3 = z;",
                "b": "x, y, z = 1, 2, 3",
                "c": "x = (1, 2, 3)",
                "d": "x y z = 1 2 3"
            },
            "correct": "b",
            "explanation": "Python allows multiple assignment using commas on both sides."
        },

        {
            "qnum": 3,
            "type": "mcq",
            "text": "What does the type() function do?",
            "options": {
                "a": "Converts a value to a string",
                "b": "Prints the variable name",
                "c": "Shows the data type of a value",
                "d": "Deletes a variable"
            },
            "correct": "c",
            "explanation": "type() returns the data type of a variable or value."
        }

    ],

    17: [
        {
            "qnum": 1,
            "type": "mcq",
            "text": "Which statement is true about an if-elif-else statement?",
            "options": {
                "a": "Only one block of code in the chain will run",
                "b": "All blocks in the chain run sequentially",
                "c": "elif is optional but else is required",
                "d": "else must always come first"
            },
            "correct": "a",
            "explanation": "An if-elif-else chain stops after the first true condition."
        },

        {
            "qnum": 2,
            "type": "mcq",
            "text": "Which logical operator checks if both conditions are true?",
            "options": {
                "a": "or",
                "b": "and",
                "c": "not",
                "d": "in"
            },
            "correct": "b",
            "explanation": "The 'and' operator requires both conditions to be true."
        },

        {
            "qnum": 3,
            "type": "code",
            "text": "Assume the list named colors is defined. Write a line of code using 'in' to check if 'red' is a part of the list.",
            "starter": "colors = ['red', 'blue', 'green']",
            "test": "'True' in __output__",
            "hint": "Use: if \"red\" in colors:",
            "explanation": "The 'in' keyword checks whether an item exists in a list."
        }

    ],
    18: [
        {
            "qnum": 1,
            "type": "mcq",
            "text": "What does the break statement do in a while loop?",
            "options": {
                "a": "Pauses the loop temporarily",
                "b": "Skips the current iteration of the loop",
                "c": "Stops the loop immediately",
                "d": "Resets the loop counter"
            },
            "correct": "c",
            "explanation": "break ends the loop instantly, regardless of the condition."
        },

        {
            "qnum": 2,
            "type": "mcq",
            "text": "What will happen if the loop condition in a while loop never becomes False?",
            "options": {
                "a": "The loop will stop automatically after some time",
                "b": "The loop will run forever (infinite loop)",
                "c": "Python will throw a syntax error",
                "d": "The program will skip the loop"
            },
            "correct": "b",
            "explanation": "A condition that never becomes False causes an infinite loop."
        },

        {
            "qnum": 3,
            "type": "mcq",
            "text": "Which of the following is True about a nested while loop?",
            "options": {
                "a": "The inner loop runs only once",
                "b": "The inner loop runs completely for each iteration of the outer loop",
                "c": "The outer loop cannot use break if there is an inner loop",
                "d": "Nested loops always create infinite loops"
            },
            "correct": "b",
            "explanation": "In nested loops, the inner loop runs fully for every iteration of the outer loop."
        }

    ],
    19: [
        {
            "qnum": 1,
            "type": "mcq",
            "text": "How do you loop through a list of fruits using a for loop in Python?",
            "options": {
                "a": "for fruit in fruits:",
                "b": "while fruit in fruits:",
                "c": "if fruit in fruits:",
                "d": "for i in range(fruits):"
            },
            "correct": "a",
            "explanation": "Lists are iterated using: for item in list."
        },

        {
            "qnum": 2,
            "type": "mcq",
            "text": "What does range(1, 10, 2) generate?",
            "options": {
                "a": "1,2,3,4,5,6,7,8,9",
                "b": "1,3,5,7,9",
                "c": "0,1,2,3,4,5,6,7,8,9",
                "d": "2,4,6,8,10"
            },
            "correct": "b",
            "explanation": "range(start, stop, step) → starts at 1, stops before 10, stepping by 2."
        },

        {
            "qnum": 3,
            "type": "code",
            "text": "Write a for loop to print all even numbers from 2 to 10 inclusive.",
            "starter": "",
            "test": "all(str(n) in __output__ for n in [2,4,6,8,10])",
            "hint": "Use: for i in range(2, 11, 2):",
            "explanation": "range(2, 11, 2) generates even numbers between 2 and 10."
        }
    ],
    20: [
        {
            "qnum": 1,
            "type": "mcq",
            "text": "Which string method converts all letters to uppercase?",
            "options": {
                "a": ".lower()",
                "b": ".capitalize()",
                "c": ".title()",
                "d": ".upper()"
            },
            "correct": "d",
            "hint": "Uppercase letters are created using .upper().",
            "explanation": "The .upper() method converts all alphabetic characters in a string to uppercase."
        },
        {
            "qnum": 2,
            "type": "mcq",
            "text": "What does data.strip() do if data = '   Python Programming      '?",
            "options": {
                "a": "Removes only left spaces",
                "b": "Removes only right spaces",
                "c": "Removes both leading and trailing spaces",
                "d": "Removes all spaces in the middle"
            },
            "correct": "c",
            "hint": "strip() removes whitespace from both ends.",
            "explanation": "The strip() method removes whitespace from the beginning and end of a string, not the middle."
        },
        {
            "qnum": 3,
            "type": "mcq",
            "text": "Assume the variable phrase is defined. Which slice gives the last 3 characters of the string?",
            "options": {
                "a": "phrase[3:]",
                "b": "phrase[-3:]",
                "c": "phrase[:3]",
                "d": "phrase[0:3]"
            },
            "correct": "b",
            "hint": "Negative indexing counts from the end.",
            "explanation": "phrase[-3:] returns the last three characters of a string."
        }
    ],

    21: [
        {
            "qnum": 1,
            "type": "mcq",
            "text": "The list myList exists and contains ['banana', 'apple', 'mango']. What is an appropriate way to access the value 'apple'?",
            "options": {
                "a": "myList[1]",
                "b": "myList[-2]",
                "c": "myList[2]",
                "d": "Both a and b are correct"
            },
            "correct": "d",
            "hint": "Remember: index 1 is the second item, and negative indices count from the end.",
            "explanation": "myList[1] returns 'apple'. myList[-2] also returns 'apple' because it is the second-to-last element."
        },
        {
            "qnum": 2,
            "type": "mcq",
            "text": "How can we add a single item to a list?",
            "options": {
                "a": "theList.append(item)",
                "b": "theList.add(item)",
                "c": "theList.push(item)",
                "d": "add item to theList;"
            },
            "correct": "a",
            "hint": "Think about the method used to add an element to the end of a list.",
            "explanation": "append() adds a single item to the end of a list. The other options are not valid Python syntax."
        },
        {
            "qnum": 3,
            "type": "mcq",
            "text": "What is printed if we have theList = [1, 2, 3] and we perform print(theList.pop())?",
            "options": {
                "a": "[1, 2]",
                "b": "3",
                "c": "1",
                "d": "pop does not return anything"
            },
            "correct": "b",
            "hint": "pop() removes and RETURNS the last item of the list.",
            "explanation": "pop() returns the last element, which is 3. It also removes it from the list."
        }
    ],

    22: [
        {
            "qnum": 1,
            "type": "mcq",
            "text": "How can we define an empty dictionary?",
            "options": {
                "a": "emptyDict = {}",
                "b": "emptyDict = Dictionary()",
                "c": "emptyDict = []",
                "d": "emptyDict = ."
            },
            "correct": "a",
            "hint": "Remember: dictionaries use curly braces.",
            "explanation": "An empty dictionary is created using {}. The other forms are not valid Python syntax for a dictionary."
        },
        {
            "qnum": 2,
            "type": "mcq",
            "text": "What is the correct way to get a list of the values of a dictionary?",
            "options": {
                "a": "dictionary.keys()",
                "b": "dictionary.values()",
                "c": "dictionary[values]",
                "d": "dictionary.results()"
            },
            "correct": "b",
            "hint": "Think about the method that retrieves only the stored values.",
            "explanation": "dictionary.values() returns a view of all values in the dictionary."
        },
        {
            "qnum": 3,
            "type": "mcq",
            "text": "If we have a dictionary called myDict with a key of 'banana', how can we see the value attached to this key?",
            "options": {
                "a": "myDict[banana]",
                "b": "myDict.find('banana')",
                "c": "myDict['banana']",
                "d": "myDict.banana()"
            },
            "correct": "c",
            "hint": "Remember: dictionary keys must be accessed using square brackets and string quotes.",
            "explanation": "myDict['banana'] retrieves the value stored at the key 'banana'."
        }
    ],

    23: [
        {
            "qnum": 1,
            "type": "mcq",
            "text": "How can we define a function with one default parameter?",
            "options": {
                "a": "def function(param):",
                "b": "def function():",
                "c": "define function(param=0):",
                "d": "def function(param=0):"
            },
            "correct": "d",
            "hint": "Default parameters are set using '=' inside the parentheses.",
            "explanation": "A default parameter must be written inside the function parentheses like def function(param=0)."
        },
        {
            "qnum": 2,
            "type": "mcq",
            "text": "What is true about the return statement of a function?",
            "options": {
                "a": "It can pull information from outside the function into the function",
                "b": "It can pass information from inside the function out of the function",
                "c": "It makes the function start over (e.g. return to the beginning)",
                "d": "It makes the entire program start over"
            },
            "correct": "b",
            "hint": "Think about what value gets sent back when a function finishes.",
            "explanation": "return sends a value from inside the function back to the part of the program that called it."
        },
        {
            "qnum": 3,
            "type": "mcq",
            "text": "What is the correct way to call a function?",
            "options": {
                "a": "The keyword 'call' followed by the function name",
                "b": "The function name followed by parentheses",
                "c": "The keyword 'perform' followed by parentheses",
                "d": "The function name only"
            },
            "correct": "b",
            "hint": "Think about how you execute a function in Python.",
            "explanation": "Functions are called by writing their name followed by parentheses, such as myFunction()."
        }
    ],

    24: [
        {
            "qnum": 1,
            "type": "mcq",
            "text": "Which of these is NOT a file opening mode?",
            "options": {
                "a": "Read",
                "b": "Write",
                "c": "Append",
                "d": "Edit"
            },
            "correct": "d",
            "hint": "Think about the built-in modes: 'r', 'w', 'a'.",
            "explanation": "There is no 'edit' mode in Python’s file handling. Valid modes include read (r), write (w), append (a)."
        },

        {
            "qnum": 2,
            "type": "mcq",
            "text": "Which of the following commands reads an entire file into one string variable?",
            "options": {
                "a": "readlines()",
                "b": "read()",
                "c": "readline()",
                "d": "open()"
            },
            "correct": "b",
            "hint": "Think about which method loads *all* file text at once.",
            "explanation": "read() returns the entire contents of the file as a single string."
        },

        {
            "qnum": 3,
            "type": "mcq",
            "text": "Which block of a try/except structure executes if there is no error?",
            "options": {
                "a": "try",
                "b": "except",
                "c": "else",
                "d": "finally"
            },
            "correct": "c",
            "hint": "This block exists specifically for the 'no error' scenario.",
            "explanation": "The else block runs only when the try block does NOT raise an exception."
        }
    ],

    25: [
        {
            "qnum": 1,
            "type": "mcq",
            "text": "Which of these is NOT a valid reason to use OOP?",
            "options": {
                "a": "It will be faster to program",
                "b": "It helps keep code more organized",
                "c": "It can help prevent repetition",
                "d": "It allows us to create similar structures without recoding them"
            },
            "correct": "a",
            "hint": "Think about what OOP actually helps with — structure and reuse, not speed.",
            "explanation": "OOP helps organization, reuse, and reducing repetition. It does not guarantee faster programming."
        },

        {
            "qnum": 2,
            "type": "mcq",
            "text": "What is the function that we write to allow the creation of a new object?",
            "options": {
                "a": "__def__()",
                "b": "__init__()",
                "c": "create()",
                "d": "new()"
            },
            "correct": "b",
            "hint": "It's the constructor method — it runs when the object is created.",
            "explanation": "__init__() is the constructor method that initializes new objects in Python."
        },

        {
            "qnum": 3,
            "type": "mcq",
            "text": "What is the keyword to create a new type of object?",
            "options": {
                "a": "type",
                "b": "object",
                "c": "class",
                "d": "def"
            },
            "correct": "c",
            "hint": "We use this keyword to define new objects with their own attributes and methods.",
            "explanation": "The keyword 'class' is used to define a new object type in Python."
        }
    ],

    26: [
        {
            "qnum": 1,
            "type": "mcq",
            "text": "What are the two parts of a typical recursive function?",
            "options": {
                "a": "The start case and the stop case",
                "b": "The base case and the tower case",
                "c": "The base case and the recursive case",
                "d": "The start case and the recursive case"
            },
            "correct": "c",
            "hint": "Every recursive function needs a simple stopping condition and a step that repeats.",
            "explanation": "A recursive function always has a base case (stopping point) and a recursive case (where the function calls itself)."
        },

        {
            "qnum": 2,
            "type": "mcq",
            "text": "What issue can occur if the base case of a recursive function is never met?",
            "options": {
                "a": "An infinite loop",
                "b": "A maximum depth reach error",
                "c": "There will be an error shown before running the code",
                "d": "A recursion error"
            },
            "correct": "d",
            "hint": "Python stops runaway recursion after a certain depth.",
            "explanation": "If recursion never hits the base case, Python raises a RecursionError after exceeding the maximum recursion depth."
        },

        {
            "qnum": 3,
            "type": "mcq",
            "text": "What is true about the recursive call inside a recursive function?",
            "options": {
                "a": "It should be with a smaller part of the problem",
                "b": "It should be with a larger part of the problem",
                "c": "It must decrease the runtime of the problem",
                "d": "It cannot include more than one parameter"
            },
            "correct": "a",
            "hint": "Recursive calls must move toward the base case.",
            "explanation": "Each recursive call should work on a smaller or simpler version of the original problem, eventually reaching the base case."
        }
    ]
}
