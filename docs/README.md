### README.md

# Sinhala Spelling and Grammar Corrector

This repository focuses on building a robust system for spelling and grammar correction in the Sinhala language. It includes multiple approaches and evaluations to identify the most accurate methods.

## **Project Features**
- **Spell Checker**:
  - Developed using an Edit Distance-Based approach.
  - Evaluated against models from `SymSpell` and pre-trained transformer-based models (`Hugging Face`).
- **Grammar Checker**:
  - Upcoming feature leveraging rule-based methods and pre-trained language models.

---

## **Repository Structure**
```
data/
    corrected_sinhala_words.csv       # Corrected Sinhala words dataset
models/
    spell_checker_model.pkl          # Saved Edit Distance-Based spell checker model
scripts/
    spell_corrector.py               # Implementation of the spell checker
    grammar_checker.py               # Implementation of the grammar checker (TBD)
    evaluate.py                      # Script for evaluating and comparing approaches
notebooks/
    spell_checker_exploration.ipynb  # Exploration of spell checker methods
    grammar_checker_exploration.ipynb  # Placeholder for grammar checker exploration
results/
    spell_checker_comparison_results.csv # Comparison results for spelling correction
docs/
    approach_comparison.md           # Comparison of methods for spelling and grammar correction
    README.md                        # Project documentation
```

---

## **Installation**

### Prerequisites
- Python 3.8+
- Libraries: `symspellpy`, `transformers`, `numpy`, `pandas`

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/TharushaSachinthana/SpellingGrammarCorrectorSinhala.git
   cd SpellingGrammarCorrectorSinhala
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

## **Usage**

### Spell Checker
Run the script for spelling correction:
```bash
python scripts/spell_corrector.py
```

### Grammar Checker (Coming Soon)
Stay tuned for updates on grammar correction!

---

## **Results**
- **Spell Checker**:
  - **Edit Distance-Based**: High accuracy and flexibility for small datasets.
  - **SymSpell**: Limited accuracy for Sinhala due to lack of large pre-built dictionaries.
  - **Pre-Trained Transformer Models**: Context-aware but less effective for out-of-vocabulary Sinhala words.

Detailed results can be found in [`results/spell_checker_comparison_results.csv`](./results/spell_checker_comparison_results.csv).

---

## **Next Steps**
1. Complete Grammar Checker implementation.
2. Integrate spelling and grammar correction into a unified system.
3. Finalize evaluation and deploy the models as an API or web application.

---

## **Contributions**
Contributions are welcome! Feel free to fork the repository and create pull requests.
