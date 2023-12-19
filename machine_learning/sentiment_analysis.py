from textblob import TextBlob



def analyze_feedback(feedback_text):
    # Analyze sentiment using TextBlob
    analysis = TextBlob(feedback_text)
    sentiment_polarity = analysis.sentiment.polarity
    return sentiment_polarity