import media
import fresh_tomatoes
import webbrowser
import urllib2
import tmdbsimple as tmdb

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
                           "https://www.youtube.com/watch?v=lc0UehYemQA&t=66s",
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
          jurassic_park
          ]

movies_search_string = ['Toy Story',
                        'Avatar',
                        'La Haine',
                        'Reservoir Dogs',
                        'The Dark Knight',
                        'Spirited Away',
                        'Fight Club',
                        'The Departed',
                        'Jurassic Park']

def populate_data(moviesList):
    for m in range(len(moviesList)):
        search = tmdb.Search()
        response = search.movie(query = movies_search_string[m])
        for s in search.results:
            moviesList[m].title = s['title']
            moviesList[m].storyline = s['overview']
            moviesList[m].poster_image_url = "https://image.tmdb.org/t/p/w500" + s['poster_path']
            break



populate_data(movies)

fresh_tomatoes.open_movies_page(movies)
