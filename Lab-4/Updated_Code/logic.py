def feedback(code, guess):
    """Return (exact, partial) using duplicate-aware Mastermind rules."""
    exact = 0
    remaining_code = []
    remaining_guess = []

    for code_symbol, guess_symbol in zip(code, guess):
        if code_symbol == guess_symbol:
            exact += 1
        else:
            remaining_code.append(code_symbol)
            remaining_guess.append(guess_symbol)

    partial = 0
    used = [False] * len(remaining_code)

    for guess_symbol in remaining_guess:
        for i, code_symbol in enumerate(remaining_code):
            if not used[i] and guess_symbol == code_symbol:
                partial += 1
                used[i] = True
                break

    return exact, partial
