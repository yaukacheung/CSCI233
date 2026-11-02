
class Character:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def deal_damage(self):
        print(f"{self.name} attacks the enemy!")


# Warrior subclass
class Warrior(Character):
    def __init__(self, name):
        super().__init__(name, 150)

    def deal_damage(self):
        print(f"{self.name} swings a sword and deals 25 damage!")


# Mage subclass
class Mage(Character):
    def __init__(self, name):
        super().__init__(name, 80)

    def deal_damage(self):
        print(f"{self.name} casts a fireball and deals 40 damage!")


# Healer subclass
class Healer(Character):
    def __init__(self, name):
        super().__init__(name, 100)

    def deal_damage(self):
        print(f"{self.name} uses a magic staff and deals 10 damage!")

    def heal(self, target):
        target.health += 30
        print(f"{self.name} heals {target.name} for 30 health!")
        print(f"{target.name}'s health is now {target.health}.")


# Create different characters
warrior = Warrior("Thor")
mage = Mage("Merlin")
healer = Healer("Luna")

# Store characters in a list
characters = [warrior, mage, healer]

# Polymorphism: Each character performs their own attack
print("=== RPG Battle ===")

for character in characters:
    character.deal_damage()

# Healer challenge
print("\n=== Healing ===")

healer.heal(warrior)
healer.heal(mage)
