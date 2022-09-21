alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

alphabetShifted = alphabet

def encode(shift, message):
    mensajeEncriptado = ""
    for character in message:
        index = message.index(character)
        mensajeEncriptado = mensajeEncriptado + alphabet[index + shift]
    print(mensajeEncriptado)



index = alphabet.index("z")
print(index % 25)





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