"""
EDIT: Fixed decode, ty OLL58!
"""

#Make a dictionary called morse code and assign the following values to it
morse_code = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
    '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    '0': '-----', ', ': '--..--', '.': '.-.-.-', '?': '..--..', '/': '-..-.',
    '-': '-....-', '(': '-.--.', ')': '-.--.-'
}

#Create a function called encode_morse that takes a string as a parameter
def encode_morse(string):
    #Create a variable called encoded_string and assign it an empty string
    encoded_string = ""
    #Create a for loop that iterates through the string
    for char in string:
        #If the character is a space, add a space to the encoded_string
        if char == " ":
            encoded_string += " "
        #Otherwise, add the morse code value of the character to the encoded_string
        else:
            encoded_string += morse_code[char.upper()] + " "
    #Return the encoded_string
    return encoded_string

#Create a function called decode_morse that takes a string as a parameter
def decode_morse(string):
    #Create a variable called decoded_string and assign it an empty string
    decoded_string = ""
    #Create a variable called morse_code_values and assign it a list of the morse code values
    morse_code_values = list(morse_code.values())
    #Create a variable called morse_code_keys and assign it a list of the morse code keys
    morse_code_keys = list(morse_code.keys())
    #Create a variable called morse_code_string and assign it an empty string
    morse_code_string = ""
    #Create a for loop that iterates through the string
    for char in string:
        #If the character is a space, add a space to the morse_code_string
        if char == " ":
            if morse_code_string in morse_code_values:
                #Add the key of the morse_code_string to the decoded_string
                decoded_string += morse_code_keys[morse_code_values.index(morse_code_string)]
                #Reset the morse_code_string to an empty string
                morse_code_string = ""
        #Otherwise, add the character to the morse_code_string
        else:
            morse_code_string += char
        #If the morse_code_string is in the morse_code_values list
        
    #Return the decoded_string
    return decoded_string

#Create a function called main that takes no parameters
def main():
    #Create a variable called message and get user input
    message = input("Enter a message to encode: ")
    #Create a variable called encoded_message and assign it the return value of the encode_morse function
    encoded_message = encode_morse(message)
    #Create a variable called decoded_message and assign it the return value of the decode_morse function
    decoded_message = decode_morse(encoded_message)
    #Print that message has been turned into morse code
    print(message, "has been turned into morse code as", encoded_message)
    print(decoded_message)

#Call the main function
main()
