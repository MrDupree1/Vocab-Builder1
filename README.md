# 📚 Vocab Builder

A beginner-friendly Python app to help you **build and practice your vocabulary**. Save words, quiz yourself, and track your progress — now with both a **text version (CLI)** and a **simple GUI** for easier use.

---

## 🚀 Features  
- **Add and store words** with definitions in a simple text file (`words.txt`)  
- **Quiz mode**: Type the word when given the definition, with a **Reset** option  
- **GUI mode** for a user-friendly experience  
- **Load external packs** from `.txt` files for quick bulk imports  
- Runs on **Windows, macOS, and Linux** with **no extra installs** (Python standard library only)

---

## 🛠️ Technologies Used  
- Python **3.x**  
- `tkinter` for the GUI (built-in, no extra packages)  
- Standard library only — **no dependencies**

---

## ⚡ Quick Start  

### 1️⃣ Clone the Repository  
```bash
git clone https://github.com/MrDupree1/Vocab-Builder1.git
cd Vocab-Builder1

2️⃣ Run the Text Version (CLI)
python main.py

3️⃣ Run the GUI Version
python gui.py

📄 Installation
Optional: Create a Virtual Environment

Windows

python -m venv venv
venv\Scripts\activate


macOS/Linux

python3 -m venv venv
source venv/bin/activate

▶️ Usage
CLI Menu Options

Review words

Take a quiz

Add a word (quick)

Exit

GUI Options

Review your saved words

Take a quiz with a Reset option

Load .txt packs for more words

📂 File Structure
Vocab-Builder1/
├── main.py         # CLI version
├── gui.py          # GUI version
├── words.txt       # Local storage file for saved words
├── packs/          # Optional folder for external word packs
├── .gitignore
└── README.md

🗂 Data File

Words are stored in words.txt automatically.

Supports simple formats like:

loquacious - tending to talk a great deal
alacrity - brisk and cheerful readiness

🤝 Contributing

Pull requests are welcome! Fork the repo, make your changes, and submit a PR.

📜 License

This project is open-source and available under the MIT License.
