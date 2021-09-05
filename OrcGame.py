class Character:
    def __init__(self, name, strength, weapon):
        self._name = name
        self.setStrength(strength)
        self.setWeapon(weapon)

    def getName(self):
        return self._name

    def getStrength(self):
        return self._strength

    def setName(self, name):
        try:
            if type(name) == str:
                self._name = name
            else:
                raise TypeError
        except:
            return 'type ERROR'

    def setStrength(self, newStrength):
        try:
            newStrength = float(newStrength)
            if newStrength > 5.0:
                self._strength = 5.0
            elif newStrength < 0.0:
                self._strength = 0.0
            elif 0.0 <= newStrength <= 5.0:
                self._strength = newStrength
        except:
            return 'type ERROR'

    def getWeapon(self):
        return self._weapon

    def setWeapon(self, weapon):
        try:
            self._weapon = bool(weapon)
        except:
            return 'Weapon must be Boolean - True/False.'

    name = property(getName, setName)
    strength = property(getStrength, setStrength)
    weapon = property(getWeapon, setWeapon)

    def __gt__(self, other):
        if self.weapon and not other.weapon:
            greater = True
        elif other.weapon and not self.weapon:
            greater = False
        else:
            if self._strength > other.strength:
                greater = True
            elif self._strength < other.strength:
                greater = False
            else:
                greater = 'Neither player is greater.'
        return greater

    def fight(self, player):
        if self.__gt__(player) is True:
            winner = self
            self.strength += 1
        elif self.__gt__(player) is False:
            winner = player
            player.strength += 1
        else:
            winner = self.__gt__(player)
            self.strength -= 0.5
            player.strength -= 0.5
        return winner

class Orc(Character):
    def __init__(self, name, strength, weapon):
        super().__init__(name, strength, weapon)

    def getWeapon(self):
        return self._weapon

    def setWeapon(self, weapon):
        try:
            self._weapon = bool(weapon)
        except:
            return 'Weapon must be Boolean - True/False.'

    name = Character.name
    strength = Character.strength
    weapon = Character.weapon

    def __str__(self):
        return "%s %s %s" % (self._name, str(float(self._strength)), self._weapon)

    def fight(self, player):
        if isinstance(player, Orc):
            if self.__gt__(player) is True:
                self.strength += 1
                winner = self
            elif self.__gt__(player) is False:
                player.strength += 1
                winner = player
            else:
                self.strength -= 0.5
                player.strength -= 0.5
                winner = Character.__gt__(self, player)
        elif isinstance(player, Human):
            if not self.weapon:
                # Humans have weapons so they win by default
                player.strength += 1
                winner = player
            else:
                # Both have weapons so it goes to strength
                if self > player:
                    self.strength += 1
                    winner = self
                elif player > self:
                    player.strength += 1
                    winner = player
                else:
                    self.strength -= 0.5
                    player.strength -= 0.5
                    winner = Character.__gt__(self, player)
        return winner

    @staticmethod
    def test():
        dan = Orc('Dan', 3, True)
        jan = Orc('Jan', 2.4, False)
        stan = Orc('Stan', 3, True)
        print(dan)
        print(jan)
        print(stan)
        print('Let\'s increase Jan\'s strength to 3!')
        jan.setStrength(3)
        print(jan)
        print('Dan will now fight his brother Stan.')
        print(dan.fight(stan), 'x')
        print(dan)
        print(stan)
        print('While they fought and lost strength, Dan found a weapon.')
        jan.setWeapon(True)
        print(jan)
        print('Jan storms to victory.')
        print(jan.fight(dan))
        print(jan.fight(stan))
        print('Jan supremacy, one orc to rule them all!')

# Orc.test()

class Human(Character):
    def __init__(self, name, strength, kingdom):
        super().__init__(name, strength, True)
        self._kingdom = kingdom

    def getKingdom(self):
        return self._kingdom

    def setKingdom(self, newkingdom):
        self._kingdom = newkingdom

    name = Character.name
    strength = Character.strength
    kingdom = property(getKingdom, setKingdom)

    def __str__(self):
        return "%s %s %s" % (str(self._name), str(float(self._strength)), str(self._kingdom))


    def fight(self, player):
        if isinstance(player, Human):
            out = 'fight ERROR'
        elif isinstance(player, Orc):
            if self.getWeapon() == False and player.getWeapon() == True:
                player.strength = (player.strength + 1)
                out = player
            elif self.getWeapon() == True and player.getWeapon() == False:
                self.strength = (self._strength + 1)
                out = self
            else:
                out = Character.__gt__(self, player)
                if self.__gt__(player):
                    self.strength += 1
                elif player.__gt__(self):
                    player.strength += 1
                else:
                    self.strength -= 0.5
                    player.strength -= 0.5
        return out

    @staticmethod
    def test():
        karen = Human('Karen', 2, 'Cork')
        sharon = Human('Sharon', 2, 'Cork')
        print(karen)
        print(sharon)
        print(karen.fight(sharon))
        john = Human('John', 3.1, 'Waterford')
        print(john)
        linda = Orc('Linda', 2, True)
        print(linda)
        print(linda.fight(john))

# Human.test()

class Archer(Human):
    def __init__(self, name, strength, kingdom):
        Human.__init__(self, name, strength, kingdom)

    @staticmethod
    def test():
        shrek = Archer('Shrek', 5, 'Far Far Away')
        fiona = Archer('Fiona', 5, 'Far Far Away')
        print(shrek)
        print(fiona)
        print(shrek.fight(fiona))

# Archer.test()

class Knight(Human):
    def __init__(self, name, strength, kingdom, archer_list):
        Human.__init__(self, name, strength, kingdom)
        if archer_list is None:
            archer_list = []
        self._archers_list = archer_list

    def getArchersList(self):
        rightKingdom = [archer.__str__() for archer in self._archers_list if archer.kingdom == self.kingdom]
        return rightKingdom

    def setArchersList(self, archer):
        try:
            if isinstance(archer, Archer):
                self._archers_list += [archer]
            else:
                raise ValueError
        except:
            return 'archers list ERROR'

    name = Character.name
    strength = Character.strength
    kingdom = Human.kingdom
    archersList = property(getArchersList, setArchersList)

    def __str__(self):
        return "%s %s %s %s" % (
            str(self.name), str(float(self.strength)), str(self.kingdom), str(self.getArchersList()))

    @staticmethod
    def test():
        ben = Archer('Ben', 2, 'Gondor')
        gwen = Archer('Gwen', 2, 'Gondor')
        kurt = Archer('Kurt', 2, 'Mordor')
        mike = Orc('Mike', 1, True)
        annie = Knight('Annie', 2, 'Gondor', ['boop', 'snoot'])
        danny = Knight('Danny', 2, 'Gondor', [ben, gwen])
        print(danny.fight(annie))
        print(danny.fight(mike))
        danny.archersList = kurt
        print(danny.setArchersList(annie))
        print(danny.setArchersList(kurt))
        print(danny.archersList)
        print(danny.__str__(), 'before')
        print(danny.fight(annie))
        print(danny.fight(mike))
        print(danny.__str__(), 'after')
        print(annie > danny)
        print(danny.fight(annie))
        print(danny.__str__())
        print(ben)
        print(danny.getArchersList())
        danny.archers_list = kurt
        print(danny.__str__())

# Knight.test()
