from IPython.display import display, Image

def run_quiz(questions):
    print("Chapter 2 - Understanding Variables and Other Data Types\n")
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
        "question": "What is a variable in Python?",
        "image": None,  # Change this to your actual image file path or set to None if not needed, like "tests/testpictures/example.png"
        "options": ["A number that never changes", "A way to store and label data in a program",
                    "A built-in function that prints output", "A tool used to create errors"],
        "answer": 2, # The correct option number (1-based index)
        "explanation": "A variable can contain values like numbers, strings or other data. It can be reused or changed throughout the code."
    },
    {
        "question": "Which of the following is NOT a valid data type?",
        "image": None, 
        "options": ["Integer", "String", "Float", "Letter"],
        "answer": 4, 
        "explanation": '"Letter" is not a built-in data type in Python.'
    },
    {
        "question": "What will this code print?",
        "image": "tests/testpictures/c2q3.png", 
        "options": ["age", "'age'", "10", "'10'"],
        "answer": 3, 
        "explanation": "The variable 'age' was created and assigned with integer 10, and 'print(age)' prints the value assigned to it, which is 10."
    },
    {
        "question": "Which of the following is a valid variable name in Python?",
        "image": None, 
        "options": ["2ndPlace", "first-name", "my_variable", "class"],
        "answer": 3, 
        "explanation": "Variables cannot contain spaces and special characters including dashes, and must not start with a number. Underscores are allowed."
    },
    {
        "question": "How can you check the type of a variable in Python?",
        "image": None, 
        "options": ["typeOf(myVar)", "checkType(myVar)", "typeof(myVar)", "type(myVar)"],
        "answer": 4, 
        "explanation": "The valid way check the data type of a variable is using type() e.g. print(type(myVar))"
    },
    {
        "question": "Which variable type below is NOT being declared?",
        "image": "tests/testpictures/c2q6.png", 
        "options": ["int", "float", "str", "bool"],
        "answer": 2, 
        "explanation": "The 'float' data type is a number that contains decimals. None of the variables declared here are float."
    },
    {
        "question": "Which of the following is TRUE about variables in Python?",
        "image": None, 
        "options": ["You must declare a variable's type before using it", "Variable names can include spaces",
                    "Variables can change type after being assigned", "Variable names can start with a number"],
        "answer": 3, 
        "explanation": "Types of data assigned to variables can change by overwriting or converting its value(e.g. int to str, replacing float with bool)"
    },
    {
        "question": "What will the code below print?",
        "image": "tests/testpictures/c2q8.png", 
        "options": ["Leo is 10 years old.", "Leo is age years old.",
                    "Leo is + age years old.", '"Leo" is str(10) years old.'],
        "answer": 1, 
        "explanation": "str(age) is used to convert the integer to a string so it can be concatenated with other strings."
    },
    {
        "question": "What will the code below print?",
        "image": "tests/testpictures/c2q9.png", 
        "options": ["12", "13","my_age", 'An error occurs'],
        "answer": 1, 
        "explanation": "'your_age' gets a copy of the value 12. It doesn't change when 'my_age' changes."
    },
    {
        "question": "There is an error in this code. What is it?",
        "image": "tests/testpictures/c2q10.png", 
        "options": ['Should be "Hello + str(name)"', "print() should be Print()",
                    "John should have quotes", 'John is a reserved keyword'],
        "answer": 3, 
        "explanation": 'Printing a string requires the text to be enclosed by quotes (e.g. "John")'
    }
]

run_quiz(questions)