🔐 Random Password Generator (Python)

A simple Python-based Random Password Generator that creates secure passwords based on user-defined length and character preferences.

✨ Features

Custom password length

Option to include:

Letters (A–Z, a–z)

Numbers (0–9)

Symbols (!@#$%^&*)

Input validation for safe execution

Beginner-friendly and terminal-based

🛠️ Built With

Python 3

Modules: random, string

▶️ How to Run
git clone https://github.com/your-username/random-password-generator.git
cd random-password-generator
python password_generator.py

⚙️ How It Works

User enters password length

User selects character types (letters, numbers, symbols)

Program generates a random password from selected options

Password is displayed in the terminal

🖥️ Sample Output
Enter password length: 10
Include letters (a-z, A-Z)? y
Include numbers (0-9)? y
Include symbols (!@#$)? y

Generated Password:
A7#fQ9@Lx!

📁 Project Structure
random-password-generator/
├── password_generator.py
└── README.md

❗ Validation

Prevents invalid length input

Shows error if no character set is selected
