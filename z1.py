questions = {
    "1. What is the capital of France?": {"A": "London", "B": "Rome", "C": "Paris"},
    "2. Who wrote the play 'Romeo and Juliet'?": {"A": "Christopher Marlowe", "B": "William Shakespeare", "C": "Jane Austen"},
    "3. What is the chemical symbol for water?": {"A": "H2O", "B": "CO2", "C": "NaCl"},
    "4. Who painted the Mona Lisa?": {"A": "Vincent van Gogh", "B": "Leonardo da Vinci", "C": "Pablo Picasso"},
    "5. What is the largest planet in our solar system?": {"A": "Venus", "B": "Mars", "C": "Jupiter"},
    "6. Which country is famous for its pyramids?": {"A": "Greece", "B": "Egypt", "C": "China"},
    "7. What is the tallest mammal in the world?": {"A": "Elephant", "B": "Giraffe", "C": "Hippo"},
    "8. Who is known as the father of modern physics?": {"A": "Albert Einstein", "B": "Isaac Newton", "C": "Galileo Galilei"},
    "9. What is the capital of Japan?": {"A": "Beijing", "B": "Seoul", "C": "Tokyo"},
    "10. What is the fastest land animal?": {"A": "Cheetah", "B": "Lion", "C": "Leopard"}
}

answers = {
    "1": "C",
    "2": "B",
    "3": "A",
    "4": "B",
    "5": "C",
    "6": "B",
    "7": "B",
    "8": "B",
    "9": "C",
    "10": "A"
}

score = 0

print("Hello! Finish this quiz to win a $10 gift card \n")

for question, options in questions.items():
    print(question)
    for option, text in options.items():
        print(option + ") " + text)
    answer = input("Your answer: ").upper()
    correct_answer = answers.get(question[0])
    
    if answer == correct_answer:
        print("Correct \n")
        score += 1
    else:
        print("Wrong. The correct answer is:", correct_answer + "\n")

print("Your score is", score)

if score == 10:
    print("Congrats! You won a $10 gift card")
else:
    print("Better luck next time!")





    x = 'ken'
    y = 'barbie'