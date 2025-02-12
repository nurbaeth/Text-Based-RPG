import random

class Character:
    def __init__(self, name, character_class):
        self.name = name
        self.character_class = character_class
        self.health = 100
        self.attack = 10
        self.defense = 5
        self.gold = 0
        self.experience = 0
        self.level = 1
        self.items = []

        if character_class == 'warrior':
            self.attack += 5
            self.defense += 5
        elif character_class == 'mage':
            self.attack += 8
            self.health += 20
        elif character_class == 'archer':
            self.attack += 6
            self.defense += 3

    def level_up(self):
        self.level += 1
        self.health += 20
        self.attack += 5
        self.defense += 3
        print(f"{self.name} leveled up! You are now level {self.level}.")
    
    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print(f"{self.name} took {damage} damage. Current health: {self.health}")

    def attack_enemy(self, enemy):
        damage = random.randint(self.attack // 2, self.attack)
        print(f"{self.name} attacks {enemy.name} for {damage} damage.")
        enemy.take_damage(damage)

    def is_alive(self):
        return self.health > 0

    def add_gold(self, amount):
        self.gold += amount
        print(f"{self.name} gained {amount} gold. Total gold: {self.gold}")

    def add_experience(self, amount):
        self.experience += amount
        print(f"{self.name} gained {amount} experience. Total experience: {self.experience}")
        if self.experience >= 100:
            self.level_up()
            self.experience = 0

class Enemy:
    def __init__(self, name, health, attack):
        self.name = name
        self.health = health
        self.attack = attack

    def take_damage(self, damage):
        self.health -= damage
        if self.health < 0:
            self.health = 0
        print(f"{self.name} took {damage} damage. Current health: {self.health}")

    def attack_player(self, player):
        damage = random.randint(self.attack // 2, self.attack)
        print(f"{self.name} attacks {player.name} for {damage} damage.")
        player.take_damage(damage)

    def is_alive(self):
        return self.health > 0

class Game:
    def __init__(self):
        self.player = None
        self.enemy = None

    def create_character(self):
        name = input("Enter your character's name: ")
        print("Choose your class: warrior, mage, or archer")
        character_class = input("Enter class: ").lower()
        if character_class not in ['warrior', 'mage', 'archer']:
            print("Invalid class choice. Defaulting to warrior.")
            character_class = 'warrior'
        self.player = Character(name, character_class)
        print(f"{self.player.name}, the {self.player.character_class}, has entered the game!")

    def generate_enemy(self):
        enemies = [
            Enemy("Goblin", 50, 8),
            Enemy("Orc", 80, 12),
            Enemy("Dragon", 200, 20)
        ]
        self.enemy = random.choice(enemies)
        print(f"A wild {self.enemy.name} appeared!")

    def fight(self):
        while self.player.is_alive() and self.enemy.is_alive():
            print(f"\n{self.player.name}'s Health: {self.player.health} | {self.enemy.name}'s Health: {self.enemy.health}")
            action = input("Choose an action: attack, flee: ").lower()
            if action == 'attack':
                self.player.attack_enemy(self.enemy)
                if self.enemy.is_alive():
                    self.enemy.attack_player(self.player)
            elif action == 'flee':
                print(f"{self.player.name} fled the battle.")
                break
            else:
                print("Invalid action. Choose 'attack' or 'flee'.")

        if not self.enemy.is_alive():
            print(f"{self.player.name} defeated {self.enemy.name}!")
            self.player.add_gold(random.randint(10, 50))
            self.player.add_experience(random.randint(20, 50))

    def start(self):
        self.create_character()
        while self.player.is_alive():
            self.generate_enemy()
            self.fight()

            if self.player.is_alive():
                continue_battle = input("Do you want to continue fighting? (yes/no): ").lower()
                if continue_battle != 'yes':
                    print("You decided to leave the dungeon.")
                    break
            else:
                print(f"{self.player.name} has died. Game over!")
                break

if __name__ == "__main__":
    game = Game()
    game.start()
