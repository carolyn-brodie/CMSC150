def countWordsinSentence(sentence, word):
    sentence_list = sentence.split()
    count = 0
    for item in sentence_list:
        if word == item:
            count += 1
    return count


