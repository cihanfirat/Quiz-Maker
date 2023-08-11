import random
def load_questions_and_answers(file_name):
    qa = {}
    file = open(file_name, 'r')
    for line in file:
        line = line.strip('\n')
        components = line.split('|||')
        question = components[0]
        answer = components[1]
        qa[question] = answer
    return qa
        
def get_random_question(qa):
    keys = list(qa.keys())
    index = random.randint(0, len(keys) - 1)
    key = keys[index]
    return key

def ask_question(qa):
    question = get_random_question(qa)
    print(question)
    response = input('Enter response: ')
    if response == qa[question]:
        print('correct!')
        del qa[question]
        return True
    else:
        print('incorrect!')
        return False

def main():
    print("Welcome to the quiz! Please write your answers first letter as capital. Otherwise it accept as an incorrect answer.")
    print("Please Choose the text file name as 'quiz1.txt'")
    print("You can choose 7 questions at most. Good Luck!")
    file_name = input('What is the name of the QA file? ')
    number_of_questions = int(input('How many questions should be asked? '))
    questions_answers = load_questions_and_answers(file_name)
    correct_count = 0
    for i in range(number_of_questions):
        correct = ask_question(questions_answers)
        if correct:
            correct_count += 1
    print('You got', correct_count, 'out of', number_of_questions, 'correct.')
    print('Your percentage grade: ' + 
      str(correct_count / number_of_questions * 100) + '%')

main()