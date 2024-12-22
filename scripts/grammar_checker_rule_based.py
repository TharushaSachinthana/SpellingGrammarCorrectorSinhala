def grammar_checker_rule_based(sentence):
    corrections = []

    # Rule 1: If the sentence has "අපි" as the subject, the verb should end with "මු"
    if "අපි" in sentence:
        words = sentence.split()
        if words[-1].endswith("මු"):
            return ["The sentence is grammatically correct."]
        else:
            corrections.append(
                f"Incorrect verb ending for subject 'අපි'. Replace '{words[-1]}' with a verb ending in 'මු'."
            )

    # Rule 2: If the sentence has "මම" as the subject, the verb should end with "මි"
    if "මම" in sentence:
        words = sentence.split()
        if words[-1].endswith("මි"):
            return ["The sentence is grammatically correct."]
        else:
            corrections.append(
                f"Incorrect verb ending for subject 'මම'. Replace '{words[-1]}' with a verb ending in 'මි'."
            )
    
    # Rule 3: If sentence does not have either "මම" or "අපි" sentence ends with "යි"
    if "මම" not in sentence and "අපි" not in sentence:
        words = sentence.split()
        subject = words[0]
        for word in words:
            if word.endswith("මු"):
                corrections.append(
                    f"Incorrect verb ending for subject {subject}. Replace '{word}' with a verb ending in 'යි'."
                )
            if word.endswith("මි"):
                corrections.append(
                    f"Incorrect verb ending for subject {subject}. Replace '{word}' with a verb ending in 'යි'."
                )

    # Return the corrections or confirm correctness
    if corrections:
        return corrections
    else:
        return ["The sentence is grammatically correct."]
        
