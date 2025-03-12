def caesar_cipher(shift, plaintext):
    result = ""
    for char in plaintext:
        if char.isalpha():
            ascii_conversion = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - ascii_conversion + shift) % 26 + ascii_conversion)
            result += shifted_char
        else:
            result += char
    
    return(result)
    

def caesar_decipher(shift, ciphertext):
    result = ""
    for char in ciphertext:
        if char.isalpha():
            ascii_conversion = ord('A') if char.isupper() else ord('a')
            shifted_char = chr((ord(char) - ascii_conversion - shift) % 26 + ascii_conversion)
            result += shifted_char
        else:
            result += char
    return result
            

 