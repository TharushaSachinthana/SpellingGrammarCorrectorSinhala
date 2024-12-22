def calculate_accuracy_rule_based(test_sentences, test_labels):
    correct_predictions = 0
    total_sentences = len(test_sentences)
    
    for sentence, true_label in zip(test_sentences, test_labels):
        result = grammar_checker_rule_based(sentence)
        predicted_label = 1 if "grammatically correct" in result[0] else 0
        if predicted_label == true_label:
            correct_predictions += 1
    
    accuracy = correct_predictions / total_sentences
    return accuracy

rule_based_accuracy = calculate_accuracy_rule_based(test_sentences, test_labels)
print(f"Rule-Based Method Accuracy: {rule_based_accuracy * 100:.2f}%")


def calculate_accuracy_linear_regression(model, test_sentences, test_labels):
    correct_predictions = 0
    total_sentences = len(test_sentences)
    
    for sentence, true_label in zip(test_sentences, test_labels):
        features = np.array(sentence_to_features(sentence)).reshape(1, -1)
        prediction = model.predict(features)
        predicted_label = 1 if prediction >= 0.5 else 0
        if predicted_label == true_label:
            correct_predictions += 1
    
    accuracy = correct_predictions / total_sentences
    return accuracy

linear_regression_accuracy = calculate_accuracy_linear_regression(model, test_sentences, test_labels)
print(f"Linear Regression Method Accuracy: {linear_regression_accuracy * 100:.2f}%")
