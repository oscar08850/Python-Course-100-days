alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

alphabetShifted = alphabet


def caesar(start_text, shift, direction):
    end_text = ""
    if direction == "decode":
        shift *= -1
    for letter in start_text:
        index = alphabet.index(letter)
        if index >= 25:
            index = (index % 25) - 1
        end_text = end_text + alphabet[index + shift]





def encode(shift, message):
    mensajeEncriptado = ""
    for character in message:
        index = alphabet.index(character)
        if index >= 25:
            index = (index % 25) - 1
        mensajeEncriptado = mensajeEncriptado + alphabet[index + shift]
    print(f"el mensaje encriptado es {mensajeEncriptado}")


def decode(shift, message):
    mensajeEncriptado = ""
    for character in message:
        index = alphabet.index(character)
        print(index - shift)
        mensajeEncriptado = mensajeEncriptado + alphabet[index - shift]
    print(f"el mensaje desencriptado es {mensajeEncriptado}")


if direction.lower() == "encode":
    encode(shift, text)

elif direction.lower() == "decode":
    decode(shift, text)

else:
    print("Error")



    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
    #e.g.
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.