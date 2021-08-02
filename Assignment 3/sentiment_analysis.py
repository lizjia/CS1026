# Function determines the happiness score of a tweet.
def happiness_score_tweets(tweet, keywords):
    sentiment_value = 0
    num_keywords = 0
    for word in tweet:
        for key, value in keywords.items():
            if word == key:
                num_keywords += 1
                sentiment_value += int(value)
    if num_keywords != 0:
        happiness_score = sentiment_value / num_keywords
        return happiness_score

# Function determines the region of tweets
def tweet_region(latitude, longitude):
    region = ''
    if latitude <= 49.189787 and latitude >= 24.660845:
        if longitude <= -67.444574 and longitude > -87.518395:
            region = 'Eastern'
        elif longitude <= -87.518395 and longitude > -101.998892:
            region = 'Central'
        elif longitude <= -101.998892 and longitude > -115.236428:
            region = 'Mountain'
        elif longitude <= -115.236428 and longitude >= -125.242264:
            region = 'Pacific'
        else:
            region = 'skip'
    else:
        region = 'skip'

    return region

# Function finds the average happiness value of a region and the number of tweets and keyword tweets from that respective region.
def compute_tweets(fileName, fileKeywords):
    try:
        # Files are opened and it returns a list of strings in which each tweet is a string with its corresponding region, date, time, and sentiment value
        t_file = open(fileName,"r",encoding="utf-8")
        tweet_file = t_file.readlines()
        k_file = open(fileKeywords,"r",encoding="utf-8")
        keyword_file = k_file.readlines()

        # Empty lists and dictionaries are created to append values that are to be calculated
        list_lines = []
        list_timezone = []
        dict_keywords = {}
        dict_region_happiness = {'Eastern': 0, 'Central': 0, 'Mountain': 0, 'Pacific': 0}
        dict_tweet_count = {'Eastern': 0, 'Central': 0, 'Mountain': 0, 'Pacific': 0}
        dict_tweet_keyword_count = {'Eastern': 0, 'Central': 0, 'Mountain': 0, 'Pacific': 0}
        compute_tweet_tuple = ()
        list_compute_tweets = []

        # The keyword file is sorted into a dictionary; dict_key.
        for line in keyword_file:
            line = line.split(',')
            line[1] = line[1].replace('\n', '')
            dict_keywords[line[0]] = line[1]

        # Each line by whitespace and then put into list
        for line in tweet_file:
            line = line.lower()
            line_list = []
            line = line.split()
            for item in line:
                line_list.append(item)
            list_lines.append(line_list)

        # The value, date, and time from each list is removed from the tweet file.
        for item in list_lines:
            item.pop(2)
            item.pop(2)
            item.pop(2)

        # All punctuation is removed from the tweet and the region of the tweet is determined
            latitude = item[0].replace('[', '')
            latitude = latitude.replace(',', '')
            longitude = item[1].replace(']', '')
            for index, char in enumerate(item):
                if char[0] in ',.!?()^&*+=;:@#$%-()\'\"':
                    item[index] = char.replace(char[0], '')
                if char[-1] in ',.!?()^&*+=;:@#$%-()\'\"':
                    item[index] = char.replace(char[-1], '')
            timezone = tweet_region(float(latitude), float(longitude))

        # Excluded timezones are determined
            if timezone != 'skip':
                dict_tweet_count[timezone] += 1
                score = happiness_score_tweets(item, dict_keywords)
                if score is not None:
                    dict_region_happiness[timezone] += score
                    dict_tweet_keyword_count[timezone] += 1

        # A tuple with the average happiness value, the number of keyword tweets, and the total number of tweets is created
        for area in dict_tweet_count:
            if dict_tweet_keyword_count[area] != 0:
                average = dict_region_happiness[area]/dict_tweet_keyword_count[area]
            else:
                average = 0
            tuple_region = (average, dict_tweet_keyword_count[area], dict_tweet_count[area])
            list_compute_tweets.append(tuple_region)

        return list_compute_tweets

    # if the file is not found, an empty list is returned
    except FileNotFoundError:
        return []
