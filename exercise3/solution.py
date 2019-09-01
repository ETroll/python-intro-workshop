import random

def solution() -> None:
    print("Rock Paper Scissors game")

    gameActive = True

    wordDict: dict = {
        1: "rock",
        2: "paper",
        3: "scissors"
    }

    while(gameActive):
        print("Pick an option:")

        for key, value in wordDict.items():
            print(f"{key}. {value.capitalize()}")

        try:
            choice : int = int(input("Option: "))
        except ValueError:
            print("You did not enter a valid number. Try again.")
            continue
        except Exception as e:
            print(f"Error: {e}")
            print("Quitting")
            gameActive = False
        else:
            if 4 > choice > 0:
                computerChoice: int = random.randint(1,3)
                diff: int = choice - computerChoice

                if diff in [-2, 1]:
                    print(f"{wordDict[choice].capitalize()} beats {wordDict[computerChoice]}. You WIN!")
                elif diff in [2, -1]:
                    print(f"{wordDict[computerChoice].capitalize()} beats {wordDict[choice]}. You LOOSE!")
                else:
                    print(f"Both choose {wordDict[choice]}. It is a draw..")
            else:
                print("You did not enter a valid number (between 1 and 3). Try again.")
                continue

        if input("Do you want to play again? [y/n]") == "y":
            continue
        else:
            gameActive = False
