

def pegasus():

    level_system = True
    print("\n*******************************************************************" +
          "\nWe are team PEGASUS, commissioned by Aniket, Austin, and Chandra." +
          "\nYour goal is to decrypt this message, and find what the secret is.")

    def new_level( original_message ):

        encrypted_message = to_encrypt(original_message, 5) # encrypting original

        print("\n\nThis is the encrypted message: " + encrypted_message)

        decrypted_message = input("\n\nDecrypt this message. [Caesar Cipher]\n-> ")

        if decrypted_message == original_message:
            print("Correct! Level passed" +
                  "\n*******************************************************************")

        else:
            print("Hmm, something is wrong. Try again." +
                  "\n*******************************************************************")
            new_level(original_message)

    def to_encrypt(original_message, s):
        result = ""
        # transverse the plain text
        for i in range(len(original_message)):
            char = original_message[i]
            # Encrypt uppercase characters in plain text

            if (char.isupper() == True):
                result += chr((ord(char) + s - 65) % 26 + 65)
            # Encrypt lowercase characters in plain text
            elif char == " ": # if space add one
                result += " "
            elif char == "-": # if hyphen leave it
                result += "-"
            else: # for all other characters
                result += chr((ord(char) + s - 97) % 26 + 97)

        return result

    new_level("This is a top-secret message") # level One
    new_level("Rendez-vous at 1224 E Street") # level Two
    new_level("s e c r e t s    e x i s t")  # level Three
    new_level("rhombicosidodecahedron")    # level Four
    new_level("pneumonoultramicroscopicsilicovolcanoconiosis") # level Five

    print(
          "\n*******************************************************************" +
          "\n****************************** DONE *******************************" +
          "\n*******************************************************************"
    )