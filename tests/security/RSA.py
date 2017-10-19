import unittest
import os
from security import RSA

class RSATest(unittest.TestCase):
    def testRSA4096Encryption(self):
        print("Testing RSA-4096 Encryption")
        inputText = "This is an example input string that should be encrypted, then decrypted!"
        keys = RSA.generateRSAKey()
        encryptedText = RSA.keyExchangeEncrypt(inputText, keys[2])
        decryptedText = RSA.keyExchangeDecrypt(encryptedText, keys[1])
        self.assertEqual(inputText, decryptedText)

    def testRSA2048Encryption(self):
        print("Testing RSA-2048 Encryption")
        inputText = "This is an example input string that should be encrypted, then decrypted!"
        keys = RSA.generateRSAKey(2048)
        encryptedText = RSA.keyExchangeEncrypt(inputText, keys[2])
        decryptedText = RSA.keyExchangeDecrypt(encryptedText, keys[1])
        self.assertEqual(inputText, decryptedText)

    def testRSA1024Encryption(self):
        print("Testing RSA-1024 Encryption")
        inputText = "This is an example input string that should be encrypted, then decrypted!"
        keys = RSA.generateRSAKey(1024)
        encryptedText = RSA.keyExchangeEncrypt(inputText, keys[2])
        decryptedText = RSA.keyExchangeDecrypt(encryptedText, keys[1])
        self.assertEqual(inputText, decryptedText)
