## Code written  by: Memo Khoury
# Start date: <insert date>
# Last modified: <insert date>
#
# Comments are numbered to the right of the lines of code,
# to understand each comment, kindly scroll to the
# bottom of the file.

import webbrowser

class Movie():
    """ This class defines a movie with four attributes: it's title, trailer, poster, and storyline. It also has a function to show the trailer """

    VALID_RATINGS = ["G", "PG", "PG-13", "R"] #1

    def __init__(self, movie_title, trailer_youtube_url, storyline, poster_image_url):  #2
        self.title = movie_title
        self.trailer_youtube_url = trailer_youtube_url
        self.storyline = storyline
        self.poster_image_url = poster_image_url

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)





##### List of Comments #####
#1: CONSTANT VARIABLES ARE ALL CAPS BY NAME DECLARATION
