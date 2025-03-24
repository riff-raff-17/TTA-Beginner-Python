from IPython.display import display, Image

def run_quiz(questions):
    print("Chapter 4 - Basic Operators (Math and Comparison)\n")
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
        "question": "What are the common data types used in math?",
        "image": None,  # Change this to your actual image file path or set to None if not needed, like "tests/testpictures/example.png"
        "options": ["str and bool", "list and dict","int and float", "set and tuple"],
        "answer": 3, # The correct option number (1-based index)
        "explanation": ""
    },
    {
        "question": "Which of the following is NOT a math operator in Python?",
        "image": None, 
        "options": ["+", "%%", "//", "**"],
        "answer": 2, 
        "explanation": '"+" is addition, "//" is floor division, "**" is exponentiation(to the power of). "%%" is not valid, but "%" is modulo.'
    },
    {
        "question": "What will this code print?",
        "image": "tests/testpictures/c4q3.png", 
        "options": ["11", "8 + 3", "83", '"11"'],
        "answer": 1, 
        "explanation": "This expression adds the two numbers -> 8 + 3 = 11 and results in an integer, having no quotes unlike a string."
    },
    {
        "question": "What data type is the result of this expression: 4 + 2.0 ?",
        "image": None, 
        "options": ["str", "int","float", "bool"],
        "answer": 3, 
        "explanation": "The result will be 6.0 as 2.0 was written as a float, therefore it is still a float."
    },
    {
        "question": "What will this program print?",
        "image": "tests/testpictures/c4q5.png", 
        "options": ["3", "3.0", "4", "4.0"],
        "answer": 2, 
        "explanation": "/ will always return a float -> 6 / 2 = 3.0"
    },
    {
        "question": "What is the output of this code?",
        "image": "tests/testpictures/c4q6.png", 
        "options": ["1", "3", "7", "3.33"],
        "answer": 1, 
        "explanation": "% is the modulo operator. 10 divided by 3 leaves a remainder of 1 -> 10 % 3 = 1"
    },
    {
        "question": "What is the output of this code?",
        "image": "tests/testpictures/c4q7.png", 
        "options": ["20", "14", "24", "12"],
        "answer": 2, 
        "explanation": "Multiplication happens first -> 3 * 4 = 12, then 2 + 12 = 14"
    },
    {
        "question": "What is the result of this code?",
        "image": "tests/testpictures/c4q8.png", 
        "options": ["10", "7",
                    "52", "25"],
        "answer": 4, 
        "explanation": "5 ** 2 is 5 squared -> 5 * 5 = 25"
    },
    {
        "question": "What will this program print?",
        "image": "tests/testpictures/c4q9.png", 
        "options": ["4", "4.0","4.5", '5'],
        "answer": 1, 
        "explanation": "// is floor division, so it will give the quotient as an integer -> 9 // 2 = 4. "
    },
    {
        "question": "What will this program print?",
        "image": "tests/testpictures/c4q10.png", 
        "options": ['2', "5 > 3",
                    "True", 'Syntax Error'],
        "answer": 3, 
        "explanation": '5 is greater than 3 -> result is True.'
    }
]

run_quiz(questions)