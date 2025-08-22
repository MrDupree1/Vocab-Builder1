# main.py — simple text (CLI) version matching gui.py behavior
from pathlib import Path
import random
import sys

WORDS_FILE = Path("words.txt")
SEPARATORS = [" - ", " – ", " — ", " : "]   # support hyphen, en dash, em dash, colon
PRIMARY_SEP = " - "

def ensure_file():
    if not WORDS_FILE.exists():
        WORDS_FILE.write_text("", encoding="utf-8")

def split_word_def(line: str):
    for sep in SEPARATORS:
        if sep in line:
            w, d = line.split(sep, 1)
            return w.strip(), d.strip()
    return line.strip(), ""   # no separator

def load_pairs():
    ensure_file()
    pairs, seen = [], set()
    for raw in WORDS_FILE.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if not line:
            continue
        w, d = split_word_def(line)
        key = w.lower()
        if key not in seen:
            seen.add(key)
            pairs.append((w, d if d else "TBD"))
    return pairs

def save_pair(word, definition="TBD"):
    word = (word or "").strip()
    definition = (definition or "TBD").strip()
    if not word:
        return False, "Word cannot be empty."
    for w, _ in load_pairs():
        if w.lower() == word.lower():
            return False, "That word already exists."
    with WORDS_FILE.open("a", encoding="utf-8", newline="\n") as f:
        f.write(f"{word}{PRIMARY_SEP}{definition}\n")
    return True, f"Saved “{word}”"

def review():
    pairs = load_pairs()
    if not pairs:
        print("Your list is empty. Add words via GUI or load a pack.")
        return
    print("\n=== Vocabulary List ===")
    for w, d in pairs:
        print(f"- {w}: {d}")
    print(f"Total: {len(pairs)} words\n")

def quiz():
    pairs = load_pairs()
    pool = [(w, d) for (w, d) in pairs if d and d.upper() != "TBD"]
    if not pool:
        print("\nNo definitions found to quiz on.")
        print('Make sure lines look like:  word - definition\n')
        return
    correct = 0
    total = 0
    random.shuffle(pool)
    for w, d in pool:
        print("\nDefinition:\n" + d)
        ans = input("Type the word (or ENTER to quit): ").strip()
        if not ans:
            break
        total += 1
        if ans.lower() == w.lower():
            print("✅ Correct!")
            correct += 1
        else:
            print(f"❌ Incorrect. Correct word: {w}")
    if total:
        print(f"\nScore: {correct}/{total}\n")

def menu():
    while True:
        print("====== Vocabulary Builder (CLI) ======")
        print("1) Review words")
        print("2) Take a quiz")
        print("3) Add a word (quick)")
        print("4) Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            review()
        elif choice == "2":
            quiz()
        elif choice == "3":
            w = input("Word: ").strip()
            if not w:
                print("Word cannot be empty.\n"); continue
            d = input("Definition (leave blank for TBD): ").strip() or "TBD"
            ok, msg = save_pair(w, d)
            print(msg + "\n")
        elif choice == "4":
            print("Goodbye!")
            return
        else:
            print("Invalid choice.\n")

if __name__ == "__main__":
    ensure_file()
    try:
        menu()
    except KeyboardInterrupt:
        print("\nExiting...")
        sys.exit(0)
