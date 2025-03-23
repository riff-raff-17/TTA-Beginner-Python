from IPython.display import display, Image

def run_quiz(questions):
    print("\nChapter 6: Loops (for and while loops)\n")
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
        "question": "What do loops do in Python?",
        "image": None,  # Change this to your actual image file path or set to None if not needed, like tests/testpictures/example.jpg
        "options": ["Runs a block of code only once", "Stops the program from running",
                    "Only works with numbers", "Repeats a block of code multiple times"],
        "answer": 4, # The correct option number (1-based index)
        "explanation": "Loops repeat a block of code depending on the condition written."
    },
    {
        "question": "What are the types of loops called?",
        "image": None,  
        "options": ["for loops", "while loops",
                    "for and while loops", "for, while and if-else loops"],
        "answer": 3, # The correct option number (1-based index)
        "explanation": "for and while loops can repeat a block of code. if-else statements do not loop."
    },
    {
        "question": 'What will this code output?',
        "image": "tests/testpictures/c6q3.png",  
        "options": ['1 2 3', '0 1 2', '0 1 2 3', '1 2'],
        "answer": 2,
        "explanation": 'i starts from 0 on the first iteration and ends before the number specified in range()'
    },
    {
        "question": 'What will be the output?',
        "image": "tests/testpictures/c6q4.jpg",  
        "options": ['Loop 1 Loop 3', 'Loop 1 Loop 2 Loop 3 Loop 4',
                    'Loop 1 Loop 2 Loop 3 Loop 4 Loop 5', 'Loop 1 Loop 3 Loop 5'],
        "answer": 1,
        "explanation": 'x starts at 1, increases by 2, prints "Loop 1" and "Loop 3" before stopping.'
    },
    {
        "question": "Which statement immediately exits a loop?",
        "image": None,  
        "options": ['continue', 'return', 'pass', 'break'],
        "answer": 4,
        "explanation": "'break' exits a loop immediately, meaning that it will never execute the code in the loop anymore."
    },
    {
        "question": "What happens when the condition in a while loop is always True and there's no break statement?",
        "image": None,  
        "options": ["Loop runs once", "Loop runs forever", 
                    "Error occurs", "Loop will never run"],
        "answer": 2,
        "explanation": "Without a break, an always-true condition causes an infinite loop."
    },
    {
        "question": "Which statement is true about 'for' loops in Python?",
        "image": None,  
        "options": ["Runs until a condition becomes False", "Runs only once", 
                    "Executes a fixed number of times", "Uses do-while structure"],
        "answer": 3,
        "explanation": "A for loop runs a fixed number of times, determined by range()."
    },
    {
        "question": "What will be the last number printed by this loop?",
        "image": "tests/testpictures/c6q8.png",  
        "options": ["2", "5", "8", "10"],
        "answer": 3,
        "explanation": "range starts at 2, adds 3 each time. -> 2, 5, 8"
    },
    {
        "question": "Which loop is suitable when the number of iterations is not known in advance?",
        "image": None,  
        "options": ["'for' loop", "'while' loop", "Both loops are suitable", "Neither loop is suitable"],
        "answer": 2,
        "explanation": "'while' loops allow you to continously run a loop until a condition is met."
    },
    {
        "question": "How many numbers will be printed here?",
        "image": "tests/testpictures/c6q10.png",  
        "options": ["5", "6", "4", "10"],
        "answer": 1,
        "explanation": "0, 2, 4, 6, 8 will be printed."
    },
    {
        "question": "How many numbers will be printed here?",
        "image": "tests/testpictures/c6q11.png",  
        "options": ["1 2 3 4 5", "5 4 3 2 1", "5 4 3 2 1 0", "Error"],
        "answer": 2,
        "explanation": "'i' starts at 5, going backwards (step = -1), and stops before 0."
    },
    {
        "question": "What does range(7) mean in Python?",
        "image": None,  
        "options": ["Start at 1, stop at 7, step by 1", "Start at 0, stop at 7, step by 1",
                    "Start at 0, stop at 6, step by 1", "Start at 1, stop at 6, step by 1"],
        "answer": 2,
        "explanation": "If only one number is given, it's the stop. Start defaults to 0 and Step defaults to 1."
    },
    {
        "question": "Which line below has an error?",
        "image": "tests/testpictures/c6q13.png",  
        "options": ["Line 1", "Line 2", "Both lines", "No error"],
        "answer": 2,
        "explanation": "Step cannot be 0 — this causes a ValueError."
    },
    {
        "question": "What is the result of the code below?",
        "image": "tests/testpictures/c6q14.png",  
        "options": ["LoopError: break cannot be used without if-else statement", "No error, but nothing is printed",
                    "'Hi' is printed once", "'Hi' is printed infinitely"],
        "answer": 3,
        "explanation": 'The loop starts as infinite, and "print("Hi!")" prints it once. "break" exits the loop immediately after that.'
    },
    {
        "question": "What is the last number printed?",
        "image": "tests/testpictures/c6q15.png",  
        "options": ["0", "1", "5", "6"],
        "answer": 4,
        "explanation": "x on its final iteration is equal to 5, then gets added by 1 and is printed before the loop breaks."
    }
]

run_quiz(questions)