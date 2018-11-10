import random


class Pokemon(object):
    def __init__(self, name, level, type_pokemon, hp, attack, defense, special_attack, special_defense, speed):
        self.name = str(name)
        self.level = level
        self.type_pokemon = type_pokemon
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.special_attack = special_attack
        self.special_defense = special_defense
        self.speed = speed

    def death(self):
        return (self.hp <= 0)

    def level_up(self):
        self.level += 1
        return "\n" + self.name + " получает уровень  " + str(self.level) + "!\n"

    def attaсk(self, enemy):
        dmg = random.randint(1, 5)
        critical_attack = random.randint(0, 1)
        print(self.name + " атакует ")
        if critical_attack == 1:
            dmg += 10
            print("Критический удар! " + enemy.name + " теряет " + str(dmg) + " здоровья.")
        enemy.hp -= dmg
        print(enemy.name + " потерял " + str(dmg) + " здоровья. Осталось " + str(enemy.hp) + " здоровья")

        if enemy.death():
            print("\n" + str(self.level_up()))


class Bulbasaur(Pokemon):
    def __init__(self, name='Бульбазавр',
                 level=1,
                 type_pokemon='Grass',
                 hp=45,
                 attack=49,
                 defense=49,
                 special_attack=65,
                 special_defense=65,
                 speed=45,

                 ):
        Pokemon.__init__(self, name, level, type_pokemon, hp, attack, defense, special_attack, special_defense, speed)


class Ivysaur(Bulbasaur):
    def __init__(self, name='Ивизавр',
                 level=16,
                 hp=60,
                 type_pokemon='Grass',
                 attack=62,
                 defense=63,
                 special_attack=80,
                 special_defense=80,
                 speed=60,
                 ):
        Pokemon.__init__(self, name, level, type_pokemon, hp, attack, defense, special_attack, special_defense, speed)


class Rattata(Pokemon):
    def __init__(self, name='Раттата',
                 level=1,
                 type_pokemon='Normal',
                 hp=30,
                 attack=56,
                 defense=35,
                 special_attack=25,
                 special_defense=35,
                 speed=72,
                 basic_attack='Tackle'):
        Pokemon.__init__(self, name, level, type_pokemon, hp, attack, defense, special_attack, special_defense, speed)
        self.basic_attack = basic_attack

    def attaсk(self, enemy):
        Pokemon.attaсk(self, enemy)
        if enemy.type_pokemon == 'Grass':  # ну допустим...
            enemy.hp -= 10  # ну допустим...
            print(self.name + ' использовал ' + self.basic_attack)
            print(enemy.name + " осталось" + str(enemy.hp) + " здоровья.")


def main():
    team1 = Rattata()
    team2 = Bulbasaur()
    print()
    while team1.hp > 0 and team2.hp > 0:
        if team1.hp > 0:
            print(team1.attaсk(team2))
            print()
        if team2.hp > 0:
            print(team2.attaсk(team1))
            print()
    if team1.death():
        print(team2.name + " победил!")
        print(team1.name + " теряет сознание ")
    else:
        print(team1.name + " победил!")
        print(team2.name + " теряет сознание")

main()
