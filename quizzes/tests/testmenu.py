from IPython.display import clear_output
import time

exit = 0

def menu_display(mode):
    clear_output(wait=True)
    if mode == "0":
        print('''Select test:
        1. "Hello, World!" and other greetings
        2. Variables and Other Data Types
        3. Getting User Input
        4. Basic Operators (Math and Comparison)
        5. Conditional Statements (if, elif, else)
        6. Loops (for and while loops)
        7. Functions (def and return)
        8. Lists and Basic List Operations
        9. Dictionaries and Key-Value Pairs
        10. Logical Operators (and, or not)
        11. Importing Modules (math, random, etc.)
        12. Basic Error Handling
        Q. Formative/Summative Quizzes
        ''')
    if mode == "q":
        print('''Select test:
        1. Formative Assessment 1 (Chapter 1-3)
        2. Formative Assessment 2 (Chapter 4-6)
        3. Summative Assessment 1 (Chapter 1-6)
        4. Formative Assessment 3 (Chapter 7-9)
        5. Formative Assessment 4 (Chapter 10-12)
        6. Summative Assessment 2 (Chapter 7-12)
        7. Master Quiz (Chapter 1-12)
        0. Previous page
        ''')
    time.sleep(1)
    return mode

menu_display("0")
mode = "0"


while exit == 0:
    
    
    test = input("Enter your choice: ").lower()  # Get user input
    if test == "q":
        menu_display(test)
        
    else:
        menu_display("0")
    
    if mode == "0":
        if test == "1":
            exec(open("tests/chapter1.py").read())  # Runs the corresponding Python file
            exit = 1
        elif test == "2":
            exec(open("tests/chapter2.py").read())
            exit = 1
        elif test == "3":
            exec(open("tests/chapter3.py").read())
            exit = 1
        elif test == "4":
            exec(open("tests/chapter4.py").read()) 
            exit = 1
        elif test == "5":
            exec(open("tests/chapter5.py").read())
            exit = 1
        elif test == "6":
            exec(open("tests/chapter6.py").read())  
            exit = 1
        elif test == "7":
            exec(open("tests/chapter7.py").read())
            exit = 1
        elif test == "8":
            exec(open("tests/chapter8.py").read())
            exit = 1
        
            
    elif mode == "q":
        if test == "1":
            exec(open("tests/formative1.py").read())
            exit = 1
        if test == "2":
            exec(open("tests/formative2.py").read())
            exit = 1
        if test == "3":
            exec(open("tests/summative1.py").read())
            exit = 1
        if test == "4":
            exec(open("tests/formative3.py").read())
            exit = 1
        if test == "5":
            exec(open("tests/formative4.py").read())
            exit = 1
        if test == "6":
            exec(open("tests/summative2.py").read())
            exit = 1
        
        
        