# Password Strength Checker

A beginner-friendly cybersecurity project built with Python that analyzes password strength and generates secure random passwords.

This project was created to practice:
- Python programming
- cybersecurity fundamentals
- password security
- regex validation
- logging systems
- Git & GitHub workflow

---

# Features

## Password Strength Analysis
- Detects weak passwords
- Rates password strength
- Provides security feedback
- Uses regex-based validation

## Password Generator
- Generates secure random passwords
- User-defined password length
- Includes letters, numbers, and symbols

## Security Features
- Password validation
- Strength scoring system
- Error handling
- Logging system with timestamps

## User Interface
- Colored terminal output
- Menu-driven interface
- Beginner-friendly design

---

# Technologies Used

- Python 3
- colorama
- regex (`re`)
- random
- string
- datetime

---

# Project Structure

```text
password-strength-checker/
│
├── main.py
├── README.md
├── requirements.txt
├── .gitignore
├── log.txt
└── screenshots/
```

---

# Installation

## 1. Clone Repository

```bash
git clone https://github.com/kingusecurity/password-strength-checker.git
```

## 2. Navigate Into Project

```bash
cd password-strength-checker
```

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# How To Run

Run the program using:

```bash
python main.py
```

---

# Menu Options

```text
1. Check Password
2. Generate Secure Password
3. Exit
```

---

# Example Usage

## Weak Password Example

Input:

```text
1234
```

Output:

```text
Password Strength: Weak

Suggestions:
- Password should be at least 8 characters
- Add uppercase letters
- Add lowercase letters
- Add special symbols
```

---

## Strong Password Example

Input:

```text
MySecurePass2025!
```

Output:

```text
Password Strength: Strong
```

---

# Password Generator Example

Input:

```text
12
```

Generated Output Example:

```text
xP@9kL#2vQ!
```

---

# Logging System

The tool automatically creates:

```text
log.txt
```

Example log entries:

```text
[2025-08-18 20:10:22] PASSWORD CHECKED: Strong
[2025-08-18 20:11:05] PASSWORD GENERATED: xP@9kL#2vQ!
[2025-08-18 20:12:31] ERROR: Invalid menu choice
```

---

# Cybersecurity Concepts Practiced

- Password security
- Brute-force resistance
- Dictionary attack prevention
- Password entropy
- Input validation
- Authentication security
- Defensive programming

---

# Python Concepts Practiced

- Functions
- Loops
- Conditionals
- Regex
- File handling
- Exception handling
- Random generation
- Modular programming

---

# Future Improvements

Planned upgrades:
- Password entropy calculator
- Common password blacklist
- GUI version using Tkinter
- Clipboard copy support
- HaveIBeenPwned API integration
- Advanced password scoring system

---

# Screenshot

Add screenshots inside:

```text
screenshots/
```

Example:

```markdown
![Tool Screenshot](screenshots/tool.png)
```

---

# Learning Purpose

This project is intended for:
- cybersecurity beginners
- Python beginners
- students building GitHub portfolios
- learning authentication security concepts

---

# Author

GitHub:
https://github.com/kingusecurity

---

# License

This project is open-source and free to use for educational purposes.