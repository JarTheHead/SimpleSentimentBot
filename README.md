# Sentiment Analysis Bot
This is a Python sentiment analysis bot that takes a string input and outputs whether the string is positive, negative, or neutral. The bot uses the TextBlob library for sentiment analysis. It was mostly generated using ChatGPT.

## How to Run the Bot
To run the script, follow these steps:

1. Clone the repository or download the file sentiment_analysis_bot.py
2. Install the TextBlob library by running pip install textblob in your terminal or command prompt.
3. Run the file by typing python sentiment_analysis_bot.py in your terminal or command prompt.
4. Enter a sentence when prompted and the bot will output the sentiment of the sentence.
5. Repeat the process until you decide to quit by entering **`'q'`**.

## Code Explanation
The code takes the input as a string and analyzes the sentiment using TextBlob. The TextBlob library has a sentiment property that returns a tuple of two values, polarity, and subjectivity. The polarity value ranges between -1 to 1, where -1 represents negative sentiment, 0 represents neutral sentiment, and 1 represents positive sentiment. The code uses an if-else loop to check the polarity value and return the sentiment as positive, negative, or neutral.
