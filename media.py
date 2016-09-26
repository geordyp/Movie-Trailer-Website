""" Holds movie related information """
import webbrowser

__author__ = "Geordy Williams"

class Movie():

    def __init__(self, p_title, p_year, p_poster, p_trailer):
        """
        @param p_title: the movie's title
        @param p_year: the year the movie was released
        @param p_poster: the url to the poster image for the movie
        @param p_trailer: the url to the movie's trailer on youtube
        """

        self.title = p_title
        self.year = p_year
        self.poster_image_url = p_poster
        self.trailer_youtube_url = p_trailer

    def get_title(self):
        return self.title

    def get_year(self):
        return self.year

    def get_poster_url(self):
        return self.poster

    def get_trailer_url(self):
        return self.trailer_youtube_url

    def show_trailer(self):
        webbrowser.open(self.trailer_youtube_url)

    def show_poster(self):
        webbrowser.open(self.poster_image_url)
