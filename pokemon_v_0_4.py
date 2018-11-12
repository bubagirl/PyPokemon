import random


class Pokemon(object):
    def __init__(self, name, level, poke_type, hp, atk, defense, special_attack, special_defense, speed):
        self.name = str(name)  # Название покемона
        self.level = level  # Уровень покемона
        self.poke_type = poke_type  # Тип покемона

        self.hp = hp  # Очки здоровья
        self.atk = atk  # Атака
        self.defense = defense  # Защита
        self.special_attack = special_attack  # Специальная атака атака
        self.special_defense = special_defense  # Специальная защита
        self.speed = speed   # Скорость

    def death(self):
        return (self.hp <= 0)

    def level_up(self):
        self.level += 1
        return "\n" + self.name + " получает уровень  " + str(self.level) + "!\n"

    def attack(self, enemy):
        dmg = int(self.atk/10)
        critical_attack = random.randint(0, 5)
        print(self.name + " атакует ")
        if critical_attack == 5:
            dmg = int(dmg + (self.special_attack/10))
            print("Критический удар! " + enemy.name + " теряет " + str(dmg) + " здоровья.")
        enemy.hp = int(enemy.hp + (enemy.defense/10) - dmg)
        print(enemy.name + " потерял " + str(dmg) + " здоровья. Осталось " + str(enemy.hp) + " здоровья")

        if enemy.poke_type == self.poke_type:
            dmg = int(dmg/2)
            print(enemy.name + " того же типа, что и " + self.name + " и получает меньше урона " + str(dmg))
        if enemy.death():
            print(str(self.level_up()))


bulbasaur_moves = ("Razor Leaf", "Headbutt", "Giga Drain")


class Bulbasaur(Pokemon):
    def __init__(self, name='Бульбазавр',
                 level=1,
                 poke_type="Grass" and "Poison",
                 hp=45,
                 atk=49,
                 defense=49,
                 special_attack=65,
                 special_defense=65,
                 speed=45,
                 ):
        Pokemon.__init__(self, name, level, poke_type, hp, atk, defense, special_attack, special_defense, speed)

    def attack(self, enemy):
        Pokemon.attack(self, enemy)
        if enemy.poke_type != "Poison" or "Grass":
            choice = random.choice(bulbasaur_moves)
            enemy.hp -= 4
            print(self.name + ' использовал ' + str(choice))
            print(enemy.name + " осталось" + str(enemy.hp) + " здоровья.")


class Ivysaur(Bulbasaur):
    def __init__(self, name='Ивизавр',
                 level=16,
                 poke_type="Grass" and "Poison",
                 hp=60,
                 atk=62,
                 defense=63,
                 special_attack=80,
                 special_defense=80,
                 speed=60,
                 ):
        Pokemon.__init__(self, name, level, poke_type, hp, atk, defense, special_attack, special_defense, speed)


rattata_moves = ("Super Fang", "Headbutt", "Shadow Ball")


class Rattata(Pokemon):
    def __init__(self, name='Раттата',
                 level=1,
                 poke_type='Normal',
                 hp=30,
                 atk=56,
                 defense=35,
                 special_attack=25,
                 special_defense=35,
                 speed=72,
                 ):
        Pokemon.__init__(self, name, level, poke_type, hp, atk, defense, special_attack, special_defense, speed)

    def attack(self, enemy):
        Pokemon.attack(self, enemy)
        if enemy.poke_type == "Poison" or "Ground" or "Rock":
            choice = random.choice(bulbasaur_moves)
            enemy.hp -= 3
            print(self.name + ' использовал ' + str(choice))
            print(enemy.name + " осталось" + str(enemy.hp) + " здоровья.")


p = (Bulbasaur(), Ivysaur(), Rattata())


def main():
    team1 = (random.choice(p), random.choice(p))
    team2 = (random.choice(p), random.choice(p))
    print()
    while team1[0].hp > 0 and team2[0].hp > 0:
        if team1[0].hp > 0:
            print(team1[0].attack(team2[0]))
            print()
        if team2[0].hp > 0:
            print(team2[0].attack(team1[0]))
            print()

    if team1[0].death():
        print(team2[0].name + " победил!")
        print(team1[0].name + " теряет сознание ")
        print()

        if team2[0].hp > 0:
            print(team1[1].name + " вступает в игрy")
            print(team1[1].attack(team2[0]))
            print()
    else:
        print(team1[0].name + " победил!")
        print(team2[0].name + " теряет сознание")
        print()

        if team1[0].hp > 0:
            print(team2[1].name + " вступает в игрy")
            print(team2[1].attack(team1[0]))
            print()

main()
