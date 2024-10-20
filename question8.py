# check if two strings are anagrams

def are_anagrams(s1, s2):

    return sorted(s1. lower()) == sorted(s2. lower())
print(are_anagrams("Listen", "silent"))