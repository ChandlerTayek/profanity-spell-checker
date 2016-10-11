import urllib.request
def read_text():
    quotes = open(r"E:\Udacity\programming-foundations\profanity-spell-checker\movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    check_profanity(contents_of_file)
    
def check_profanity(text_to_check):
    connection = urllib.request.urlopen("http://www.wdylike.appspot.com/?q=" + urllib.parse.quote(text_to_check))
    output = str(connection.read())
    #print(output)
    connection.close()
    if "true" in output:
        print("Profanity Alert!!!")
    elif "false" in output:
        print("This document has no curse words!")
    
read_text()