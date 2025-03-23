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
        "question": "What is a list in Python?",
        "image": None,  # Change this to your actual image file path or set to None if not needed, like tests/testpictures/example.jpg
        "options": ["A type of fruit", "A way to store multiple values in one variable",
                    "A type of loop", "A function that prints text"],
        "answer": 2, # The correct option number (1-based index)
        "explanation": "A list is a way to store multiple values in one variable."
    },
    {
        "question": "Which of the following correctly creates a list in Python?",
        "image": None,  
        "options": ["list = (1, 2, 3, 4)", "list = [1, 2, 3, 4]", "list = {1, 2, 3, 4}", "list = <1, 2, 3, 4>"],
        "answer": 2,
        "explanation": "Lists use square brackets [ ] to store values."
    },
    {
        "question": 'What will my_list[2] return if my_list = ["apple", "banana", "cherry", "date"]?',
        "image": None,  
        "options": ['"apple"', '"banana"', '"cherry"', '"date"'],
        "answer": 3,
        "explanation": "Lists start counting from 0, so 'cherry' is at index 2."
    },
    {
        "question": "How do you add a new item to a list?",
        "image": None,  
        "options": ['list.add("grape")', 'list.append("grape")', 'list.insert("grape")', 'list.update("grape")'],
        "answer": 2,
        "explanation": ".append() adds an item to the end of a list."
    },
    {
        "question": "What will happen if you try to access an index that is too big, like my_list[10] when the list only has 5 items?",
        "image": None,  
        "options": ["It will return None", "It will return the last item in the list", 
                    "It will add a new item to the list", "It will give an IndexError"],
        "answer": 4,
        "explanation": "If you try to access an index that doesn't exist, Python gives an IndexError."
    },
    {
        "question": "What is the output of the code below?",
        "image": "tests/testpictures/c8q6.png",  
        "options": ["2", "3", 
                    "4", "[2, 4, 6, 8]"],
        "answer": 3,
        "explanation": "len() returns the number of items in the list."
    },
    {
        "question": "What is the output of the code below?",
        "image": "tests/testpictures/c8q7.jpg",  
        "options": ["[10, 99, 30, 40]", "[99, 20, 30, 40]", 
                    "[10, 20, 30, 40, 99]", "99"],
        "answer": 1,
        "explanation": "Lists allow you to change an element using its index. numbers[1] replaces 20 with 99."
    },
    {
        "question": "What does list.pop() do by default?",
        "image": None,  
        "options": ["Adds an item to the end", "Removes the first item", 
                    "Removes the last item", "Deletes the entire list"],
        "answer": 3,
        "explanation": "pop() removes the last item in a list."
    },
    {
        "question": "What will this program print?",
        "image": "tests/testpictures/c8q9.png",  
        "options": ['["hamster", "cat", "dog", "rabbit"]', '["cat", "hamster", "dog", "rabbit"]',
                    '["cat", "dog", "hamster", "rabbit"]', '["cat", "dog", "rabbit", "hamster"]'],
        "answer": 2,
        "explanation": "insert(index, value) adds the value at that index, shifting others over"
    },
    {
        "question": "What does a negative index like -1 refer to in a list? e.g. list[-1]",
        "image": None,  
        "options": ['The first item', 'The second item',
                    'The last item', 'The last second item'],
        "answer": 3,
        "explanation": "Negative indexes from -1 start from the last item in a list."
    },
    {
        "question": "What happens when you loop through a list using a 'for' loop?",
        "image": None,  
        "options": ['Each item is removed one by one', 'Each item is printed twice',
                    'Each item is accessed one by one', 'A new list is created using the previous list'],
        "answer": 3,
        "explanation": "Looping a list accesses each item based on iteration, starting from index [0]."
    },
    {
        "question": "What does this code do?",
        "image": "tests/testpictures/c8q12.png",  
        "options": ['Prints only the first colour', 'Prints all the colours one time each',
                    'Prints the colours as a list', "NameError: 'color' is not defined"],
        "answer": 2,
        "explanation": "'color' is a local variable that can print the list items based on its iteration. The 'for' loop accesses each item one."
    },
    {
        "question": "What is the result of this comparison?",
        "image": "tests/testpictures/c8q13.png",  
        "options": ['True', 'False',
                    'None', "SyntaxError: Invalid syntax"],
        "answer": 1,
        "explanation": "Lists with the same content are considered equal with =="
    },
    {
        "question": "What is slicing in lists used for?",
        "image": None,  
        "options": ['Removing items from a list', 'Splitting strings into words',
                    'Getting a part of a list', 'Creating a new variable'],
        "answer": 3,
        "explanation": "Slicing is used to obtain specific parts of lists."
    },
    {
        "question": "What is the output below?",
        "image": "tests/testpictures/c8q15.png",  
        "options": ["['apple', 'banana', 'cherry']", "['apple', 'banana', 'cherry', 'durian']" ,
                    "['banana', 'cherry', 'durian']","['banana', 'cherry', 'durian', 'eggplant']" ],
        "answer": 3,
        "explanation": "list[1:4] is from index [1] ('banana') to index [3] ('durian'). Listing stops before 4."
    }
]

run_quiz(questions)