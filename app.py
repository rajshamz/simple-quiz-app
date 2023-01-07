import os

def run_quiz(questions):
    score = 0
    for question in questions:
        print(question[0])
        for i, option in enumerate(question[1]):
            print(f"{i+1}. {option}")
        user_answer = input("Enter your answer: ")
        if user_answer == question[2]:
            print("Correct!\n")
            score += 1
        else:
            print("Incorrect.\n")
    print(f"You scored {score} out of {len(questions)}")

def read_questions(file):
    questions = []
    with open(file, "r") as f:
        lines = f.readlines()
    for i, line in enumerate(lines):
        if line[0] == "Q":
            q = line[2:].strip()
            options = []
            for j in range(i+1, len(lines)):
                if lines[j][0] == "A":
                    answer = lines[j][2:].strip()
                    break
                options.append(lines[j].strip())
            questions.append((q, options, answer))
    return questions

if __name__ == "__main__":
    file = "questions.txt"
    if not os.path.exists(file):
        print("Error: question file not found")
        exit(1)
    questions = read_questions(file)
    run_quiz(questions)

