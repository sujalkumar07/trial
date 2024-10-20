# capitalize the first letter of each word(title case)

def title_case(sentence):
    words=sentence.split()

    capitalized_words = [word.capitalize() for word in words]

    return ' '.join(capitalized_words) 

print(title_case("hello world"))