import re
import json

# Read data from questions.txt
with open('raw_questions_data.txt', 'r') as file:
    questions_data = file.read()

# Define a function to parse each question
def parse_question(question_text):
    database = []

    # Extract questions
    questions = re.findall(r"Question ID: (\d+)([\s\S]*?)(sec.*?)*Answer \((.)\)", question_text, re.DOTALL)
    solutions = re.findall(r"ID: (\d+)[\s\S]*?Sol([\s\S]*?)Ques", question_text, re.DOTALL)

    for _ in range(len(questions)):
        question = {}
        options = []

        question_id = questions[_][0]
        question_text = questions[_][1].lstrip('}\n')
        correct_answer = questions[_][3]
        opt = re.findall(r'\((.)\) (.*)', question_text)


        for k in range(len(opt)):
            if (opt[k][0] == correct_answer):
                correctness = True
            else:
                correctness = False
            option_data = {
                'optionNumber': k+1,
                'optionText': opt[k][1],
                'isCorrect': correctness
            }
            options.append(option_data)
        
        question['questionNumber'] = _+1
        question['questionId'] = question_id
        question_text = re.sub(r'(\(.\).*\n)', '', question_text)
        question_text = question_text.rstrip('\n\\')
        question['questionText'] = question_text
        question['options'] = options
        question['solutionText'] = ''

        for _ in range(len(solutions)):
            if (solutions[_][0] == question_id):
                question['solutionText'] = solutions[_][1].rstrip('\n{section*\\')
                break

        database.append(question)
        
    return database


# Parse each question and store in a list
parsed_questions = parse_question(questions_data)

# Convert parsed questions to JSON format
json_data = json.dumps(parsed_questions, indent=2)

# Write JSON data to file
with open('json_formatted_questions.json', 'w') as file:
    file.write(json_data)
