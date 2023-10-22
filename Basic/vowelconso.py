def vc1(alpha):
    
    if alpha in ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']:
        print(alpha, "is vowel.")
    else:
        print(f"{alpha} is consonant.")

def vc2(alpha):
    
    if ord(alpha) in [65, 69, 73, 79, 85, 97, 101, 105, 111, 117]:
        print(alpha, "is vowel.")
    else:
        print(alpha, "is consonant.")
        
def vc3(alpha):
    
    if alpha in [65, 69, 73, 79, 85, 97, 101, 105, 111, 117]:
        print(chr(alpha), "is vowel.")
    else:
        print(chr(alpha), "is consonant.")

if __name__ == "__main__":
    
    alphabet = input("Enter alphabet to check vowel or not : ")
    if alphabet.isalpha():
        vc1(alphabet)
        vc2(alphabet)
    else:
        print("Enter Alphabet")
    
    alphabet = ord(input("Enter alphabet to check vowel or not : "))
    vc3(alphabet)