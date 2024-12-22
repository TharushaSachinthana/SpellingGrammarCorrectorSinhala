import numpy as np
from sklearn.linear_model import LinearRegression

# Step 1: Prepare the dataset
# Example sentences and their grammatical correctness (1 = correct, 0 = incorrect)
sentences = [
    "මම ගීතයක් ගයමි",
    "මම බුඳුන් වදිමි",
    "මම බසයෙන් යයි",
    "මා කවියක් ලියමි",
    "අපි චාරිකාවක් යමු",
    "අපි ආහාර පිසිමු",
    "අප නගරයට යමු",
    "අපි නිවසට යති",
    "ගස සුලඟට වැනෙමි",
    "හිරු නැගෙනහිරින් නැග එයි",
    "මිනිසා රැකියාවට යයි"
]

labels = [1, 1, 0, 0, 1, 1, 0, 0, 0, 1, 1]  # 1 = Correct, 0 = Incorrect

# Step 2: Feature Engineering
def sentence_to_features(sentence):
    features = []
    # Subject features
    features.append(1 if "මම" in sentence else 0)  # "මම" presence
    features.append(1 if "අපි" in sentence else 0)  # "අපි" presence
    
    # Verb ending features
    verb = sentence.split()[-1]  # Get the last word (verb)
    features.append(1 if verb.endswith("මි") else 0)  # Ends with "මි"
    features.append(1 if verb.endswith("මු") else 0)  # Ends with "මු"
    features.append(1 if verb.endswith("යි") else 0)  # Ends with "යි"
    
    return features

# Transform sentences into features
X = np.array([sentence_to_features(sentence) for sentence in sentences])
y = np.array(labels)

# Step 3: Train the model
model = LinearRegression()
model.fit(X, y)

# Step 4: Grammar Checker
def grammar_checker_linear_regression(sentence):
    features = np.array(sentence_to_features(sentence)).reshape(1, -1)
    prediction = model.predict(features)
    
    if prediction >= 0.5:
        return "The sentence is grammatically correct."
    else:
        # Suggest corrections based on rules
        corrections = []
        if "මම" in sentence and sentence.split()[-1].endswith("මු"):
            corrections.append("Replace the verb with one ending in 'මි'.")
        elif "අපි" in sentence and sentence.split()[-1].endswith("මි"):
            corrections.append("Replace the verb with one ending in 'මු'.")
        elif "මම" not in sentence and "අපි" not in sentence:
            corrections.append("Replace the verb with one ending in 'යි'.")
        return corrections if corrections else "The sentence is grammatically incorrect, but no specific suggestion is available."