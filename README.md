# Project Overview

This repository contains tools and resources for building and evaluating a Sinhala language spell checker and grammar checker. The aim is to provide effective tools for detecting and correcting spelling and grammar errors in Sinhala text.

## Directory Structure

```
data/
    corrected_sinhala_words.csv       # Corrected Sinhala words dataset
models/
    spell_checker_model.pkl          # Saved spell checker model
scripts/
    spell_corrector.py               # Spelling correction implementation
    grammar_checker.py               # Grammar checking (to be implemented)
    evaluate.py                      # Evaluation script
notebooks/
    spell_checker_exploration.ipynb  # Jupyter notebook for spelling exploration
    grammar_checker_exploration.ipynb  # (Placeholder for grammar checker)
results/
    spell_checker_comparison_results.csv # Results from evaluation
docs/
    README.md                        # Project overview and instructions
    approach_comparison.md           # Details about spell and grammar checker methods
```

## Getting Started

### Prerequisites
- Python 3.8 or above
- Install dependencies:

```bash
pip install -r requirements.txt
```

### Setup
1. Clone the repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```
2. Prepare the dataset:
   - Place the `corrected_sinhala_words.csv` file in the `data/` directory.

3. Train the spell checker model:
   ```bash
   python scripts/spell_corrector.py --train data/corrected_sinhala_words.csv
   ```

### Usage
- **Spell Checker:**
  ```bash
  python scripts/spell_corrector.py --correct "your text here"
  ```

- **Grammar Checker:** (To be implemented)

### Evaluation
Run the evaluation script to compare the model's performance:
```bash
python scripts/evaluate.py
```
Results will be saved in the `results/` directory.

## Project Files

### `data/`
Contains the dataset of corrected Sinhala words used for training and evaluation.

### `models/`
Stores the trained spell checker model (`spell_checker_model.pkl`).

### `scripts/`
- `spell_corrector.py`: Implements the spell checker functionality.
- `grammar_checker.py`: Placeholder for grammar checking functionality.
- `evaluate.py`: Script for evaluating the performance of the spell checker.

### `notebooks/`
Jupyter notebooks for exploration and experimentation:
- `spell_checker_exploration.ipynb`: Analysis and visualization of the spell checker.
- `grammar_checker_exploration.ipynb`: Placeholder for grammar checker exploration.

### `results/`
Evaluation results, including comparison with other approaches, are saved here.

### `docs/`
- `README.md`: This file.
- `approach_comparison.md`: Detailed documentation on the approaches used for spell and grammar checking.

## Future Work
- Implement and integrate grammar checking.
- Enhance the dataset for better model accuracy.
- Compare with other existing models and approaches.

## Contributing
Contributions are welcome! Please submit a pull request or raise an issue if you have suggestions or improvements.

## License
This project is licensed under the MIT License. See `LICENSE` for details.
