# Player should have a name
# We should save answered questions
# We should have money won
class Player:
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return (f'Hello, {self.name}!\nWelcome tou our game show!\nBefore we start a game, you need to understand our rules:\n1. We have 15 questions that you need to answer correctly to get your reward (money in this case);\n2. You can stop the game any time you want and get reward that you deserve, if you fail to answer any question, you get nothing;\n3. Question has 4 answers, where only one is correct;\n4. You can get help if you feel stuck: 50:50, Audience or Call once each.\nNow let\'s start our game. Good luck, {self.name}!')