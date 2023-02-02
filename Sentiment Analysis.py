from textblob import TextBlob

def sentiment_analysis(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return "positive"
    elif analysis.sentiment.polarity == 0:
        return "neutral"
    else:
        return "negative"

text = input("Enter a sentence: ")
sentiment = sentiment_analysis(text)
print("The sentiment is:", sentiment)
