import media
import fresh_tomatoes as ft

def create_movie_object(line_of_config):
    parts = line_of_config.replace(' ','').split(',')
    return media.Movie(parts[0], parts[1], parts[2])


with open('movie_list.csv') as fhandle:
    movies = [create_movie_object(line) for line in fhandle]

ft.open_movies_page(movies)

