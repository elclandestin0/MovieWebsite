# Code written by: Memo Khoury under the guidance of the Udacity team
# Modules used: media, fresh_tomatoes, and
# The Movie Database API (https://www.themoviedb.org)
# Start date: 11/01/2017
# Last modified: 11/03/2017

import media
import fresh_tomatoes
import tmdbsimple as tmdb

""" This is the driver file. It creates the movie instances,
    populates the data using The Movie Database as an API,
    and then feeds the array of instances into a function
    in fresh_tomatoes, ultimately compiling it into a website.
"""

tmdb.API_KEY = '4a3e0dba52dfa69ee42550261e86155f'

toy_story = media.Movie("",
                        "https://www.youtube.com/watch?v=KYz2wyBy3kc",
                        "",
                        "")
avatar = media.Movie("",
                     "https://www.youtube.com/watch?v=d1_JBMrrYw8",
                     "",
                     "")

la_haine = media.Movie("",
                       "https://www.youtube.com/watch?v=cy5TaO6qTBU",
                       "",
                       "")

reservoir_dogs = media.Movie("",
                             "https://www.youtube.com/watch?v=vayksn4Y93A",
                             "",
                             "")

the_dark_knight = media.Movie("",
                              "https://www.youtube.com/watch?v=EXeTwQWrcwY",
                              "",
                              "")


spirited_away = media.Movie("",
                            "https://www.youtube.com/watch?v=ByXuk9QqQkk",
                            "",
                            "")

fight_club = media.Movie("",
                         "https://www.youtube.com/watch?v=SUXWAEX2jlg",
                         "",
                         "")

the_departed = media.Movie("",
                           "https://www.youtube.com/watch?v=iojhqm0JTW4",
                           "",
                           "")

jurassic_park = media.Movie("",
                            "https://www.youtube.com/watch?v=lc0UehYemQA&",
                            "",
                            "")

movies = [toy_story,
          avatar,
          la_haine,
          reservoir_dogs,
          the_dark_knight,
          spirited_away,
          fight_club,
          the_departed,
          jurassic_park]

movies_search_string = ['Toy Story',
                        'Avatar',
                        'La Haine',
                        'Reservoir Dogs',
                        'The Dark Knight',
                        'Spirited Away',
                        'Fight Club',
                        'The Departed',
                        'Jurassic Park']


def populate_data(movies_list):
    """Fetches data of movie from The Movie Database using TMDB API.

        Retrieves the unique tuple that we need based on the array of string
        movies above. After selecting the movie based on the search, it takes
        it's title, overview, and poster image. This data is fed back to the
        movie instance.

    Args:
        moviesList: An array of movie instances we created before. Each
        instance's parameters are empty, except the Youtube URL.
        This is because we want to fetch/overwrite the other data using
        this function.
    """

    # For each item in the array of strings containing the movie title,
    # we request a search from TMDB API using that item in the array.
    # For the first item that comes in the search, we fetch the movie's
    # title, storyline, and poster image and set it to the corresponding
    # movie instance, which is in an array of movie instances created
    # above. The loop breaks after the first search because it is the
    # most confident item in the query.

    for m in range(len(movies_list)):
        search = tmdb.Search()
        response = search.movie(query=movies_search_string[m])
        for s in search.results:
            movies_list[m].title = s['title']
            movies_list[m].storyline = s['overview']
            movies_list[m].poster_url = "https://image.tmdb.org/t/p/w500" + s['poster_path']
            break

populate_data(movies)
fresh_tomatoes.open_movies_page(movies)
