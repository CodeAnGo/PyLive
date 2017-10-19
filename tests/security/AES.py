import unittest
import os
from security import AES

class AESTest(unittest.TestCase):
    def testCBCEncryption(self):
        print("Testing AES-CBC Encryption")
        inputText = "This is an example input string that should be encrypted, then decrypted!"
        encryptedText = AES.encryptBlockText(inputText)
        decryptedText = AES.decryptBlockText(encryptedText[0], encryptedText[3], encryptedText[1], encryptedText[2])
        self.assertEqual(inputText, decryptedText.decode("utf-8"))

    def testFakeEncryption(self):
        print("Testing Fake Encryption")
        inputText = "This is an example input string that should be encrypted, then decrypted!"
        encryptedText = AES.encryptBlockText(inputText, "FAKE")
        decryptedText = AES.decryptBlockText(encryptedText[0], encryptedText[3], encryptedText[1], encryptedText[2])
        self.assertEqual(inputText, decryptedText.decode("utf-8"))