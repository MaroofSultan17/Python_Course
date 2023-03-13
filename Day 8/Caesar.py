from Art import logo
print(logo)

def caeser(user_text, shift_amount, direction):
    output = ""
    if direction == "encode":
        for letter in user_text:
            if letter in alphabet: 
                position = alphabet.index(letter)
                new_position = position + shift_amount
                output += alphabet[new_position]
            else:
                output += letter
    elif direction == "decode":
        for letter in user_text:
            if letter in alphabet:
                position = alphabet.index(letter)
                new_position = position - shift_amount
                output += alphabet[new_position]
            else:
                output += letter
    return output


should_continue = True
while should_continue:
    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    direction = input("Type 'encode' to encrypt and Type 'decrypt' to decode your message\n")
    text = input("Type your Message \n").lower()
    shift = int(input("Type the shift number \n"))
    # for lage index like 77 we use modulous
    shift = shift % 26
    print(f"Anser is {caeser(text, shift, direction)}")
    decision = input("If you want to Continue then type 'Yes' or if you want to quit then type 'No'").lower()
    if decision == 'yes':
        should_continue = True
    elif decision == 'no':
        print("Good Bye")
        should_continue = False