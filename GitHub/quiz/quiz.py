# Quiz Questions Data Structure

quiz_questions = [
    {
        "question": "What is the capital of France?",
        "options": ["Berlin", "Madrid", "Paris", "Rome"],
        "correct_answer": 3  # 3rd option (Paris) is correct
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["Earth", "Mars", "Jupiter", "Venus"],
        "correct_answer": 2  # 2nd option (Mars) is correct
    },
    {
        "question": "What is the chemical symbol for water?",
        "options": ["H2O", "CO2", "O2", "NaCl"],
        "correct_answer": 1  # 1st option (H2O) is correct
    }
]

# Print to verify the structure
print(quiz_questions)

# Loop through each question
for index, question_data in enumerate(quiz_questions, start=1):
    print(f"\nQuestion {index}: {question_data['question']}")  # Display question

    # Display answer choices
    for i, option in enumerate(question_data["options"], start=1):
        print(f"{i}. {option}")

    # Get user input
    user_answer = input("Enter the number of your answer: ")

    # Print what the user entered (for now, just to check)
    print(f"You chose option {user_answer}")


# Initialize score tracker
score = 0  # Keeps count of correct answers

# Loop through each question
for index, question_data in enumerate(quiz_questions, start=1):
    print(f"\nQuestion {index}: {question_data['question']}")  # Display question

    # Display answer choices
    for i, option in enumerate(question_data["options"], start=1):
        print(f"{i}. {option}")

    # Get user input
    user_answer = input("Enter the number of your answer: ")

    # Convert input to integer
    try:
        user_answer = int(user_answer)  # Convert to integer
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue  # Skip to the next question

    # Check if the answer is correct
    if user_answer == question_data["correct_answer"]:
        print("✅ Correct!")
        score += 1  # Increase score
    else:
        print(f"❌ Wrong! The correct answer was {question_data['correct_answer']}.")

# Print final score
print(f"\nQuiz complete! Your final score: {score} out of {len(quiz_questions)}")
# Initialize score tracker
score = 0  # Keeps count of correct answers

# Loop through each question
for index, question_data in enumerate(quiz_questions, start=1):
    print(f"\nQuestion {index}: {question_data['question']}")  # Display question

    # Display answer choices
    for i, option in enumerate(question_data["options"], start=1):
        print(f"{i}. {option}")

    # Get user input
    user_answer = input("Enter the number of your answer: ")

    # Convert input to integer
    try:
        user_answer = int(user_answer)  # Convert to integer
    except ValueError:
        print("Invalid input! Please enter a number.")
        continue  # Skip to the next question

    # Check if the answer is correct
    if user_answer == question_data["correct_answer"]:
        print("✅ Correct!")
        score += 1  # Increase score
    else:
        print(f"❌ Wrong! The correct answer was {question_data['correct_answer']}.")

# Print final score
print(f"\nQuiz complete! Your final score: {score} out of {len(quiz_questions)}")
