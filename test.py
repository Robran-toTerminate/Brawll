options = ["1","2","3"]

def select_option(selection_options):
    selected_index = 0
    while True:
        print("-------------")
        for i in range(0,len(selection_options)):
            output = selection_options[i]
            if selected_index == i:
                output += " <--"
            print(output)
        print("-------------")
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

        


print(select_option(options) + " is selected")