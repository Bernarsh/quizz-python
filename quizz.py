# Define a list of questions
questions = [
    "What is the capital of France?",
    "What is the currency of Japan?",
    "What is the largest planet in our solar system?"
]

# Define a list of answers
answers = [
    "Paris",
    "Yen",
    "Jupiter"
]

# Define a variable to keep track of the score
score = 0

# Iterate over the questions and ask them to the user
for i in range(len(questions)):
    question = questions[i]
    answer = answers[i]
    
    # Prompt the user for their answer
    user_answer = input(question + " ")
    
    # Check if the answer is correct
    if user_answer.lower() == answer.lower():
        print("Correct!")
        score += 1
    else:
        print("Incorrect. The correct answer is:", answer)

# Print the final score
print("You scored", score, "out of", len(questions))

