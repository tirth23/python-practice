"""Text=abc...xyz
   encp=zyx...cba"""

def caesarencrypt(text):
    result = ""
    for ch in text:

        if ch.isupper():
            result += chr(90 - ord(ch) + 65)
        if ch.islower():
            result += chr(122 - ord(ch) + 97)
    return result

if __name__ == "__main__":

    text = input("Enter text for Encryption: ")
    print(f"Encrypted Text: {caesarencrypt(text)}")