#convert a string to uppercase and lowercase

def convert_case(s):
    upper_case = s.upper()

    lower_case =s.lower()

    return upper_case, lower_case
print(convert_case("hello world"))