from player import Player

# Game intro
player_name = input('Welcome to Who Wants To Be a Millionaire? terminal game! To start, please enter your name: ')
player = Player(player_name)
print(player)
input('Press Enter to start a game')