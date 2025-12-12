from pathlib import Path


def read_grid(path: Path):
    with path.open("r", encoding="utf8") as f:
        return [line.rstrip("\n") for line in f]


def read_directions(path: Path):
    res = []
    with path.open("r", encoding="utf8") as f:
        for line in f:
            t = line.strip().upper()
            if t == "R":
                res.append(1)
            elif t == "L":
                res.append(-1)
            else:
                res.append(0)
    return res


def rotate_row(chars, shift):
    n = len(chars)
    if n == 0:
        return chars
    s = shift % n
    return chars[-s:] + chars[:-s]

def compute_clue1(grid_path, dir_path):
    grid = read_grid(Path(grid_path))
    dirs = read_directions(Path(dir_path))

    new_rows = []
    for i, row in enumerate(grid):
        shift = dirs[i] if i < len(dirs) else 0
        rotated = rotate_row(list(row), shift)
        new_rows.append("".join(rotated))

    center = len(new_rows) // 2
    center_row = new_rows[center]
    return sum(ord(c) for c in center_row)

if __name__ == "__main__":
    base = Path.cwd() / "inputs"
    grid = base / "grid.txt"
    dirs = base / "directions.txt"
    print(compute_clue1(grid, dirs))
