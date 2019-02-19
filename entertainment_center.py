import media
import fresh_tomatoes as ft

def create_movie_object(line_of_config):
    """
    This function takes in a string with `|` separated values of a movie object
    The first part should be a movie title, the 2nd a URL to the movie poster and the 3rd the URL to the movie trailer.
    """
    parts = line_of_config.replace(' ','').split('|')
    return media.Movie(parts[0], parts[1], parts[2])


with open('movie_list.csv') as fhandle:
    movies = [create_movie_object(line) for line in fhandle]

ft.open_movies_page(movies)

