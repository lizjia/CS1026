# This program will perform an analysis of keywords or phrases in tweets

import sentiment_analysis

user_file = input('Enter name of file with tweets:')
user_keywords_file = input('Enter file name of file with keywords:')

print(sentiment_analysis.compute_tweets(user_file, user_keywords_file))
