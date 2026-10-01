from game import DIFFICULTIES, Mastermind

def choose_difficulty():
    print("Choose difficulty:")
    print("1. Easy   - 3 digits, symbols 1-4, 10 turns")
    print("2. Medium - 4 digits, symbols 1-6, 10 turns")
    print("3. Hard   - 5 digits, symbols 1-8, 8 turns")
    choices = {"1": "easy", "2": "medium", "3": "hard"}

    while True:
        choice = input("Difficulty > ").strip().lower()
        if choice in choices:
            return choices[choice]
        if choice in DIFFICULTIES:
            return choice
        print("Choose 1, 2, 3, or enter easy, medium, or hard.")

if __name__ == "__main__":
    Mastermind(choose_difficulty()).run()
