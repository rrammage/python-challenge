'''
Created on Oct 19, 2014

@author: ron
'''
# import httplib2
# resp, content = httplib2.Http().request("http://www.pythonchallenge.com/pc/def/linkedlist.php")
# print content

import urllib

url_root = "http://www.pythonchallenge.com/pc/def/linkedlist.php?"
# form_field = {'nothing':'12345'}
# form_data = urllib.urlencode(form_field)
# url_string = url_root + form_data
# 
# pretext_string = 'and the next nothing is '
# u = urllib.urlopen(url_string)
# intermediate_string = u.readline()
# 
# counter = 0
# while counter < 400:
#     index = intermediate_string.find(pretext_string) + pretext_string.__len__()
#     stop_sentinnel = intermediate_string.__len__()
#     next_string = ""
#     
#     while (index < stop_sentinnel) and (intermediate_string[index].isdigit()):
#         next_string = next_string + intermediate_string[index]
#         index = index + 1
#  
#     form_field = {'nothing': next_string}
#     form_data = urllib.urlencode(form_field)    
#     url_string = url_root + form_data
#     u = urllib.urlopen(url_string)
#     intermediate_string = u.readline()
#     print counter, intermediate_string
#     counter = counter + 1
# 
# print intermediate_string

# After 82 iterations the output is 
# 82 and the next nothing is 3875
# 83 and the next nothing is 16044
# 84 Yes. Divide by two and keep going.
# 85 and the next nothing is 6711

# Other snags in the sequence include a false 'next nothing' and multiline strings
# keep following.
# Eventually gett to 
# 108 peak.html

form_field = {'nothing':'63579'}
form_data = urllib.urlencode(form_field)
url_string = url_root + form_data
 
pretext_string = 'and the next nothing is '
u = urllib.urlopen(url_string)
intermediate_string = u.readline()
 
counter = 0
while counter < 400:
    index = intermediate_string.find(pretext_string) + pretext_string.__len__()
    stop_sentinnel = intermediate_string.__len__()
    next_string = ""
     
    while (index < stop_sentinnel) and (intermediate_string[index].isdigit()):
        next_string = next_string + intermediate_string[index]
        index = index + 1
  
    form_field = {'nothing': next_string}
    form_data = urllib.urlencode(form_field)    
    url_string = url_root + form_data
    u = urllib.urlopen(url_string)
    intermediate_string = u.read()
    print counter, intermediate_string
    counter = counter + 1
 
print intermediate_string