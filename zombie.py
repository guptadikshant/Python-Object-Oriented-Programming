from enemy import Enemy


class Zombie(Enemy):
    def __init__(self, type_of_enemy: str, health_points: int = 10 , attack_damage: int = 1) -> None:
        super().__init__(type_of_enemy=type_of_enemy, health_points=health_points, attack_damage=attack_damage)

    def talk(self):
        print("Grumbling........")

    def spread_infection(self):
        print("spreading the infection.....")