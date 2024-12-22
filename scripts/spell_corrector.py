import difflib

def spell_checker(word, dictionary):
    """Return suggestions for a misspelled word based on the edit distance."""
    suggestions = difflib.get_close_matches(word, dictionary, n=10, cutoff=0.6)
    return suggestions

if __name__ == "__main__":
    # Example usage
    dictionary_path = "../data/corrected_sinhala_words.csv"
    with open(dictionary_path, "r", encoding="utf-8") as file:
        dictionary = [line.strip() for line in file]

    test_word = "සංයොජන"
    suggestions = spell_checker(test_word, dictionary)
    print(f"Suggestions for '{test_word}': {suggestions}")
