'''
Created on Sep 28, 2014

@author: ron
'''

import httplib2


def patternMatch(inString):
    # Routine that takes 9 characters and returns true or false based on whether
    # the substring matches lUUUlUUUl
    
    #   Use S.isupper() and S.islower()
    if inString[0].islower():
        if inString [1].isupper():
            if inString[2].isupper():
                if inString[3].isupper():
                    if inString[4].islower():
                        if inString[5].isupper():
                            if inString[6].isupper():
                                if inString[7].isupper():
                                    if inString[8].islower():
                                        return True
    return False

resp, content = httplib2.Http().request("http://www.pythonchallenge.com/pc/def/equality.html")
contentAfterHTML = content.split("</html>",1)[1]

# Add code to remove all text up to and including </html>
#print contentAfterHTML

# Need to scan thru the text with a 9 character window.:
# Start by getting the string length.
strLen = contentAfterHTML.__len__()
#print strLen

start = 0
end = 9
goalString = ""
while end <= strLen:
    subString = contentAfterHTML[start:end]
    if patternMatch(subString):
        goalString = goalString + subString[4]
    start += 1
    end += 1

print goalString
# Outputs "linkedlist"

