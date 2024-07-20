# This repo contains examples for Python OOPs concepts
## Abstraction
- Hide the implementation and only show necessary details
to the user
```python
class Enemy:
    type_of_enemy: str
    health_points: int = 10
    attack_damage: int = 1


    def talk(self):
        print(f"I am a {self.type_of_enemy}. Be prepared to fight!")

    def walk_farward(self):
        print(f"{self.type_of_enemy} moves closer to you.")

    def attack(self):
        print(f"{self.type_of_enemy} attacks for {self.attack_damage} damage.")


if __name__ == "__main__":
    enemy = Enemy()
    enemy.type_of_enemy = "Zoombie"
    enemy.talk()
    enemy.walk_farward()
    enemy.attack()
```

## Constructor Example
```python
class Enemy:

    def __init__(self, type_of_enemy: str, health_points: int = 10 , attack_damage: int = 1) -> None:
        self.type_of_enemy = type_of_enemy
        self.health_points = health_points
        self.attack_damage = attack_damage
        

    def talk(self):
        print(f"I am a {self.type_of_enemy}. Be prepared to fight!")

    def walk_farward(self):
        print(f"{self.type_of_enemy} moves closer to you.")

    def attack(self):
        print(f"{self.type_of_enemy} attacks for {self.attack_damage} damage.")


if __name__ == "__main__":
    enemy = Enemy("Zoombie")
    enemy.talk()
    enemy.walk_farward()
    enemy.attack()
```

# Inheritance

```python
class Enemy:

    def __init__(self, type_of_enemy: str, health_points: int = 10 , attack_damage: int = 1) -> None:
        self.__type_of_enemy = type_of_enemy # private attribute
        self.health_points = health_points
        self.attack_damage = attack_damage

    def get_type_of_enemy(self): # getter method to access the private objects
        return self.__type_of_enemy


    def talk(self):
        print(f"I am a {self.__type_of_enemy}. Be prepared to fight!")

    def walk_farward(self):
        print(f"{self.__type_of_enemy} moves closer to you.")

    def attack(self):
        print(f"{self.__type_of_enemy} attacks for {self.attack_damage} damage.")

class Zombie(Enemy):
    def __init__(self, type_of_enemy: str, health_points: int = 10 , attack_damage: int = 1) -> None:
        super().__init__(type_of_enemy=type_of_enemy, health_points=health_points, attack_damage=attack_damage)

    def talk(self):
        print("Grumbling........")

    def spread_infection(self):
        print("spreading the infection.....")

```