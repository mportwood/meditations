#source: 'http://www.gutenberg.org/cache/epub/2680/pg2680.txt'

##Original idea was to parse the meditation text and
##store in a list of dictionaries or dict of dicts like this: 
# {book_num: {
#     meditation_num: "meditation text"
# }}

##I ended up not doing that, but may end up going back and doing it later
##For now, this consistently prints a random meditation

##connect to meditations text in the data folder
with open('data/meditations.txt') as file:
   data = file.read().splitlines()

data = data[576:] #remove header
data = data[:(5717-577)] #remove appendix/end matter
# print(data[:1]) #Test: First Line
# print(data[5139:]) #Test: Last Line

BOOK_list = []
substr = 'BOOK'
# first_ten_lines = data[:10]
for linenum, line in enumerate(data):    # Keep track of line numbers
        #If substring search matches, then store index # and line (Book Title) in a dictionary
        if line.find(substr) != -1:
                BOOK_list.append((linenum, line.rstrip('\n'))) #Could do tuples, list of tuples allows me to access indexes
                # line_book_dict[linenum] = line.rstrip('\n') #Alternative, could do with dict; I opted for tuple route

index0 = 0 
index1 = 1
line_book_list = []
for item in BOOK_list: 
        record = {} #Each record is a dict that stores name, start, end of a book
        record['book_title'] = item[1]
        record['book_start'] = BOOK_list[index0][0]##All of the indexes
        record['book_end'] = BOOK_list[index1][0]
        index0+=1
        if BOOK_list[index1][0] < 4811:
                index1+=1
        line_book_list.append(record)

##Fix the last book's ending to be the end of the file
last_line=len(data)
line_book_list[11]['book_end'] = last_line

#Creates a list of dictionaries,
#Each dict has the book name and the body of meditations split by book
body = []
record_index = 0
for record in line_book_list: 
        meditations_body = {}
        meditations_body['book_title'] = record['book_title']
        meditations_body['index'] = record_index
        meditations_body['book_body'] = data[int(record['book_start']+2):record['book_end']]
        record_index+=1
        body.append(meditations_body)
# print(body[0]['book_body'])

##parse data to get meditations
##What this sections does is, join all the text lines back into one string
## Then parses the string  to find the breaks "double spaces"
## Then turn those into dicts for each meditation
for book in body:   
        book['book_body'] = ' '.join(book['book_body'])
        book['book_body'] = book['book_body'].split('  ')

import random
#the book count is fixed, so a simple random number works
random_book_num = random.randint(0,11)

# have to find book len
#then put that books len in the randint range for the med

meditations_in_book = (len(body[random_book_num]['book_body']))
# print(random_book_num)
# print(meditations_in_book)

#the meditation count is variable based on book
# have to account for that
random_meditation_num = random.randint(0,meditations_in_book)
random_book = body[random_book_num]['book_title']
random_meditation = body[random_book_num]['book_body'][random_meditation_num]

random_meditation = '>' + random_meditation #This '>' just makes it display as a quote in slack
##TEST: PASS
##Tested by running several times
##confirmed this prints meditations in the whole book range
##confirmed this prints meditations in the range within a given book
# print(random_book, random_meditation)


##This is the code for sending the message via slack

##First have to install slackclient. More on that here: https://pypi.org/project/slackclient/
#run this in CLI: 
#pip install slackclient

import os
from slackclient import SlackClient

from api_key import api_key #import api_key as a variable from the api_key file
slack_token = api_key
sc = SlackClient(slack_token)

quote_indicator = '>'
sc.api_call(
  "chat.postMessage",
  channel="meditation",
  text="%s\n%s" %(random_book, random_meditation)
)