# gui.py — GUI with Load Pack, flexible separators, resettable quiz
import tkinter as tk
from tkinter import messagebox, simpledialog, filedialog
from pathlib import Path
import random

WORDS_FILE = Path("words.txt")
SEPARATORS = [" - ", " – ", " — ", " : "]   # support hyphen, en dash, em dash, colon
PRIMARY_SEP = " - "                          # when we save, we use this

# Small built-in fallback dictionary (used if no definition is found)
BUILTIN_DEFS = {
    "abate": "to lessen",
    "abdicate": "to give up power",
    "ambiguous": "unclear",
    "amiable": "friendly",
    "benevolent": "kind",
    "candid": "honest",
    "coerce": "to force",
    "concise": "brief",
    "diligent": "hardworking",
    "elucidate": "to explain",
    "feasible": "possible",
    "frugal": "thrifty",
    "gregarious": "sociable",
    "impeccable": "flawless",
    "innate": "inborn",
    "lucid": "clear",
    "meticulous": "very careful",
    "obsolete": "out of date",
    "pragmatic": "practical",
    "succinct": "brief and to the point",
}

def ensure_file():
    if not WORDS_FILE.exists():
        WORDS_FILE.write_text("", encoding="utf-8")

def split_word_def(line: str):
    """Split a line into (word, definition) using any known separator."""
    for sep in SEPARATORS:
        if sep in line:
            w, d = line.split(sep, 1)
            return w.strip(), d.strip()
    return line.strip(), ""   # no separator found

def load_pairs():
    """Return list of (word, definition) from words.txt (de-dup by word, case-insensitive)."""
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

def find_definition_in_file(word):
    """Look up a definition for `word` already stored in the file."""
    for w, d in load_pairs():
        if w.lower() == word.lower() and d and d.upper() != "TBD":
            return d
    return None

def save_pair(word, definition):
    """Append a word/definition if not already present."""
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

class QuizWindow(tk.Toplevel):
    """Simple quiz window with Next/Reset."""
    def __init__(self, master, pool):
        super().__init__(master)
        self.title("Quiz")
        self.pool_all = pool[:]         # keep full pool
        self.pool_current = pool[:]     # mutable pool we randomize through
        self.correct = 0
        self.asked = 0

        tk.Label(self, text="Type the word for the given definition:").pack(padx=12, pady=(12, 6))

        self.lbl_def = tk.Label(self, text="", justify="left", wraplength=420)
        self.lbl_def.pack(padx=12, pady=(0, 8))

        self.entry = tk.Entry(self, width=40)
        self.entry.pack(padx=12, pady=(0, 8))
        self.entry.focus_set()

        row = tk.Frame(self); row.pack(pady=(2, 10))
        tk.Button(row, text="Submit", width=10, command=self.check).pack(side="left")
        tk.Button(row, text="Next", width=10, command=self.next_question).pack(side="left", padx=6)
        tk.Button(row, text="Reset", width=10, command=self.reset_quiz).pack(side="left")

        self.lbl_score = tk.Label(self, text="")
        self.lbl_score.pack(pady=(0, 8))

        self.next_question()

    def reset_quiz(self):
        self.pool_current = self.pool_all[:]
        self.correct = 0
        self.asked = 0
        self.next_question()

    def next_question(self):
        if not self.pool_current:
            self.pool_current = self.pool_all[:]
        random.shuffle(self.pool_current)
        self.word, self.definition = self.pool_current.pop()
        self.lbl_def.config(text=f"Definition:\n{self.definition}")
        self.entry.delete(0, "end")
        self.entry.focus_set()
        self.lbl_score.config(text=f"Score: {self.correct}/{self.asked}")

    def check(self):
        guess = self.entry.get().strip().lower()
        self.asked += 1
        if guess == self.word.lower():
            self.correct += 1
            messagebox.showinfo("Result", "✅ Correct!")
        else:
            messagebox.showinfo("Result", f"❌ Incorrect.\nCorrect word: {self.word}")
        self.next_question()

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("📚 Vocabulary Builder")
        self.geometry("540x440")
        self.option_add("*Font", "Arial 11")

        header = tk.Label(self, text="Vocabulary Builder", font=("Arial", 16, "bold"))
        header.pack(pady=(14, 8))

        card = tk.Frame(self, bd=1, relief="groove")
        card.pack(fill="x", padx=16, pady=8, ipadx=8, ipady=8)

        tk.Label(card, text="Load word packs and quiz yourself. Review shows your current list.")\
            .pack(padx=8, pady=(6, 2), anchor="w")

        row_btns = tk.Frame(card); row_btns.pack(fill="x", padx=8, pady=(10, 6))
        tk.Button(row_btns, text="📦 Load Pack",   width=16, command=self.on_load_pack).pack(side="left")
        tk.Button(row_btns, text="📖 Review Words", width=16, command=self.on_review).pack(side="left", padx=8)
        tk.Button(row_btns, text="❓ Take Quiz",    width=16, command=self.on_quiz).pack(side="left")

        self.lbl_tip = tk.Label(self, fg="#666"); self.lbl_tip.pack(pady=(6, 0))
        self.status = tk.Label(self, anchor="w", bg="#f2f2f2"); self.status.pack(side="bottom", fill="x")
        self.set_status("Ready.")
        self.refresh_count()

    def set_status(self, msg): self.status.config(text="  " + msg)
    def refresh_count(self): self.lbl_tip.config(text=f"{len(load_pairs())} words in your list • File: {WORDS_FILE.name}")

    # --------- actions ---------
    def on_load_pack(self):
        path = filedialog.askopenfilename(
            title="Select a word pack (.txt)",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if not path:
            self.set_status("Load cancelled."); return

        existing = {w.lower() for (w, _) in load_pairs()}
        added = 0
        try:
            with open(path, "r", encoding="utf-8") as f:
                for raw in f:
                    line = raw.strip()
                    if not line:
                        continue
                    w, d = split_word_def(line)
                    key = w.lower()
                    if not key or key in existing:
                        continue
                    with WORDS_FILE.open("a", encoding="utf-8", newline="\n") as out:
                        out.write(f"{w}{PRIMARY_SEP}{(d or 'TBD')}\n")
                    existing.add(key)
                    added += 1
            self.refresh_count()
            self.set_status(f"Loaded {added} new words from pack.")
            messagebox.showinfo("Load Pack", f"Added {added} new words.")
        except Exception as e:
            messagebox.showerror("Load Pack", f"Could not load pack:\n{e}")
            self.set_status("Load failed.")

    def on_review(self):
        pairs = load_pairs()
        if not pairs:
            messagebox.showinfo("Review Words", "Your list is empty. Load a pack first."); return
        text = "\n".join(f"• {w}: {d}" for w, d in pairs[:600])
        if len(pairs) > 600:
            text += f"\n\n(+ {len(pairs) - 600} more not shown)"
        messagebox.showinfo("Review Words", text)
        self.set_status("Displayed your vocabulary list.")

    def on_quiz(self):
        pairs = load_pairs()
        pool = [(w, d) for (w, d) in pairs if d and d.upper() != "TBD"]
        if not pool:
            messagebox.showinfo(
                "Quiz",
                "No definitions found to quiz on.\n\nLoad a pack with lines like:\nword - definition\nor\nword – definition"
            )
            return
        QuizWindow(self, pool)

if __name__ == "__main__":
    ensure_file()
    App().mainloop()
