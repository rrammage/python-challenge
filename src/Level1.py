'''
Created on Sep 27, 2014

@author: ron
'''
from string import maketrans

def MysteryString1():
    return "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. \
bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. \
sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

def MysteryString2():
    return "http://www.pythonchallenge.com/pc/def/map.html"


# Decode the mystery string by applying a Shift 2 Ceasar's cypher.
def Decrypt(EncryptedString):

    
    letters = list(EncryptedString)
    
    for letter in letters:
        print shiftLetter(letter),
        
def shiftLetter(lclLetter):

    table = maketrans("abcdefghijklmnopqrstuvwxyz","cdefghijklmnopqrstuvwxyzab")
    return lclLetter.translate(table)
#     return alphabet[letterIndex]

Decrypt(MysteryString1())
print
Decrypt(MysteryString2())
