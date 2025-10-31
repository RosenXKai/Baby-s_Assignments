
def sentiment(message):
    '''
    Purpose:
        Determines whether text has a positive or negative tone.
    Parameters:
        message (str): The text to analyze 
    Return Value:
        (int) The number of "positive" words in the text minus the
        number of "negative" words.
    '''

    nfile = open('negative_words.txt')
    negative = nfile.read().split()
    nfile.close()
    pfile = open('positive_words.txt')
    positive = pfile.read().split()
    pfile.close()
   # print(negative, positive)

    sentiment_counter = 0

    message.upper()
    for word in message:
        if word in positive:
            sentiment_counter += 1
        elif word in negative:
            sentiment_counter += -1 

    return sentiment_counter



if __name__ == '__main__':
    print(sentiment("Sometimes there are Bad things that Get you in trouble, have a nice day!"))
    print(sentiment("ABANDON, ABANDONED,ABANDONING,ABANDONMENT,ABANDONMENTS"))