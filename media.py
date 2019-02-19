class Movie:
    '''
    This class contains the properties and behavior representing a movie object
    '''
    def __init__(self, title, poster_image_url, trailer_youtube_url):
        self.trailer_youtube_url = trailer_youtube_url
        self.title = title
        self.poster_image_url = poster_image_url