#  Vocabulary Builder

A Python application that helps users build and practice vocabulary by saving words/definitions, reviewing them, and quizzing. Includes both a **Command-Line Interface (CLI)** and a **Graphical User Interface (GUI)** with support for loading external word packs.

---

##  Quick Start

```bash
git clone https://github.com/MrDupree1/Vocab-Builder1.git
cd Vocab-Builder1
Run the text version (CLI):

bash
python main.py
Run the GUI version:

bash
python gui.py
No third-party installs needed — everything uses Python’s standard library.

 Features
Review your saved words and definitions from a local file (words.txt).

Quiz mode (definition → type the word) with a Reset option.

Load Pack button in the GUI to import more words from .txt files.

Flexible line parsing: accepts word - definition, word – definition, word — definition, or word : definition.

Beginner-friendly code; works on Windows/macOS/Linux with Python 3.x.

 Requirements
Python 3.x

Standard library only (no extra packages)

🛠 Installation
bash
git clone https://github.com/MrDupree1/Vocab-Builder1.git
cd Vocab-Builder1
(Optional) Create a virtual environment:

bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
▶ Usage
CLI (text version)
bash
python main.py
Menu options:

Review words

Take a quiz

Add a word (quick)

Exit

GUI
bash
python gui.py
 Load Pack — import a .txt file of words (see format below)

 Review Words — shows your current list

 Take Quiz — quizzes you by definition (with Next and Reset)

 Data & Packs
All words are stored in a plain text file at the project root:

words.txt — your personal list (app reads/writes here)

Accepted line formats (any one per line):

arduino
word - definition
word – definition
word — definition
word : definition
Word packs live in the packs/ folder. A sample is included:

bash
packs/sample_pack.txt
Example contents:

css
eloquent - fluent or persuasive in speaking or writing
benevolent - well meaning and kindly
meticulous - showing great attention to detail
In the GUI, click Load Pack and select a .txt file to append those words into words.txt.
Duplicate words are ignored (case-insensitive).

 Project Structure
Vocab-Builder1/
│-- main.py          # Text-based program (CLI)
│-- gui.py           # Graphical User Interface (Tkinter)
│-- words.txt        # Your saved vocabulary list
│-- packs/
│   └─ sample_pack.txt  # Example pack (import via GUI)
│-- README.md
│-- .gitignore
 Notes
Quiz skips entries with missing definitions (e.g., “TBD”).

You can mix your own packs; just keep the word - definition style (or the supported separators above).

If words.txt is missing, the app will create it on first save.

 License
Open-source, MIT-style.
