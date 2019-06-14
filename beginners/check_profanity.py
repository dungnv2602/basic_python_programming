from urllib.request import urlopen

def read_text():
    quotes= open('movie_quotes.txt','r').read()
    check_profanity(quotes)
    quotes.close()

def check_profanity(text):
    conn = urlopen("http://www.wdylike.appspot.com/?q="+text)
    output = conn.read()
    print(output)
    conn.close()

