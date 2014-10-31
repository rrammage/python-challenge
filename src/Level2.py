'''
Created on Sep 27, 2014

@author: ron
'''

import httplib2
from string import maketrans

def extractText(lclLetter):

    table = maketrans("!@#$%^&*(){}[]+=-_","                  ")

    # Eliminate apply translation, remove white space and newline characters.
    intermediate = lclLetter.translate(table).replace(" ","").replace("\n","")
    return intermediate

# Get the data after the end of the HTML source
resp, content = httplib2.Http().request("http://www.pythonchallenge.com/pc/def/ocr.html")
contentAfterHTML = content.split("</html>",1)[1]

# Decode by removing extraneous characters.
print extractText(contentAfterHTML)