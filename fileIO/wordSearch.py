def countWordsinSentence(sentence, word):
    sentenceLst = sentence.split()
    count = 0
    for item in sentenceLst:
        if word == item:
            count += 1
    return count


 