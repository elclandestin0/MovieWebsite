# Code written by: Memo Khoury, under the guidance of the Udacity team
# Modules used: webbrowser
# Start date: 11/01/2017
# Last modified: 11/03/2017

import webbrowser

class Movie():
    """ This class defines a movie with four attributes:
        it's title, trailer, poster, and storyline. It also
        has a function to show the trailer
    Attributes:
              movie_title: A string that contains the movie title.
              trailer_youtube_url: A string containing the URL link of the trailer.
              storyline: A string that contains a movie's description/overview.
              poster_image_url: A string of a directory path that contains the image.
    """

    #VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, movie_title, trailer_youtube_url, storyline, poster_image_url):
        self.title = movie_title
        self.trailer_youtube_url = trailer_youtube_url
        self.storyline = storyline
        self.poster_image_url = poster_image_url

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)
