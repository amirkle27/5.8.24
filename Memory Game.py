def memory_game (i1:str = "", i2:str = "") -> list:
    import random
    letters: list = ['A','A','B','B','C','C','D','D','E','E','F','F']
    count: int = 12
    while True:
        try:
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
                    i1: int = int(input(f"Please select a number between 1-{count}"))
                    print(f"You chose the letter '{letters[i1-1]}'")
                    i2: int = int(input(f"Please select another card between 1-{count}"))
                    print(f"You chose the letter '{letters[i2-1]}'")
                except:
                    print("Wrong Key...")
                    continue
                if letters[i1-1]==letters[i2-1] and letters:
                    print("Yeah! You've found a pair! keep going!!")
                    letters [i1-1], letters [i2-1] = "",""
                    letters.remove("")
                    letters.remove("")
                    count -= 2
            else:
                print("Wow! you won!")
                ans: str = str(input("Wanna play a new game?"))
                if ans not in ['yes', 'y', 'no', 'n']:
                    print("Please answer 'yes' or 'no'")
                    continue
                elif ans in ['no', 'n']:
                    print("Sorry to see you go. Goodbye!")
                    break
                letters: list = ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D', 'E', 'E', 'F', 'F']
                count: int = 12
        except:
            print("Wrong Key...")

memory_game()