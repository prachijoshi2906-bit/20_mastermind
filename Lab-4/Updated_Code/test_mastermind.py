from game import DIFFICULTIES, Mastermind
from logic import feedback

assert feedback(list("1234"), list("1234")) == (4, 0)
assert feedback(list("1234"), list("5678")) == (0, 0)
assert feedback(list("1234"), list("2143")) == (0, 4)
assert feedback(list("1123"), list("1111")) == (2, 0)
assert feedback(list("1122"), list("1212")) == (2, 2)
assert feedback(list("1122"), list("2211")) == (0, 4)

for name, settings in DIFFICULTIES.items():
    game = Mastermind(name)
    assert len(game.code) == settings["length"]
    assert all(ch in settings["symbols"] for ch in game.code)
    assert game.turns == settings["turns"]

game = Mastermind("medium")
before = game.turns
assert not game._valid_guess("12")
assert not game._valid_guess("12x4")
assert game.turns == before

print("All Mastermind tests passed.")
