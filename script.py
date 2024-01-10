from player import Player
from question import Question

# Game intro
player_name = input('Welcome to Who Wants To Be a Millionaire? terminal game! To start, please enter your name: ')
player = Player(player_name)
print(player)
input('Press Enter to start a game')

# Ask questions
question = Question()
while question.can_play and question.asked_questions_count < 15:
    question.ask_random_question()
    player_answer = input('Think about your answer and type a letter: ')
    print(question.get_correct_answer(player_answer))
    if question.can_play and question.asked_questions_count == 15:
        print(f'{player.name}, you are a Millionaire! 🤑💵💵🫰 Congratulations!')
        break
    if question.can_play:
        player_input = input('Press Enter to continue game or type "Get reward" to finish and get your reward ')
        if player_input == 'Get reward':
            print(f'You stopped the game and got reward: ${question.rewards[question.asked_questions_count-1]}, congratulations!')
            break