
def pegasus():
    print("\n*******************************************************************"+
          "\nWe are team PEGASUS, commissioned by Aniket, Austin, and Chandra." +
          "\nYour goal is to decrypt this message, and find what the secret is.")

    original_message = "This is a top-secret message"
    encrypted_message = "Uijt jt b upq-tfdsfu nfttbhf"

    print("\n\nThis is the encrypted message: " + encrypted_message)

    decrypted_message = input("\n\nDecrypt this message. [Caesar Cipher] -> ")

    if decrypted_message == original_message:
        print("Correct!"+
              "\n*******************************************************************")
    else:
        print("Hmm, something is wrong. Please check your answer..." +
              "\n*******************************************************************")



