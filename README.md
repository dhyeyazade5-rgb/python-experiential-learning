A Python-based English-to-Hindi Translator with a simple Tkinter GUI. Users can enter English words or sentences and receive Hindi translations using a predefined dictionary.

Features

English text input

Hindi translation output

Simple Tkinter graphical interface

Predefined English-Hindi dictionary

String manipulation

Exception handling

Clear button

No internet or API key required

Technologies

Python 3

Tkinter

Python Dictionary

String Manipulation

Exception Handling

Project Structure

English-Hindi-Translator/
├── translator.py
├── dictionary.py
└── README.md

Requirements

Python 3.x

Tkinter (normally included with Python)

How to Run

Open the project folder in VS Code.

Open the terminal.

Run:

python translator.py

If required, use:

python3 translator.py

How It Works

English Input
     ↓
Split into Words
     ↓
Search Translation Dictionary
     ↓
Convert English Words to Hindi
     ↓
Display Hindi Translation

Example

Input:

hello my name is Saksham

Output:

नमस्ते मेरा नाम है Saksham

Python Concepts Demonstrated

Dictionary: Stores English-Hindi word mappings.

Functions: Handles translation and clearing.

Loops: Processes each input word.

Conditional statements: Checks dictionary entries.

String manipulation: Uses lower(), split(), strip(), and join().

Exception handling: Uses try-except.

GUI programming: Uses Tkinter widgets.

Limitations

This version uses a predefined dictionary, so words that are not in the dictionary may remain unchanged. It does not perform context-aware grammatical translation.

Future Improvements

Integrate an online translation API

Translate complete paragraphs more accurately

Add Hindi-to-English translation

Add voice input

Add text-to-speech

Add translation history

Support multiple languages

Improve the GUI design

Objective

The objective of this project is to demonstrate practical Python programming through a simple language translation application while applying dictionaries, string processing, GUI development, and exception handling.

Author

Saksham Yerawar

License

This project is created for educational purposes
