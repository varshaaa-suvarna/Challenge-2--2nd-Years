from pathlib import Path

VOWELS = set("aeiouAEIOU")

def compute_clue2(path):
    text = Path(path).read_text(encoding="utf8")

    
    text = text[::-1]

    
    filtered = ""
    for i, ch in enumerate(text, start=1):
        if i % 3 != 0:
            filtered += ch

    
    shifted = "".join(chr(ord(c) + 2) for c in filtered)

    
    return sum(1 for c in shifted if c in VOWELS)

if __name__ == "__main__":
    base = Path.cwd() / "inputs" / "input2.txt"
    print(compute_clue2(base))
