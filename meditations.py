#source: 'http://www.gutenberg.org/cache/epub/2680/pg2680.txt'

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
                BOOK_list.append((linenum, line.rstrip('\n'))) #Could do tuples, list of tuples allows me to access indexes, unlike dict
                # line_book_dict[linenum] = line.rstrip('\n')
# print(BOOK_list)
# print(BOOK_list[11][1]) #THE SECOND BOOK

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

#Bug: need to fix last book, should be book_end = last line of data "data[-1]"

##parse books to get meditations

# for items in line_book_list: 
        # print(items)

##store in a list of dictionaries or dict of dicts: 
# {booknum: {
#     meditationnum: "meditation text"
# }}