from IPython.display import display, Image

def run_quiz(questions):
    score = 0
    for i, q in enumerate(questions, 1):
        print(f"Q{i}: {q['question']}")

        # Display image if provided
        try:
            if "image" in q:
                display(Image(q["image"]))
        except:
            pass
        for j, option in enumerate(q['options'], 1):
            print(f"  {j}. {option}")
        
        while True:
            try:
                answer = int(input("Enter the number of your answer: "))
                if 1 <= answer <= 4:
                    break
                else:
                    print("Invalid choice!")
            except ValueError:
                print("Invalid choice!")

        
        if int(answer) == q['answer']:
            print("Correct!\n")
            score += 1
        else:
            correct_option = q['answer']
            correct_answer = q['options'][correct_option - 1]
            print(f"Wrong! The correct answer was {correct_option}: {correct_answer}.\n")
            
        if 'explanation' in q:
            print(f"Explanation: {q['explanation']}\n")
            
    print(f"You got {score}/{len(questions)} correct!")

# Example questions (replace with your own)
questions = [
    {
        "question": "What application is currently being used to code and compile Python?",
        "image": None,  # Change this to your actual image file path or set to None if not needed
        "options": ["Anaconda Navigator", "IDLE", "Jupyter Notebook", "Visual Studio"],
        "answer": 3, # The correct option number (1-based index)
        "explanation": "Jupyter Notebook is now being used to create programs with the Python Language."
    },
    {
        "question": "What is the name of the extension given when creating a notebook?",
        "image": None,  
        "options": [".py", ".notebook", ".ipynb", ".txt"],
        "answer": 3,
        "explanation": ".ipynb is the file extension of the created notebook."
    },
    {
        "question": "Which of the functions below correctly prints 'Hello, World!'?",
        "image": None,  
        "options": ['print"Hello, World!"', 'print("Hello, World!")', 'Print Hello, World!', 'print(Hello, World!)'],
        "answer": 2,
        "explanation": "You must type the function name correctly, followed by parentheses. To type a string, you must enclose the phrase with quotes."
    },
    {
        "question": "The rules regarding how code is written in Python and other languages is also known as...?",
        "image": None,  
        "options": ["Syntax", "Order of code", "Instructions", "A ruleset"],
        "answer": 1,
        "explanation": "Syntax is the set of rules defining how code must be written so that a computer can correctly interpret and execute instructions."
    },
    {
        "question": "What will this code print?",
        "image": "tests/testpictures/c1q5.png",  
        "options": ["Hello World", "Hello\n   World", "Hello\\nWorld", "Error"],
        "answer": 2,
        "explanation": "The \\n creates a new line, so 'World' appears on the next line."
    },
    {
        "question": "Which of the following will cause a syntax error?",
        "image": "tests/testpictures/c1q6.png",  
        "options": ["No error", "SyntaxError: Missing parentheses", "RuntimeError", "TypeError"],
        "answer": 2,
        "explanation": """In Python 3, print must be written as a function with parentheses: print("\\Hello, World!\\")."""
    },
    {
        "question": "What is the error in the following code?",
        "image": "tests/testpictures/c1q7.png",  
        "options": ["Missing print function", "No error", "print cannot handle strings", "String not closed properly"],
        "answer": 4,
        "explanation": """The string starts with a double quote (") but ends with a single quote ('). The correct version is: print("Python is fun!")."""
    },
    {
        "question": "What happens if you run this?",
        "image": "tests/testpictures/c1q8.png",  
        "options": ["Python is awesome!", "Python is \"awesome\"!", " SyntaxError", "\"Python is \"awesome\"!"],
        "answer": 3,
        "explanation": """The inner double quotes around "awesome" break the string. The correct way is: print('Python is "awesome"!')."""
    },
    {
        "question": "Which of the following prints a single backslash (\\)?",
        "image": None,  
        "options": ['print("\\")', 'print("\\\\")', 'print("/")', 'print("\\\\\\")'],
        "answer": 2,
        "explanation": 'The backslash (\\) is an escape character, so you must use "\\\\" to print a single backslash.'
    },
    {
        "question": "What is the error in the following code?",
        "image": "tests/testpictures/c1q10.png",  
        "options": ["No error", "Mismatched quotes", "print must use double quotes", "String too long"],
        "answer": 1,
        "explanation": "This string only has one double quote, but it is properly enclosed by single quotes, therefore this is still valid. (Try it out!)"
    },
]

run_quiz(questions)