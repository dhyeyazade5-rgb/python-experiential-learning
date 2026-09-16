import tkinter as tk
from tkinter import messagebox
from dictionary import TRANSLATIONS


def translate_text():
    try:
        english_text = input_text.get("1.0", tk.END).strip()

        if not english_text:
            messagebox.showwarning("Empty Input", "Please enter some English text.")
            return

        words = english_text.lower().split()
        translated_words = []

        for word in words:
            clean_word = word.strip(".,!?;:")

            if clean_word in TRANSLATIONS:
                translated_words.append(TRANSLATIONS[clean_word])
            else:
                translated_words.append(clean_word)

        hindi_text = " ".join(translated_words)

        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, hindi_text)

    except Exception as error:
        messagebox.showerror("Error", f"Something went wrong:\n{error}")


def clear_text():
    input_text.delete("1.0", tk.END)
    output_text.delete("1.0", tk.END)


root = tk.Tk()
root.title("English to Hindi Translator")
root.geometry("800x600")
root.resizable(False, False)
root.configure(bg="#f2f2f2")

title = tk.Label(
    root,
    text="English → Hindi Translator",
    font=("Arial", 24, "bold"),
    bg="#f2f2f2"
)
title.pack(pady=20)

english_label = tk.Label(
    root,
    text="Enter English Text",
    font=("Arial", 14, "bold"),
    bg="#f2f2f2"
)
english_label.pack()

input_text = tk.Text(
    root,
    height=8,
    width=80,
    font=("Arial", 13)
)
input_text.pack(pady=10)

translate_button = tk.Button(
    root,
    text="Translate",
    font=("Arial", 13, "bold"),
    command=translate_text,
    padx=30,
    pady=8
)
translate_button.pack(pady=10)

hindi_label = tk.Label(
    root,
    text="Hindi Translation",
    font=("Arial", 14, "bold"),
    bg="#f2f2f2"
)
hindi_label.pack()

output_text = tk.Text(
    root,
    height=8,
    width=80,
    font=("Arial", 13)
)
output_text.pack(pady=10)

clear_button = tk.Button(
    root,
    text="Clear",
    font=("Arial", 12),
    command=clear_text,
    padx=25,
    pady=5
)
clear_button.pack(pady=10)

root.mainloop()
