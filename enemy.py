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