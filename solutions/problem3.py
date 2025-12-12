import math
from pathlib import Path

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False
    r = int(math.sqrt(n))
    for i in range(3, r + 1, 2):
        if n % i == 0:
            return False
    return True

def compute_clue3(path):
    text = Path(path).read_text().strip()
    nums = [int(x) for x in text.split()]

    states = [0] * len(nums)

    for _ in range(10):
        changed = False
        for i, v in enumerate(nums):
            if states[i] == 3:
                continue

            if is_prime(v):
                states[i] = 3
                changed = True
            elif v % 2 == 0:
                states[i] = min(states[i] + 1, 3)
                changed = True
            else:
                pass

        if not changed:
            break

    return states.count(3)

if __name__ == "__main__":
    base = Path.cwd() / "inputs" / "states.txt"
    print(compute_clue3(base))
