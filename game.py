import random

class Game:
    def __init__(self, player1, player2, rounds):
        self.__player1 = player1
        self.__player2 = player2
        self.__rounds = rounds

    def playRound(self):
        random_number1 = random.randint(-25, 25)
        random_number2 = random.randint(-25, 25)

        result1 = self.__player1.boost(random_number1)
        result2 = self.__player2.boost(random_number2)

        return [result1, result2]

    def winner(self):
        if self.__player1.get_energy() > self.__player2.get_energy():
            return self.__player1
        elif self.__player1.get_energy() < self.__player2.get_energy():
            return self.__player2
        else:
            return None

    def play(self):
        for i in range(1, self.__rounds + 1):
            round_result = self.playRound()
            print(f'Round {i}: {round_result}')

