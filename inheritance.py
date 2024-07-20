from zombie import Zombie

if __name__ == "__main__":
    zombie = Zombie("Zombie", 10, 1)
    print(zombie.get_type_of_enemy())
    zombie.talk()
    zombie.spread_infection()