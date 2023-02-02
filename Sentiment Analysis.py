from textblob import TextBlob

def sentiment_analysis(text):
    analysis = TextBlob(text)
    if analysis.sentiment.polarity > 0:
        return "positive"
    elif analysis.sentiment.polarity == 0:
        return "neutral"
    else:
        return "negative"

while True:
    text = input("Enter a sentence (Enter 'q' to quit): ")
    if text == 'q':
        break
    sentiment = sentiment_analysis(text)
    print("The sentiment is:", sentiment)

print("Bye!")
