class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        remaining = Counter()

        # First pass: count bulls and unmatched secret digits
        for s, g in zip(secret, guess):
            if s == g:
                bulls += 1
            else:
                remaining[s] += 1

        # Second pass: count cows from unmatched guess digits
        for i, g in enumerate(guess):
            if secret[i] != g and remaining[g] > 0:
                cows += 1
                remaining[g] -= 1

        return f"{bulls}A{cows}B"
