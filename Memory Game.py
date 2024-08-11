
def memory_game (i1:str = "", i2:str = "") -> None:
    import random
    while True:
            letters: list = ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D', 'E', 'E', 'F', 'F']
            ans: str = str(input("Wanna play a new game? (yes/no)").lower())
            if ans not in ['yes','y','no','n']:
                print("Please answer 'yes' or 'no'")
                continue
            elif ans in ['no','n']:
                print("Sorry to see you go. Goodbye!")
                break
            random.shuffle(letters)
            while letters:
                try:
                    i1: int = int(input(f"Please select a number between 1-{len(letters)}"))
                    print(f"You chose the letter '{letters[i1-1]}'")
                    i2: int = int(input(f"Please select another card between 1-{len(letters)}"))
                    print(f"You chose the letter '{letters[i2-1]}'")
                    if i1 == i2:
                        print(f"You already chose {i1}. Try something else")
                        continue
                except:
                    print("Wrong Key...")
                    continue
                if letters[i1-1]==letters[i2-1] and letters:
                    print("Yeah! You've found a pair! keep going!!")
                    letters [i1-1], letters [i2-1] = "",""
                    letters.remove("")
                    letters.remove("")
            else:
                print("Wow! you won!")

memory_game()
