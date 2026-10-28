# Three approaches to one application: Word Frequency Analyzer

All three implementations solve the same core task, counting words, while differing in architecture and features.

## 1. By hand (beginner-level design)
`python3 01_by_hand/analyzer.py`

- Single script, terminal input, `split()`, dictionary, `for` loops, simple punctuation removal.
- No dependencies.
- Deliberate limitations: no files, GUI, CSV or dedicated functions; punctuation within words is not handled as cleanly.

## 2. Vibe coded (AI-led feature generation)
`python3 02_vibe_coded/analyzer_gui.py`

- Tkinter GUI, text file opening, frequency table, stopword toggle.
- Requires Python with Tkinter available. On some macOS installations, Tkinter requires an additional installation.
- No external Python libraries.

## 3. Hybrid (human-guided AI iteration)
`python3 03_hybrid/analyzer.py`

- Terminal UI retains understandable structure, now organized into functions.
- Regex tokenization, top-ten display, text file input, optional CSV export, and unit tests.

