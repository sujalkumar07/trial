# find the first occurrence of a substring in a string

def find_substring(s, substring):
    index =s.find(substring)

    return index
print(find_substring("Hello world","world"))