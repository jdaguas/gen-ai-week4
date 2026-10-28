import re
from collections import Counter


def count_words(text):
    """Return normalized word counts, including contractions."""
    words = re.findall(r"[a-z]+(?:'[a-z]+)?", text.lower())
    return Counter(words)


def print_top_words(counts, limit=10):
    print(f"\nTotal words: {sum(counts.values())}")
    print(f"Unique words: {len(counts)}")
    print(f"\nTop {limit} words:")
    for word, frequency in counts.most_common(limit):
        print(f"{word:<20} {frequency}")


def export_csv(counts, path):
    with open(path, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["word", "frequency"])
        writer.writerows(counts.most_common())


def main():
    print("Word Frequency Analyzer (Hybrid)")
    choice = input("Analyze (1) typed text or (2) a .txt file? [1/2]: ").strip()
    if choice == "1":
        text = input("Enter your text: ")
    elif choice == "2":
        path = input("Text file path: ").strip()
        try:
            with open(path, "r", encoding="utf-8") as file:
                text = file.read()
        except (OSError, UnicodeError) as exc:
            print("Could not read the file:", exc)
            return
    else:
        print("Invalid choice.")
        return

    counts = count_words(text)
    print_top_words(counts)
    if input("Export results to a CSV file? [y/N]: ").strip().lower() == "y":
        path = input("Output filename [frequency.csv]: ").strip() or "frequency.csv"
        try:
            export_csv(counts, path)
            print("Saved results to", path)
        except OSError as exc:
            print("Could not write CSV:", exc)


if __name__ == "__main__":
    main()
