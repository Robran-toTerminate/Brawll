import time
import random

selected_index = 0
def select_option(selection_options, vertical = True):
    global selected_index
    print("\033c",end="")
    display_main()
    if vertical:
        selected_index = 0
    while True:
        output = ""
        print("---------------")
        for i in range(0,len(selection_options)):
            if vertical:
                output = selection_options[i]
            else:
                output += selection_options[i]

            if selected_index == i:
                output += " <-- "
            elif not vertical:
                output += "     "
            if vertical:
                print(output)

        if not vertical:
            print(output)

        print("---------------")
        movement = input().lower()
        print(movement)
        if movement == "s":
            selected_index += 1
        elif movement == "w":
            selected_index -= 1
        elif movement == "":
            return selection_options[selected_index]

        if selected_index <0 or selected_index > len(selection_options)-1:
            selected_index = 0
        if not vertical:
            break
        else:
            print("\033c",end="")
            display_main()



player_has_played = False

player_health = 10
enemie_health = 10

def display_main():
    print("---------------")
    print("Your HP :",player_health)
    print("Enemie HP:",enemie_health)
    print("---------------")

    print("   o     =0\   ")
    print("  lv\     0uo- ")
    print("  / |    o  o  ")

    print("---------------")

def kick_animation(damage_dealt):
    print("\033c",end="")

    print("---------------")
    print("")
    print("")

    print("---------------")

    print("   o     =0\   ")
    print("  lv\     0uo- ")
    print("  / |    o  o  ")

    print("---------------")
    time.sleep(0.5)
    print("\033c",end="")

    print("---------------")
    print("")
    print("")

    print("---------------")

    print("   /v/  =0\    ")
    print("   / |   0uo-  ")
    print("        o  o   ")

    print("---------------")
    time.sleep(0.5)
    print("\033c",end="")

    print("---------------")
    print(damage_dealt)
    print("DAMAGE!")

    print("---------------")

    print("   /0|__=0\    ")
    print("   /     0uo.!  ")
    print("        o  o   ")

    print("---------------")
    time.sleep(0.5)
    print("\033c",end="")

    print("---------------")
    print(damage_dealt)
    print("DAMAGE!")

    print("---------------")

    print("   /v/  =0\    ")
    print("   / |   0uo.! ")
    print("        o  o   ")

    print("---------------")
    time.sleep(0.5)
    print("\033c",end="")
    display_main()
def punch_animation(damage_dealt):
    print("\033c",end="")
    print("---------------")
    print("")
    print("")

    print("---------------")

    print("   o     =0\   ")
    print("  lv\     0uo- ")
    print("  / |    o  o  ")

    print("---------------")
    time.sleep(0.5) 

    print("\033c",end="")
    print("---------------")
    print("")
    print("")

    print("---------------")

    print("   o     =0\   ")
    print("  v0-     0uo- ")
    print("  / |    o  o  ")

    print("---------------")
    time.sleep(0.3) 

    print("\033c",end="")
    print("---------------")
    print("")
    print("")

    print("---------------")

    print("   o     =0\   ")
    print("  _0v     0uo- ")
    print("  / |    o  o  ")

    print("---------------")
    time.sleep(0.7) 

    print("\033c",end="")
    print("---------------")
    print(damage_dealt)
    print("DAMAGE!")

    print("---------------")

    print("   o     =0\   ")
    print("  _0------0uo.!")
    print("  / |    o  o  ")

    print("---------------")
    time.sleep(0.2) 

    print("\033c",end="")
    print("---------------")
    print(damage_dealt)
    print("DAMAGE!")

    print("---------------")

    print("   o     =0\   ")
    print("  _0v     0uo.!")
    print("  / |    o  o  ")

    print("---------------")
    time.sleep(0.5) 

