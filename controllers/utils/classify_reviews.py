from controllers.utils.ClassificationModule import ClassificationModule

# Create an instance of the ClassificationModule
classification_module = ClassificationModule()


async def classify_reviews(reviews):
    # Predict the sentiment of the input texts
    predictions = classification_module.predict_sentiment(reviews)

    # class_labels = ["Negative", "Neutral", "Positive"]

    classified_reviews = {
        "Negative": [],
        "Neutral": [],
        "Positive": []
    }

    # Convert indices to labels
    def interpret_predictions(predictions):
        for review, prediction in zip(reviews, predictions):
            if prediction == 0:
                classified_reviews["Negative"].append(review)
            elif prediction == 1:
                classified_reviews["Neutral"].append(review)
            else:
                classified_reviews["Positive"].append(review)
    
    interpret_predictions(predictions)
    print(classified_reviews)
    
    return classified_reviews