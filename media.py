
# -*- coding: utf-8 -*-

import webbrowser


class Movie:
    """
    This class define movie object and your behavior.
    """

    def __init__(self, movie_title, movie_story, movie_poster, movie_trailer):
        self.title = movie_title
        self.storyline = movie_story
        self.poster_image_url = movie_poster
        self.trailer_youtube_url = movie_trailer

    def show_trailer(self):
        """
        This method is responsibily for open the movie trailer.
        """
        webbrowser.open(self.trailer_youtube_url)

