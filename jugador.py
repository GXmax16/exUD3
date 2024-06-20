MAX_ENERGY = 100
MIN_ENERGY = 0

class Player:
    def __init__(self, idPlayer, nickName):
        self.__idPlayer = idPlayer
        self.__nickName = nickName
        self.__energy = (MAX_ENERGY - MIN_ENERGY) // 2

    def get_idPlayer(self):
        return self.__idPlayer

    def set_idPlayer(self, idPlayer):
        self.__idPlayer = idPlayer

    def get_nickName(self):
        return self.__nickName

    def set_nickName(self, nickName):
        self.__nickName = nickName

    def get_energy(self):
        return self.__energy

    def setEnergy(self, energy):
        if MIN_ENERGY <= energy <= MAX_ENERGY:
            self.__energy = energy

    def toString(self):
        return f'[{self.__idPlayer}, {self.__nickName}, {self.__energy}]'

    def boost(self, charge):
        if type(charge) == int:
            new_energy = self.__energy + charge
            if charge < 0:
                new_energy = max(MIN_ENERGY, new_energy)
            else:
                new_energy = min(MAX_ENERGY, new_energy)
            self.__energy = new_energy
        return charge, self.__energy
