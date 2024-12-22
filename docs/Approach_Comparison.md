# Approach Comparison for Sinhala Spelling and Grammar Correction

This document highlights the different approaches tested for spelling and grammar correction, detailing their pros, cons, and results.

---

## **Spell Checker Approaches**

### **1. Edit Distance-Based**
- **Description**: Uses Levenshtein distance to identify and suggest the closest matches to misspelled words.
- **Advantages**:
  - Works well with small datasets.
  - Simple and interpretable.
- **Disadvantages**:
  - Limited scalability with large datasets.
  - May struggle with context-aware corrections.
- **Performance**:
  - Accurate suggestions for most words in the dataset.

---

### **2. SymSpell**
- **Description**: Uses a hash-based dictionary for fast lookup and spelling correction.
- **Advantages**:
  - Very fast and efficient for large datasets.
  - Easy to integrate.
- **Disadvantages**:
  - Requires extensive pre-built dictionaries for Sinhala.
  - Does not consider contextual information.
- **Performance**:
  - Limited effectiveness for Sinhala due to dictionary constraints.

---

### **3. Pre-Trained Transformer Models**
- **Description**: Utilizes transformer-based models (`Hugging Face`) for context-aware spelling correction.
- **Advantages**:
  - Considers sentence context for better suggestions.
  - State-of-the-art for text-based NLP tasks.
- **Disadvantages**:
  - Computationally expensive.
  - Struggles with out-of-vocabulary words.
- **Performance**:
  - Suggests contextually appropriate replacements but fails with unique Sinhala words.

---

## **Grammar Checker Approaches**
*(To Be Implemented)*

---

## **Performance Comparison**

| Approach                  | Speed        | Accuracy | Context-Aware | Resource Requirement |
|---------------------------|--------------|----------|---------------|-----------------------|
| Edit Distance-Based       | Moderate     | High     | No            | Low                  |
| SymSpell                  | Very Fast    | Low      | No            | Low                  |
| Pre-Trained Transformers  | Moderate     | Moderate | Yes           | High                 |

---

## **Conclusion**
- **Best Approach**: The **Edit Distance-Based** method is the most suitable for this project due to its simplicity, interpretability, and compatibility with smaller datasets.
- **Future Plans**: Explore context-aware grammar correction using pre-trained transformer models.

---

## **References**
1. SymSpell Documentation: [https://github.com/wolfgarbe/SymSpell](https://github.com/wolfgarbe/SymSpell)
2. Hugging Face Transformers: [https://huggingface.co/](https://huggingface.co/)
3. Levenshtein Distance: [Wikipedia](https://en.wikipedia.org/wiki/Levenshtein_distance)
