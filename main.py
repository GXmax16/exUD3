from jugador import Player
from game import Game
p1 = Player(1, 'a')
p2 = Player(2, 'b')
g1 = Game(p1, p2, 3)
print(f'p1: {p1.toString()}')
print(f'p2: {p2.toString()}')
g1.play()
winner = g1.winner()
print(f'El ganador mediante g1.winner().toString() es: {winner.toString()}')
