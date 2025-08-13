# 📚 Vocabulary Builder

A simple Python application that helps users build and practice their vocabulary by tracking words, definitions, and progress.

---

## ⚡ Quick Start (3 Steps)
```bash
git clone https://github.com/MrDupree1/Vocab-Builder1.git
cd Vocab-Builder1
python main.py
No extra installs needed — just run it and follow the menu prompts.

🚀 Features
Add new words and their definitions to your personal vocabulary list.

Review your saved words from a local file.

Quiz yourself on saved words to reinforce learning.

🛠 Requirements
Python 3.x

No third-party packages required (standard library only)

📦 Installation
Clone the repository

bash
git clone https://github.com/MrDupree1/Vocab-Builder1.git
cd Vocab-Builder1
(Optional) Create/activate a virtual environment

bash
python -m venv .venv
# Windows
.venv\Scripts\activate
# macOS/Linux
source .venv/bin/activate
No extra dependencies to install.

▶️ Usage
Run the app:

bash
python main.py
Follow the on-screen menu to:

Add a word & definition

Review your vocabulary list

Take a quiz

Exit

🗂 Data File
The app reads/writes a simple text file named words.txt in the project folder.

If the file doesn’t exist, create an empty words.txt before running, or the app will create/update it when you save words.

Example lines (format can be one word per line or “word – definition”, depending on how you enter them in the app):

plaintext
loquacious – tending to talk a great deal
alacrity – brisk and cheerful readiness
📂 Project Structure
plaintext
Vocab-Builder1/
├── main.py        # Entry point
├── words.txt      # Saved vocabulary data file
├── .gitignore
└── README.md
🤝 Contributing
Pull requests are welcome!

📜 License
This project is open-source and available under the MIT License.
