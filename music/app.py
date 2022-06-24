def getSentiment(text):
    """
    This function takes in a string of text and returns the sentiment of the text.
    """
    # Import the necessary modules
    import nltk
    from nltk.sentiment.vader import SentimentIntensityAnalyzer
    # Create a SentimentIntensityAnalyzer object
    sid = SentimentIntensityAnalyzer()
    # Get the sentiment of the text
    sentiment = sid.polarity_scores(text)
    # Return the sentiment
    return sentiment
sentence = "This is a great movie"
print(getSentiment(sentence))