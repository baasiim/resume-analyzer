# Resume Analyzer

A simple Python script that analyzes the most used words in a resume and evaluates how well it matches a Data Science job description.

## Features

- Cleans and tokenizes resume text
- Removes filler/stopwords
- Preserves programming keywords (e.g., `C++`, `R&D`, `.NET`)
- Counts and ranks word frequency
- Evaluates resume against key skills like Python, SQL, Pandas, etc.
- Provides a match score and highlights missing skills

## Skills Evaluated

This project simulates a resume screener for Data Science roles. It checks typical skills for a Data Science job.

## How to Use

1. Clone or download this repo
2. Open a terminal and run `resume_analyzer.py`
3. Paste your resume text into the terminal
4. Type `DONE` (case-sensitive) on a new line to finish input
5. Review the top keywords, match score, and suggested improvements

## Sample Output

```
10 commonly used words
Word            Count
----------------------
python          4
sql             2
data            2

Resume Match Score: 70%
Resume is missing too many required skills: tensorflow, statsmodels, bash
```

## Future Improvements

- Smarter context-aware keyword detection (not just word count)
- PDF upload support
- Job selector for different tech roles (ML Engineer, Web Developer, etc.)
- Optional GUI with drag-and-drop resume upload

---

Built by Baasim Ahmed
