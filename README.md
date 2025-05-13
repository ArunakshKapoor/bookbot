# 📚 BookBot

**BookBot** is a simple Python program that analyzes a book in `.txt` format and prints out useful statistics like word count and the frequency of each character. This project was built as part of the [Boot.dev](https://boot.dev) Backend Development learning path to practice key backend programming concepts.

---

## 🚀 What It Does

Given a `.txt` file (e.g., `books/frankenstein.txt`), BookBot:

- Counts the total number of words in the book.
- Calculates the frequency of each alphabetic character (case-insensitive).
- Displays the results in a clean, readable format.

Example output:
--- Begin report of books/frankenstein.txt ---
34241 words found in the document
The 'e' character was found 2345 times
The 't' character was found 1982 times
...
--- End report ---


---

## 🧠 Skills Practiced

- File I/O with Python
- String and text processing
- Using dictionaries for frequency counting
- Writing clean, modular functions
- Console output formatting

---

## 🏗️ Project Structure
```
bookbot/
├── main.py           # Main script that runs the analysis
├── books/
│   └── frankenstein.txt  # Sample input text (public domain)
├── README.md         # Project documentation
```

---

## 🛠️ How to Run It

1. Clone the repository:
```bash
git clone https://github.com/ArunakshKapoor/bookbot.git
cd bookbot
```

2. Make sure you have Python installed (python3 --version).

3. Run the script:
```
python3 main.py
```
The script will analyze books/frankenstein.txt and print the report to the terminal.

## Requirements
Python 3.6 or higher

No external libraries required — uses only the Python standard library

## Book Source
The sample book (frankenstein.txt) is sourced from Project Gutenberg, which provides free access to works in the public domain.

## Notes
You can replace frankenstein.txt with any other .txt file — just place it in the books/ folder and update the path in main.py accordingly.

This project is intentionally simple and is focused on building comfort with basic backend concepts.

## License
This project is open-source and available under the MIT License.

---

Let me know if you’d like to include badges, contribution guidelines, or extend it with sorting features or word frequency analysis!
