def check_if_alphabet(input_char):
    if len (input_char) == 1 and input_char.isalpha():
        return "The input is an alphabet."
    else:
        return "The input is not an alphabet."
input_value = input("Enter a character: ")
print(check_if_alphabet(input_value))