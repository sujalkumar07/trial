# count the numbers of word in a sentence

def count_words(sentence):

    words = sentence.split()

    return len(words)
print(count_words("this is a simple sentence"))
    