def enemie_high_attack_animation(damage_dealt):
    print("\033c",end="")
    print("---------------")
    print("")
    print("")

    print("---------------")

    print("   o     =0\   ")
    print("  lv\     0uo- ")
    print("  / |    o  o  ")

    print("---------------")
    time.sleep(0.5)

    print("\033c",end="")
    print("---------------")
    print("")
    print("")

    print("---------------")

    print("   o           ")
    print("  lv\    =0uo- ")
    print("  / |          ")

    print("---------------")
    time.sleep(0.2)

    print("\033c",end="")
    print("---------------")
    print("")
    print("")

    print("---------------")

    print("   o     o  o  ")
    print("  lv\     0uo- ")
    print("  / |    =0\   ")

    print("---------------")
    time.sleep(0.5)

    print("\033c",end="")
    print("---------------")
    print("")
    print("")

    print("---------------")

    print("   o   o    o  ")
    print("  lv\     0uo- ")
    print("  / |    =0\   ")

    print("---------------")
    time.sleep(0.1)

    print("\033c",end="")
    print("---------------")
    print(damage_dealt)
    print("DAMAGE TAKEN")

    print("---------------")

    print("   !o       o  ")
    print("  lv\     0uo- ")
    print("  / |    =0\   ")

    print("---------------")
    time.sleep(0.5)

    print("\033c",end="")
    print("---------------")
    print(damage_dealt)
    print("DAMAGE TAKEN")

    print("---------------")

    print("   o   o    o  ")
    print("  lv\     0uo- ")
    print("  / |    =0\   ")

    print("---------------")
    time.sleep(0.1)

    print("\033c",end="")
    print("---------------")
    print(damage_dealt)
    print("DAMAGE TAKEN")

    print("---------------")

    print("   o     o  o  ")
    print("  lv\     0uo- ")
    print("  / |    =0\   ")

    print("---------------")
    time.sleep(0.3)

    print("\033c",end="")
    print("---------------")
    print(damage_dealt)
    print("DAMAGE TAKEN")

    print("---------------")

    print("   o           ")
    print("  lv\    =0uo- ")
    print("  / |          ")

    print("---------------")
    time.sleep(0.2)
def enemie_low_attack_animation(damage_dealt):
    print("\033c",end="")
    print("---------------")
    print("")
    print("")

    print("---------------")

    print("   o     =0\   ")
    print("  lv\     0uo- ")
    print("  / |    o  o  ")

    print("---------------")
    time.sleep(0.5)

    print("\033c",end="")
    print("---------------")
    print("")
    print("")

    print("---------------")

    print("   o           ")
    print("  lv\    =0\ / ")
    print("  / |   o 0uo o")

    print("---------------")
    time.sleep(0.5)

    print("\033c",end="")
    print("---------------")
    print("")
    print("")

    print("---------------")

    print("   o           ")
    print("  lv\    =0\ / ")
    print("  / |  o  0uo o")

    print("---------------")
    time.sleep(0.1)

    print("\033c",end="")
    print("---------------")
    print(damage_dealt)
    print("DAMAGE TAKEN")

    print("---------------")

    print("   !           ")
    print("  lv\    =0\ / ")
    print("  / |o    0uo o")

    print("---------------")
    time.sleep(0.3)

    print("\033c",end="")
    print("---------------")
    print(damage_dealt)
    print("DAMAGE TAKEN")

    print("---------------")

    print("   !           ")
    print("  lv\    =0\ / ")
    print("  / |  o  0uo o")

    print("---------------")
    time.sleep(0.2)

    print("\033c",end="")
    print("---------------")
    print(damage_dealt)
    print("DAMAGE TAKEN")

    print("---------------")

    print("   !     =0\    ")
    print("  lv\     0uo- ")
    print("  / |    o  o  ")

    print("---------------")
    time.sleep(0.5)

def enemie_blocked_high_animation(damage_dealt):
    print("\033c",end="")
    print("---------------")
    print("")
    print("")

    print("---------------")

    print("   o     =0\   ")
    print("  lv\     0uo- ")
    print("  / |    o  o  ")

    print("---------------")
    time.sleep(0.5)

    print("\033c",end="")
    print("---------------")
    print("")
    print("")

    print("---------------")

    print("   o           ")
    print("  lv\    =0uo- ")
    print("  / |          ")

    print("---------------")
    time.sleep(0.2)

    print("\033c",end="")
    print("---------------")
    print("")
    print("")

    print("---------------")

    print("   o     o  o  ")
    print("  lv\     0uo- ")
    print("  / |    =0\   ")

    print("---------------")
    time.sleep(0.5)

    print("\033c",end="")
    print("---------------")
    print("")
    print("")

    print("---------------")

    print("   o   o    o  ")
    print("  lv-     0uo- ")
    print("  / |    =0\   ")

    print("---------------")
    time.sleep(0.1)

    print("\033c",end="")
    print("---------------")
    print(damage_dealt)
    print("DAMAGE BLOCKED")

    print("---------------")

    print("   o|o      o  ")
    print("  lv     0uo- ")
    print("  / |    =o\   ")

    print("---------------")
    time.sleep(0.5)

    print("\033c",end="")
    print("---------------")
    print(damage_dealt)
    print("DAMAGE BLOCKED")

    print("---------------")

    print("   o    o   o  ")
    print("  lv-    0uo- ")
    print("  / |    =o\   ")

    print("---------------")
    time.sleep(0.3)

    print("\033c",end="")
    print("---------------")
    print(damage_dealt)
    print("DAMAGE BLOCKED")

    print("---------------")

    print("   o     o  o  ")
    print("  lv\     0uo- ")
    print("  / |    =o\   ")

    print("---------------")
    time.sleep(0.3)

    print("\033c",end="")
    print("---------------")
    print(damage_dealt)
    print("DAMAGE BLOCKED")

    print("---------------")

    print("   o           ")
    print("  lv\    =0uo- ")
    print("  / |          ")

    print("---------------")
    time.sleep(0.2)
