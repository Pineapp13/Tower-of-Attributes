import random
on = 0
first = 0
print("btw block doesn't work yet")
while not on == str("yes"):
    combat = 0
    floor_num = 1
    heart = (random.randint(1,3))
    head = (random.randint(1,3))
    on = input("Risk your life in the tower of attributes? ")
    while on == str("yes"):
        print("---------------")
        if first == 0:
            input("You find a strange creature, its seems to follow you around.")
            input("Upon further inspection the creature is quite friendly.")
            input("It has two large gemstones in its body.") 
            input("one close to its brain the other near the heart.")
            print("---------------")
            first = 1
        while on == str("yes"):
            pet_name = 0
            base_pet_health = 100
            base_pet_damage = 17
            pet_damage_taken_multiplier = 1
            if head == 1:
                pet_name = str("Heavenly ")
                base_pet_health = base_pet_health + 15
            if head == 2:
                pet_name = str("Hellish ")
                base_pet_damage = base_pet_damage + 3
            if head == 3:
                pet_name = str("Shelled ")
                pet_damage_taken_multiplier = pet_damage_taken_multiplier - 0.1
            if heart == 1:
                pet_name = pet_name + str("Angel")
                base_pet_health = base_pet_health + 25
            if heart == 2:
                pet_name = pet_name + str("Demon")
                base_pet_damage = base_pet_damage + 5
            if heart == 3:
                pet_name = pet_name + str("Turtle")
                pet_damage_taken_multiplier = pet_damage_taken_multiplier - 0.1
            print("You are on floor " + str(floor_num))
            combat = input("Do you wish to open the door leading to the stair room? ")
            print("---------------")
            while combat == str("yes"):
                enemy_health = 0
                enemy_damage = 0
                base_enemy_health = 100
                base_enemy_damage = 17
                enemy_damage_taken_multiplier = 1
                enemy_name = 0
                enemy_heart = (random.randint(1,3))
                enemy_head = (random.randint(1,3))
                if enemy_head == 1:
                    enemy_name = str("Heavenly ")
                    base_enemy_health = base_enemy_health + 15
                if enemy_head == 2:
                    enemy_name = str("Hellish ")
                    base_enemy_damage = base_enemy_damage + 3
                if enemy_head == 3:
                    enemy_name = str("Shelled ")
                    enemy_damage_taken_multiplier = enemy_damage_taken_multiplier - 0.1
                if enemy_heart == 1:
                    enemy_name = enemy_name + str("Angel")
                    base_enemy_health = base_enemy_health + 25
                if enemy_heart == 2:
                    enemy_name = enemy_name + str("Demon")
                    base_enemy_damage = base_enemy_damage + 5
                if enemy_heart == 3:
                    enemy_name = enemy_name + str("Turtle")
                    enemy_damage_taken_multiplier = enemy_damage_taken_multiplier - 0.1
                enemy_health = base_enemy_health
                enemy_damage = base_enemy_damage
                input("You see an animal similar to yours but it doesn't look too friendly")
                pet_health = base_pet_health
                pet_damage = base_pet_damage
                print(str(pet_name))
                print("Health: " + str(pet_health))
                print("       vs")
                print(str(enemy_name))
                print("Health: " + str(enemy_health))
                print("---------------")
                while combat == str("yes"):
                    pet_action = input("Attack or Block? ")
                    roundstart_pet_health = 0
                    roundstart_enemy_health = 0
                    roundstart_pet_health = pet_health
                    roundstart_enemy_health = enemy_health
                    if pet_action == str("attack"):
                        enemy_health = enemy_health - int(pet_damage * enemy_damage_taken_multiplier)
                        pet_action = 0
                    enemy_action = (random.randint(1,1))
                    if enemy_action == 1 and not enemy_health <= 0:
                        pet_health = pet_health - int(enemy_damage * pet_damage_taken_multiplier)
                        enemy_action = 0
                    print(str(pet_name) + " -" + str(roundstart_pet_health - pet_health))
                    print("Health: " + str(pet_health))
                    print("       vs")
                    print(str(enemy_name) + " -" + str(roundstart_enemy_health - enemy_health))
                    print("Health: " + str(enemy_health))
                    print("---------------")
                    if enemy_health <= 0:
                        input("The enemies body vanished after the final blow.")
                        input("The two gemstones in its body were left behind")
                        combat = 0
                        floor_num = floor_num + 1
                    if pet_health <= 0:
                        print("You died")
                        combat = 0
                        on = 0