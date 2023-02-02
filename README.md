# Sentiment Analysis Bot
This is a simple sentiment analysis bot that takes a string input and outputs whether the string is positive, negative, or neutral. The sentiment analysis is done using the TextBlob library in Python.

## Prerequisites
Before you run the script, make sure that you have the following installed:

## Python 3.x
TextBlob library (can be installed using pip install textblob)
How to Run the Script
To run the script, follow these steps:

## Open your terminal or command prompt.
Navigate to the directory where the script is saved.
Type python SentimentAnalysis.py and press enter.
The script will prompt you to enter a sentence. Type in your sentence and press enter.
The sentiment analysis result will be displayed as either "positive", "neutral", or "negative".
Code Explanation
The code imports the TextBlob library and defines a function named sentiment_analysis that takes a string input and returns the sentiment as "positive", "neutral", or "negative".

The TextBlob library is used to analyze the sentiment of the input text. The sentiment property of the TextBlob object returns a tuple of two values: polarity and subjectivity. The polarity value ranges between -1 to 1, where -1 represents negative sentiment, 0 represents neutral sentiment, and 1 represents positive sentiment.

An if-else loop is used to check the polarity value and return the sentiment as "positive", "neutral", or "negative".

Finally, the script takes user input and calls the sentiment_analysis function to display the sentiment analysis result.
