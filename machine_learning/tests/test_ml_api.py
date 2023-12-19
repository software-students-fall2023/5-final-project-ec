from textblob import TextBlob


def analyze_feedback(feedback_text):
    # Analyze sentiment using TextBlob
    analysis = TextBlob(feedback_text)
    sentiment_polarity = analysis.sentiment.polarity
    return sentiment_polarity

def test_ml_api():
    assert analyze_feedback("Good job!")>0
    assert analyze_feedback("Bad job!")<0
    

if __name__ == "__main__":
    test_ml_api()
