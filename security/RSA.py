from Crypto.PublicKey import RSA
from Crypto import Random

def generateRSAKey(keySize=4096):
    key = RSA.generate(keySize)
    return [key, key.exportKey("DER"), key.publickey().exportKey("DER")]

def keyExchangeEncrypt(text, publicKey):
    encryptionObject = RSA.importKey(publicKey)
    return encryptionObject.encrypt(text, 'x')[0]

def keyExchangeDecrypt(text, privateKey):
    encryptionObject = RSA.importKey(privateKey)
    return encryptionObject.decrypt(text)