def enemie_blocked_low_animation(damage_dealt):
    print("\033c",end="")
    print("---------------")
    print("")
    print("")

    print("---------------")

    print("   o     =0\   ")
    print("  lv\     0uo- ")
    print("  / |    o  o  ")

    print("---------------")
    time.sleep(0.5)

    print("\033c",end="")
    print("---------------")
    print("")
    print("")

    print("---------------")

    print("   o           ")
    print("  lv\    =0\ / ")
    print("  / |   o 0uo o")

    print("---------------")
    time.sleep(0.5)

    print("\033c",end="")
    print("---------------")
    print("")
    print("")

    print("---------------")

    print("   o           ")
    print("  lv\    =0\ / ")
    print("  //  o  0uo o")

    print("---------------")
    time.sleep(0.1)

    print("\033c",end="")
    print("---------------")
    print(damage_dealt)
    print("DAMAGE BLOCKED")

    print("---------------")

    print("   o           ")
    print("  lv\    =o\ / ")
    print(" -/- o    0uo o")

    print("---------------")
    time.sleep(0.5)

    print("\033c",end="")
    print("---------------")
    print(damage_dealt)
    print("DAMAGE BLOCKED")

    print("---------------")

    print("   o           ")
    print("  lv\    =o\ / ")
    print("  //   o  0uo o")

    print("---------------")
    time.sleep(0.2)

    print("\033c",end="")
    print("---------------")
    print(damage_dealt)
    print("DAMAGE BLOCKED")

    print("---------------")

    print("   o     =0\    ")
    print("  lv\     0uo- ")
    print("  / |    o  o  ")

    print("---------------")
    time.sleep(0.5)



fight_moves = ["Kick","Punch"]
block_moves = ["High","Low"]
menu_options = ["Fight", "Block"]

while True:
    menu_selection = select_option(menu_options, False)
    current_block_status = ""
    if menu_selection == "Fight":
        player_has_played = True

        selected_action = select_option(fight_moves)

        if selected_action == "Kick":
            damage_dealt = random.randint(2,5)
            enemie_health -= damage_dealt
            kick_animation(damage_dealt)

        elif selected_action == "Punch":
            damage_dealt = random.randint(3,4)
            enemie_health -= damage_dealt
            punch_animation(damage_dealt)


    elif menu_selection == "Block":
        player_has_played = True
        current_block_status = select_option(block_moves)




    print("\033c",end="")

    if enemie_health <= 0:
        print("---------------")
        print("")
        print("")

        print("---------------")

        print("               ")
        print("    YOU WIN    ")
        print("               ")

        print("---------------")
        print("---------------")
        print("")
        print("")

        print("---------------")

        break

        #Enemy logik och så

    if player_has_played:
        player_has_played = False
        if random.randint(0,1) == 1:
            damage_dealt = random.randint(1,4)

            if current_block_status != "Low":
                player_health -= damage_dealt
                enemie_low_attack_animation(damage_dealt)
            else:
                enemie_blocked_low_animation(damage_dealt)
        else:
            damage_dealt = random.randint(2,3)

            if current_block_status != "High":
                player_health -= damage_dealt
                enemie_high_attack_animation(damage_dealt)
            else:
                enemie_blocked_high_animation(damage_dealt)
  
    if player_health <= 0:
        print("---------------")
        print("")
        print("")

        print("---------------")

        print("               ")
        print("   GAME OVER   ")
        print("               ")

        print("---------------")
        print("---------------")
        print("   YOU LOSE    ")
        print("               ")

        print("---------------")

        break

