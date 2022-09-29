import time
import os

def quiz_game():
    questions = ["What is the capital of France?", "How many legs does a spider have?", "What is the current US president?", "What is the capital of the US?", "What was Meta Platforms Inc formerly known as?"]
    possible_answers = [["Beijing", "Paris", "London", "New York"], ["2", "4", "6", "8"], ["Joe Biden", "Donald Trump", "Mr Faulkner", "Dr. Sins"], ["Washington DC", "Dubai", "Istanbul", "Hong Kong"], ["Facebook", "Google", "Amazon", "Twitter"]]
    correct_answers = ["Paris", "8", "Joe Biden", "Washington DC", "Facebook"]
    
    score = 0
    for i in range(len(questions)):
        os.system('cls' if os.name == 'nt' else 'clear')
        print(questions[i])
        print("Possible answers:\n")
        for possible_answer in possible_answers[i]:
            print(possible_answer)
        user_answer = input("\nEnter the answer: ")
        if user_answer == correct_answers[i]:
            print("Correct!")
            time.sleep(0.75)
            score += 1
        else:
            print("Incorrect")
            continue
    return score

final_score = quiz_game()
print("Score: " + str(final_score))
