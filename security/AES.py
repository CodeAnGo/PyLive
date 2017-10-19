from Crypto.Cipher import AES
from Crypto import Random
import textwrap


'''Takes in Text, a Optional Mode and an Optional IV
Modes Allowed:
"FAKE" = Fake Encryption (No-Encryption) (ONLY USE FOR DEVELOPMENT)
"CBC" = Cipher Block Chaining Encryption (AES-CBC) (Default)

If an IV is not supplied, it will generate one.
If a Key is not supplied, it will generate one.

Output = Array[String Encrypted Text, String Key, String IV, String Method Used]'''
def encryptBlockText(text, mode="CBC", key=Random.new().read(32), iv=Random.new().read(16)):
    if mode == "FAKE":
        text = text[::-1]
    elif mode == "CBC":
        encryptionObject = AES.new(key, AES.MODE_CBC, iv)
        blocks = packBlockText(text, 16)
        encryptedText = ""
        for block in blocks:
            encryptedText += encryptionObject.encrypt(block)
        text = encryptedText
    else:
        text = text, iv
    return [str(text), str(key), str(iv), str(mode)]

def decryptBlockText(text, mode="CBC", key=Random.new().read(32), iv=Random.new().read(16)):
    if mode == "FAKE":
        text = text[::-1]
    elif mode == "CBC":
        encryptionObject = AES.new(key, AES.MODE_CBC, iv)
        decryptedText = encryptionObject.decrypt(text)
        text = removeTrailBuffer(decryptedText)
    else:
        text = text, iv
    return str(text)

'''Methods such as CBC require 16 bit blocks, this ensures that this is the case'''
def packBlockText(text, blockSize):
    text = text.replace(" ", "#")
    parts = textwrap.wrap(text, blockSize)
    for index, part in enumerate(parts):
        if "#" in part:
            parts[index] = part.replace("#", " ")
        if not len(part) == blockSize:
            while len(part) != blockSize:
                part = part + " "
            parts[index] = part
    return parts

def removeTrailBuffer(text):
    return text.rstrip(" ")