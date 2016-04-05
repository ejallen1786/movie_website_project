# Lesson 3.4: Make Classes
# Mini-Project: Movies Website

# In this file, you will define instances of the class Movie defined
# in media.py. After you follow along with Kunal, make some instances
# of your own!

# After you run this code, open the file fresh_tomatoes.html to
# see your webpage!

# https://www.udacity.com/course/viewer#!/c-nd000/l-4185678656/e-991358856/m-1013629064

import media
import fresh_tomatoes

toy_story = media.Movie("Toy Story", "A story of a boy and his toys that come to life", "http://img.lum.dolimg.com/v1/images/open-uri20150422-20810-m8zzyx_5670999f.jpeg?region=0,0,300,450", "https://www.youtube.com/watch?v=QW0sjQFpXTU")

avatar = media.Movie("Avatar", "A marine on an alien planet", "http://imgs.abduzeedo.com/files/articles/Avatar/4154691413_a695e033a8_o.jpg", "https://www.youtube.com/watch?v=cRdxXPV9GNQ")

jurassic_park = media.Movie("Jurassic Park", "An amusement park with dinosaurs!", "http://images.moviepostershop.com/jurassic-park-movie-poster-1992-1020141477.jpg", "https://www.youtube.com/watch?v=lc0UehYemQA")

school_of_rock = media.Movie("School of Rock", "Using rock music to learn", "http://ia.media-imdb.com/images/M/MV5BMjEwOTMzNjYzMl5BMl5BanBnXkFtZTcwNjczMTQyMQ@@._V1_SX640_SY720_.jpg", "https://www.youtube.com/watch?v=3PsUJFEBC74")

midnight_in_paris = media.Movie("Midnight in Paris", "Going back in time to meet authors", "http://ia.media-imdb.com/images/M/MV5BMTM4NjY1MDQwMl5BMl5BanBnXkFtZTcwNTI3Njg3NA@@._V1_SX640_SY720_.jpg", "https://www.youtube.com/watch?v=BYRWfS2s2v4")

hunger_games = media.Movie("Hunger Games", "A really real reality show", "http://vignette1.wikia.nocookie.net/thehungergames/images/0/09/Mockingjay_part_1_poster_2.jpg/revision/latest?cb=20150109223445", "https://www.youtube.com/watch?v=4S9a5V9ODuY")

movies = [toy_story, avatar, jurassic_park, school_of_rock, midnight_in_paris, hunger_games]

fresh_tomatoes.open_movies_page(movies)

