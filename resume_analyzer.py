"""
Basic Resume Analyzer  by Baasim Ahmed
This script takes a resume from the user and shows the top 10 used words.
by taking the most used words, it determines whether the candidate is reputable for the job.
The example job used in this project is a Data Science job.
"""

import re

# Function 1 - gets the resume
def get_resume():
    resume_text = ""

    # Prompt the user to enter a resume
    print('Paste your resume below. Once you are finished, type DONE (Case Sensitive)\n')

    # Collect multi-line input until the user exits
    while True:
        line = input()
        if line.strip() == "DONE":
            break
        resume_text += line + " "
    return resume_text


# Function 2 - Converts the resume to lowercase, Removes Punctuation,
# and splits into individual words.
def convert_resume(text):
    text = text.lower()

    # Preserve common programming terms before removing punctuation
    text = text.replace("c++", "cplusplus")
    text = text.replace("c#", "csharp")
    text = text.replace("r&d", "researchanddevelopment")
    text = text.replace("f#", "fsharp")
    text = text.replace(".net", "dotnet")

    # Remove all punctuation using regex
    text = re.sub(r"[^\w\s]", "", text)
    return text.split()

# Function 3 - Counts how many times each word was used and filters filler words
def word_counter(word_list):

    # list that will stop common filler words from appearing in key used words dictionary
    stopwords = {
        "the", "and", "is", "to", "a", "in", "of", "for", "on", "with", "as", "by",
        "this", "that", "at", "an", "be", "are", "was", "were", "from", "or", "it", "i"
    }

    word_counts = {}

    # Loop to count how many times each word appears
    for word in word_list:
        if word in stopwords:
            continue
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1
    return word_counts

# Function 4 - Makes sure the dictionary is sorted by value, highest first
def sort_dict(word_counts):
    sorted_word_counts = sorted(word_counts.items(), key=lambda x: x[1], reverse=True)

    # Print the top 10 most common words
    print("10 commonly used words")
    print(f"{'Word':<15} {'Count'}")
    print("-" * 20)
    for word, count in sorted_word_counts[:10]:
        print(f"{word:<15} {count}")

# Function 5 - Evaluates the fit of the candidate (based on the resume) for the job,
# also determines if the resume is missing essential skills
def evaluate_fit(word_list, required_keywords):
    missing = []

    # Loop to add the missing words into the list above
    for keyword in required_keywords:
        if keyword not in word_list:
            missing.append(keyword)

    # Calculate percentage match
    match_score = ((len(required_keywords) - len(missing)) / len(required_keywords)) * 100
    print(f"Resume match score: {round(match_score)}%")

    # Tell the user which keywords are missing, or none if none are missing.
    if len(missing) == 0:
        print("\nResume meets criteria of required skills!")
    elif len(missing) <= 2:
        print("\nResume meets some criteria, but is missing:", ", ".join(missing))
    else:
        print("\nResume is missing too many required skills:", ", ".join(missing))


# Main function
def main():
    resume_text = get_resume()
    word_list = convert_resume(resume_text)
    word_count = word_counter(word_list)
    sort_dict(word_count)
    required_keywords = ["python", "scikitlearn", "pandas", "numpy", "matplotlib",
                         "statsmodels", "tensorflow", "r", "sql", "bash" ]
    evaluate_fit(word_list, required_keywords)

if __name__ == '__main__':
    main()