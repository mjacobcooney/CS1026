from string import digits
from string import punctuation

#this function adds the happiness score of the tweet(average) to the running total for that timezone(n). Also increments
#the count for happy tweets if it is a keyword tweet
def scoreHelper(average, totalScores, happyTweets, totalTweets, n):
    if average > 0:
        sum = totalScores[n]
        sum += average
        totalScores[n] = sum
        happyTweets[n] += 1
        totalTweets[n] += 1
    else:
        totalTweets[n] += 1

def compute_tweets(tweetsFile, keywordsFile):
    word = ""
    score = 0
    result = []
    dict = {word: score}
    happyTweets = [0, 0, 0, 0]
    totalTweets = [0, 0, 0, 0]
    totalScores = [0, 0, 0, 0]
    try:
        tweetsFile = open(tweetsFile, encoding='utf‐8', errors='ignore')
        keywordsFile = open(keywordsFile, encoding='utf‐8', errors='ignore')
        line = tweetsFile.readline()
    except IOError:
        print("Error: file not found.")
        return result
    except ValueError as exception:
        print("Error:", str(exception))
        return result
    #populate dict with key: score
    for line in keywordsFile:
        keylist = line.split(",")
        dict[keylist[0]] = keylist[1]
    # first need to go through all the tweets.txt and create Tweet objects and store in list
    for line in tweetsFile:
        # separate coordinate  into a variable
        count = 0
        score = 0
        average = 0
        line = line.rstrip()
        coordinateList = line.split("]")
        coordinate = coordinateList[0] = line.split(",")
        removeChars = "[ ,"
        coordinateLat = float(coordinate[0].lstrip(removeChars))
        coordinateLong = coordinate[1].split("]")
        coordinateLong = float(coordinateLong[0].lstrip(removeChars))
        tweetText = coordinateList[1][23:]
        #check if coordinates are within specification
        if (24.660845 <= coordinateLat <= 49.189787) and (67.444574 <= abs(coordinateLong) <= 125.242264):
            words = tweetText.split()
            #this for loop calculates the score for the tweet using the dict we populated earlier
            for word in words:
                word = word.strip(punctuation)
                if word.lower() in dict:
                    score += int(dict[word.lower()])
                    count += 1
            if count > 0:
                average = float(score / count)
            if abs(coordinateLong) < 87.518395:  # eastern
                scoreHelper(average, totalScores, happyTweets, totalTweets, 0)
            elif 87.518395 <= abs(coordinateLong) < 101.998892:  # central
                scoreHelper(average, totalScores, happyTweets, totalTweets, 1)
            elif 101.998892 <= abs(coordinateLong) < 115.236428:  # mountain
                scoreHelper(average, totalScores, happyTweets, totalTweets, 2)
            elif 115.236428 <= abs(coordinateLong) < 125.242264:  # Pacific
                scoreHelper(average, totalScores, happyTweets, totalTweets, 3)

    averages = [0, 0, 0, 0]
    #only calculate average is count > 0
    for i in range(0,4):
        if happyTweets[i] > 0:
            averages[i] = float(totalScores[i] / happyTweets[i])
        else:
            averages[i] = 0
            
    eastern = (averages[0], happyTweets[0], totalTweets[0])
    central = (averages[1], happyTweets[1], totalTweets[1])
    mountain = (averages[2], happyTweets[2], totalTweets[2])
    pacific = (averages[3], happyTweets[3], totalTweets[3])
    result = [eastern, central, mountain, pacific]
    return result
