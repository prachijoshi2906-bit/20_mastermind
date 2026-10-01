import random
from logic import feedback

DIFFICULTIES = {
    "easy": {"length": 3, "symbols": "1234", "turns": 10},
    "medium": {"length": 4, "symbols": "123456", "turns": 10},
    "hard": {"length": 5, "symbols": "12345678", "turns": 8},
}

class Mastermind:
    def __init__(self, difficulty="medium"):
        difficulty = difficulty.lower()
        if difficulty not in DIFFICULTIES:
            raise ValueError("Invalid difficulty.")

        settings = DIFFICULTIES[difficulty]
        self.difficulty = difficulty
        self.code_length = settings["length"]
        self.symbols = settings["symbols"]
        self.turns = settings["turns"]
        self.history = []
        self.code = [random.choice(self.symbols) for _ in range(self.code_length)]
        self.game_over = False
        self.won = False

    def _valid_guess(self, raw):
        return len(raw) == self.code_length and all(ch in self.symbols for ch in raw)

    def _show_history(self):
        print("\nGuess history:")
        for number, (guess, exact, partial) in enumerate(self.history, 1):
            print(f"{number}. {guess} -> Exact: {exact}, Partial: {partial}")

    def run(self):
        print(
            f"Mastermind — {self.difficulty.title()} mode. "
            f"Enter {self.code_length} digits using {self.symbols}."
        )

        while self.turns > 0 and not self.game_over:
            raw = input(f"{self.turns} turns left > ").strip()

            if raw.lower() == "q":
                self.game_over = True
                print("Game quit. Thanks for playing!")
                return

            if not self._valid_guess(raw):
                print(f"Enter exactly {self.code_length} digits using only {self.symbols}.")
                continue

            exact, partial = feedback(self.code, list(raw))
            self.history.append((raw, exact, partial))
            self.turns -= 1
            print("Exact:", exact, " Partial:", partial)

            if exact == self.code_length:
                self.won = True
                self.game_over = True
                print("Cracked the code!")
                self._show_history()
                return

        self.game_over = True
        print("Out of turns. The code was", "".join(self.code))
        self._show_history()
