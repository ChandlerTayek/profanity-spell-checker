def read_text():
    quotes = open(r"E:\Udacity\programming-foundations\profanity-spell-checker\movie_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
        
read_text()