import random

def load_words(filepath="words.txt"):
    words = []
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            for line in file:
                if ":" in line:
                    word, definition = line.strip().split(":", 1)
                    words.append((word.strip(), definition.strip()))
    except FileNotFoundError:
        print(f"Error: {filepath} not found.")
    return words

def generate_question(words, num_choices=4):
    correct_word = random.choice(words)
    choices = [correct_word]
    while len(choices) < num_choices:
        candidate = random.choice(words)
        if candidate not in choices:
            choices.append(candidate)
    random.shuffle(choices)
    return correct_word, choices

def run_quiz(words, num_questions=5):
    score = 0
    missed = []

    for _ in range(num_questions):
        correct, options = generate_question(words)
        print(f"\nWhat is the meaning of: '{correct[0]}'?")
        for i, (word, definition) in enumerate(options):
            print(f"{i + 1}. {definition}")

        try:
            answer = int(input("Your choice (1-4): ").strip())
            if options[answer - 1] == correct:
                print("✅ Correct!")
                score += 1
            else:
                print(f"❌ Incorrect. Correct answer: {correct[1]}")
                missed.append(correct)
        except (ValueError, IndexError):
            print("⚠️ Invalid input. Skipping question.")
            missed.append(correct)

    print(f"\nYour Score: {score}/{num_questions}")
    if missed:
        print("\nWords to Review:")
        for word, definition in missed:
            print(f"- {word}: {definition}")

def main():
    print("📘 Welcome to the Vocabulary Builder!")
    words = load_words()
    if not words:
        return

    while True:
        print("\nMenu:\n1. Start Quiz\n2. Exit")
        choice = input("Choose an option: ").strip()
        if choice == "1":
            run_quiz(words)
        elif choice == "2":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select 1 or 2.")

main()
