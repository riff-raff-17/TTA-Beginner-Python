from IPython.display import display, Image

def run_quiz(questions):
    print("\nChapter 3: Getting User Input\n")
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
        "question": "What does the input() function do in Python?",
        "image": None,  # Change this to your actual image file path or set to None if not needed
        "options": ["It prints text on the screen", "It takes user input and stores it as a string.", "It adds two numbers together.", "It creates a new variable automatically"],
        "answer": 2, # The correct option number (1-based index)
        "explanation": "The input() function asks the user for a value and always stores it as a string."
    },
    {
        "question": "What will this code output?",
        "image": "tests/testpictures/c3q2.png",
        "options": ["Hello", "Hello,", "Hello, <user's name>!", "Error"],
        "answer": 3,
        "explanation": "The input() function stores the user's input (in this case, their name) in the variable name, and print() displays it."
    },
    {
        "question": "What happens if this code is executed?",
        "image": "tests/testpictures/c3q3.png",
        "options": ["It will print the user's age correctly.", "It will raise an error because the input is not an integer.", "It will ask for the user's age but print nothing.", "It will print Your age is None."],
        "answer": 1,
        "explanation": "The input() function returns a string, so if the user enters a number, it will be treated as a string."
    },
    {
        "question": "Which of the following will correctly get a number from the user and store it in a variable?",
        "image": None,
        "options": ['num = input("Enter a number: ")', 'num = int(input("Enter a number: "))', 'num = float(input("Enter a number: "))', "All of the above"],
        "answer": 4,
        "explanation": "You can convert the input to an integer using int() or to a float using float(). Using input() directly stores it as a string."
    },
    {
        "question": "What does the following code do?",
        "image": "tests/testpictures/c3q5.png",
        "options": ["Asks the user for their age and raises an error.", "Asks the user for their age and adds 1 to it.", "Asks the user for their age and multiplies it by 2.", "Asks the user for their age and prints it."],
        "answer": 4,
        "explanation": "The input() function stores the user's input as a string, and print() displays the value stored in the age variable."
    },
    {
        "question": "What will be the output if the user enters Peter and 12?",
        "image": "tests/testpictures/c3q6.png",
        "options": ["Peter is 12 years old.", "Peter is age years old.", "Error", "Peter is12 years old."],
        "answer": 1,
        "explanation": ('''input() returns strings, and + joins them, so print(name + " is " + age + " years old.") correctly prints "Peter is 12 years old."
        with spaces included inside the quotes.''')
    },
    {
        "question": "The code below prints out user's birth year after their age has been input. What should be typed in the blank?",
        "image": "tests/testpictures/c3q7.png",
        "options": ['str', 'bool', 'int', 'float'],
        "answer": 3,
        "explanation": "Using 'int(input)' allows the birthyear to be calculated as an integer."
    },
    {
        "question": "What will happen if the user enters Friend?",
        "image": "tests/testpictures/c3q8.png",
        "options": ["Your best friend is Friend!", 'Your best friend is "Friend"!', "Friend", "Error"],
        "answer": 1,
        "explanation": 'The input "Friend" is concatenated with the string "Your best friend is " and "!" to form the output.'
    },
    {
        "question": "What will happen if the user enters 10 for the following code?",
        "image": "tests/testpictures/c3q9.png",
        "options": ["The number you entered is: 10", 'The number you entered is: "10"', "The number you entered is: 10.0", "Error"],
        "answer": 1,
        "explanation": 'The input() function takes "10" as a string, and the print() function concatenates it with the message.'
    },
    {
        "question": "What will the following code output if the user enters Banana and Yellow?",
        "image": "tests/testpictures/c3q10.png",
        "options": ["Banana is Yellow!", 'Banana is "Yellow"', "Error", "Banana is Yellow"],
        "answer": 4,
        "explanation": "The input() function stores the entered values as strings, and the print() function concatenates the values of fruit and color."
    },


]

run_quiz(questions)