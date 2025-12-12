# SOSC Challenge – Round 2 (Coding Puzzle Challenge)


## 🔹 Problem 1 – Grid Transform
**Inputs:** `grid.txt`, `directions.txt`  
- Performed row-wise rotations using direction instructions (R = rotate right, L = rotate left).  
- After all rotations, extracted the **central row** (index = floor(n/2)).  
- Computed **Clue 1** as the sum of ASCII values (`ord()`) of all characters in that row.

**Result:**  
- Clue 1 = **385**  
- Hexadecimal of Clue 1 = **181**



## 🔹 Problem 2 – Multi-Pass String Process
**Input:** `input2.txt`  
Steps followed exactly as described:
1. Reversed the entire string.  
2. Removed every **3rd character** (1-indexed positions 3, 6, 9, …).  
3. Applied a **+2 ordinal shift** to every remaining character.  
4. Counted all **vowel-class characters** (a, e, i, o, u — case-insensitive).

**Result:**  
Clue 2 = **4**



## 🔹 Problem 3 – State Sequence Simulation
**Input:** `states.txt`  
Rules applied:
- **Prime numbers** → Jump directly to the terminal state (state 3).  
- **Even numbers** → Advance by +1 state per pass until reaching state 3.  
- **Odd composite numbers / 1** → Do not advance.

After simulating up to 10 passes, counted how many numbers reached the final state.

**Result:**  
Clue 3 = **7**



## 🔹 Final Key Construction
According to the challenge rules:

