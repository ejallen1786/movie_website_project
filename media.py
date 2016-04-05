# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define the class Movie. You could do this
# directly in entertainment_center.py but many developers keep their
# class definitions separate from the rest of their code. This also
# gives you practice importing Python files.

# https://www.udacity.com/course/viewer#!/c-nd000/l-4185678656/m-1013629057

import webbrowser

class Movie():
    # This class provides a way to store movie related information
    # Class can have both data and methods

    """ This class provides a way to store movie related information """

    VALID_RATINGS = ["G", "PG", "PG-13", "R"]

    def __init__(self, title, storyline, poster_image_url, trailer_youtube_url):
        self.title = title
        self.poster_image_url = poster_image_url
        self.trailer_youtube_url = trailer_youtube_url
        self.storyline = storyline

    def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url) 


