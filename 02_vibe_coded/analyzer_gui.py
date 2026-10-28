import re
import tkinter as tk
from collections import Counter
from tkinter import filedialog, messagebox, ttk

STOPWORDS = {"a", "an", "and", "are", "as", "at", "be", "by", "for", "from", "in", "is", "it", "of", "on", "or", "that", "the", "to", "was", "were", "with"}


def tokenize(text):
    return re.findall(r"[a-z]+(?:'[a-z]+)?", text.lower())


def analyze():
    words = tokenize(editor.get("1.0", "end-1c"))
    filtered = [word for word in words if not ignore_stopwords.get() or word not in STOPWORDS]
    counts = Counter(filtered)
    for child in table.get_children():
        table.delete(child)
    for word, count in counts.most_common(20):
        table.insert("", "end", values=(word, count))
    status.set(f"Total words: {len(words)}  |  Unique words: {len(set(words))}  |  Displayed: {min(20, len(counts))}")


def open_file():
    path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if not path:
        return
    try:
        with open(path, "r", encoding="utf-8") as file:
            content = file.read()
    except (OSError, UnicodeError) as exc:
        messagebox.showerror("Cannot open file", str(exc))
        return
    editor.delete("1.0", "end")
    editor.insert("1.0", content)
    analyze()


root = tk.Tk()
root.title("Word Frequency Explorer")
root.geometry("680x560")
frame = ttk.Frame(root, padding=16)
frame.pack(fill="both", expand=True)
ttk.Label(frame, text="Word Frequency Explorer", font=("Arial", 18, "bold")).pack(anchor="w")
ttk.Label(frame, text="Paste text or open a .txt file, then analyze it.").pack(anchor="w", pady=(4, 8))
editor = tk.Text(frame, height=12, wrap="word")
editor.pack(fill="both", expand=True)
buttons = ttk.Frame(frame)
buttons.pack(fill="x", pady=10)
ttk.Button(buttons, text="Open text file", command=open_file).pack(side="left")
ttk.Button(buttons, text="Analyze", command=analyze).pack(side="left", padx=8)
ignore_stopwords = tk.BooleanVar(value=False)
ttk.Checkbutton(buttons, text="Ignore common words", variable=ignore_stopwords, command=analyze).pack(side="left")
table = ttk.Treeview(frame, columns=("word", "count"), show="headings", height=8)
table.heading("word", text="Word")
table.heading("count", text="Frequency")
table.column("word", width=360)
table.column("count", width=130, anchor="center")
table.pack(fill="both", expand=True)
status = tk.StringVar(value="Total words: 0  |  Unique words: 0  |  Displayed: 0")
ttk.Label(frame, textvariable=status).pack(anchor="w", pady=(8, 0))
root.mainloop()
