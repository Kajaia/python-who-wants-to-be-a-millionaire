# Should give us a random question with answers and its number
import random

class Question:
    asked_questions = []
    asked_questions_count = 0
    can_play = True
    rewards = [100, 200, 300, 500, 1000, 2000, 4000, 8000, 16000, 32000, 64000, 125000, 250000, 500000, 1000000]
    questions = [
        {'question': 'Who is known for his contributions to the field of computer science and is often referred to as the "father of modern computer science"?', 'answers': {'a': 'Bill Gates', 'b': 'Alan Turing', 'c': 'Steve Jobs', 'd': 'Mark Zuckerberg'}, 'correct': 'b'},
        {'question': 'Which programming language is often used for web development?', 'answers': {'a': 'Java', 'b': 'Python', 'c': 'HTML', 'd': 'Swift'}, 'correct': 'c'},
        {'question': 'What does PHP stand for?', 'answers': {'a': 'Personal Home Page', 'b': 'Hypertext Markup Language', 'c': 'Python Hypertext Processor', 'd': 'Programming Hyper Processor'}, 'correct': 'a'},
        {'question': 'Which JavaScript framework is often used for building user interfaces?', 'answers': {'a': 'Angular', 'b': 'Django', 'c': 'Flask', 'd': 'Express'}, 'correct': 'a'},
        {'question': 'What does the "DOM" stand for in web development?', 'answers': {'a': 'Document Object Model', 'b': 'Data Object Model', 'c': 'Dynamic Object Mechanism', 'd': 'Document Oriented Middleware'}, 'correct': 'a'},
        {'question': 'Which Python framework is commonly used for web development?', 'answers': {'a': 'Django', 'b': 'Flask', 'c': 'Ruby on Rails', 'd': 'Express.js'}, 'correct': 'a'},
        {'question': 'What is the purpose of the "elif" keyword in Python?', 'answers': {'a': 'Loop iteration', 'b': 'Exception handling', 'c': 'Conditional branching', 'd': 'Function definition'}, 'correct': 'c'},
        {'question': 'Which of the following is a Python data type for storing a sequence of elements?', 'answers': {'a': 'Dictionary', 'b': 'List', 'c': 'Tuple', 'd': 'Set'}, 'correct': 'b'},
        {'question': 'What is the purpose of "git" in software development?', 'answers': {'a': 'Database management', 'b': 'Version control', 'c': 'Package management', 'd': 'Testing automation'}, 'correct': 'b'},
        {'question': 'Which method is used to get the length of a list in Python?', 'answers': {'a': 'size()', 'b': 'length()', 'c': 'count()', 'd': 'len()'}, 'correct': 'd'},
        {'question': 'In Python, what does the "+= 1" operation do?', 'answers': {'a': 'Subtract 1', 'b': 'Add 1', 'c': 'Multiply by 1', 'd': 'Assign value 1'}, 'correct': 'b'},
        {'question': 'Which of the following is a benefit of using virtual environments in Python development?', 'answers': {'a': 'Faster code execution', 'b': 'Easier dependency management', 'c': 'Higher security', 'd': 'Improved syntax'}, 'correct': 'b'},
        {'question': 'What does the acronym "API" stand for?', 'answers': {'a': 'Application Programming Interface', 'b': 'Automated Program Integration', 'c': 'Advanced Programming Interface', 'd': 'Application Program Interface'}, 'correct': 'a'},
        {'question': 'Which Python library is commonly used for data visualization?', 'answers': {'a': 'Matplotlib', 'b': 'NumPy', 'c': 'Pandas', 'd': 'SciPy'}, 'correct': 'a'},
        {'question': 'What is the primary purpose of a constructor in object-oriented programming?', 'answers': {'a': 'Data manipulation', 'b': 'Code organization', 'c': 'Object instantiation', 'd': 'Memory optimization'}, 'correct': 'c'}
    ]

    def ask_random_question(self):
        questions = [question for question in self.questions if not question in self.asked_questions]
        random_question = random.choice(questions)
        self.asked_questions.append(random_question)
        Question.asked_questions_count += 1
        print(f'Question: {random_question["question"]}')
        print('Answers:')
        for letter, answer in random_question['answers'].items():
            print(letter.upper(), answer)

    def get_correct_answer(self, player_answer):
        latest_question = self.asked_questions[-1]
        correct_answer_letter = latest_question['correct']
        final_answer = self.get_final_answer(latest_question['answers'], correct_answer_letter)
        if player_answer.lower() == correct_answer_letter.lower():
            Question.can_play = True
            return f"Hurrayy! Your answer: {correct_answer_letter.upper()} {final_answer} is correct and you get ${self.rewards[self.asked_questions_count-1]}, congratulations!"
        Question.can_play = False
        return f"Oh noo, your answer is not correct, this is a correct answer: {correct_answer_letter.upper()} {final_answer}. Game Over! You won nothing :("
    
    def get_final_answer(self, question_answers, correct_answer_letter):
        final_answer = ""
        for letter, answer in question_answers.items():
            if letter == correct_answer_letter:
                final_answer += answer
        return final_answer