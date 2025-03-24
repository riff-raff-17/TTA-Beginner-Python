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
        "image": r"tests/testpictures/example.jpg",  # Change this to your actual image file path or set to None if not needed
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
        "question": "What is NOT a valid method of printing outputs on multiple lines?",
        "image": None,  
        "options": ["Using \\n in between statements ", "Use print() command on multiple lines", 
                    "Using triple quotes (''')", "Run multiple cells at the same time"],
        "answer": 4,
        "explanation": "Running multiple cells does not print on the same output cell."
    }
]

run_quiz(questions)