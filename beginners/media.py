import webbrowser as wb

class Movie():
    """ This class provides a way to store movie related information""" #define __doc__

    valid_ratings = ["G", "PG", "PG-13", "R"] #Class Variable
    
    def __init__(self, title, storyline, poster_image_url, trailer_youtube_url):
        self.title = title #Instance variables
        self.storyline = storyline
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url

    def show_trailer(self):
        wb.open(self.trailer_youtube_url)


toy_story = Movie('Toy Story', 'Title',
                  'https://www.youtube.com/', 'https://www.youtube.com/')

print(Movie.valid_ratings)
print(Movie.__doc__)
