""" Creates an array of movies which are passed to fresh_tomatoes to be displayed """
import fresh_tomatoes
import media

__author__ = "Geordy Williams"

toy_story = media.Movie("Toy Story",
        "1995",
        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
        "http://www.youtube.com/watch?v=vwyZH85NQC4")

bugs_life = media.Movie("A Bug's Life",
        "1998",
        "https://upload.wikimedia.org/wikipedia/en/c/cc/A_Bug%27s_Life.jpg",
        "https://www.youtube.com/watch?v=cXWRAb84TTE")

toy_story_2 = media.Movie("Toy Story 2",
        "1999",
        "https://upload.wikimedia.org/wikipedia/en/c/c0/Toy_Story_2.jpg",
        "https://www.youtube.com/watch?v=Lu0sotERXhI")

monsters_inc = media.Movie("Monsters Inc",
        "2001",
        "https://upload.wikimedia.org/wikipedia/en/6/63/Monsters_Inc.JPG",
        "https://www.youtube.com/watch?v=8IBNZ6O2kMk")

finding_nemo = media.Movie("Finding Nemo",
        "2003",
        "https://upload.wikimedia.org/wikipedia/en/2/29/Finding_Nemo.jpg",
        "https://www.youtube.com/watch?v=wZdpNglLbt8")

incredibles = media.Movie("Incredibles",
        "2004",
        "https://upload.wikimedia.org/wikipedia/en/e/ec/The_Incredibles.jpg",
        "https://www.youtube.com/watch?v=sZwWCrFNfzQ")

cars = media.Movie("Cars",
        "2006",
        "https://upload.wikimedia.org/wikipedia/en/3/34/Cars_2006.jpg",
        "https://www.youtube.com/watch?v=WGByijP0Leo")

ratatouille = media.Movie("Ratatouille",
        "2007",
        "http://upload.wikimedia.org/wikipedia/en/5/50/RatatouillePoster.jpg",
        "https://www.youtube.com/watch?v=c3sBBRxDAqk")

walle = media.Movie("WALL-E",
        "2008",
        "https://upload.wikimedia.org/wikipedia/en/c/c2/WALL-Eposter.jpg",
        "https://www.youtube.com/watch?v=alIq_wG9FNk")

up = media.Movie("Up",
        "2009",
        "https://upload.wikimedia.org/wikipedia/en/0/05/Up_%282009_film%29.jpg",
        "https://www.youtube.com/watch?v=pkqzFUhGPJg")

toy_story_3 = media.Movie("Toy Story 3",
        "2010",
        "https://upload.wikimedia.org/wikipedia/en/6/69/Toy_Story_3_poster.jpg",
        "https://www.youtube.com/watch?v=JcpWXaA2qeg")

cars_2 = media.Movie("Cars 2",
        "2011",
        "https://upload.wikimedia.org/wikipedia/en/7/7f/Cars_2_Poster.jpg",
        "https://www.youtube.com/watch?v=oFTfAdauCOo")

brave = media.Movie("Brave",
        "2012",
        "https://upload.wikimedia.org/wikipedia/en/9/96/Brave_Poster.jpg",
        "https://www.youtube.com/watch?v=TEHWDA_6e3M")

monsters_university = media.Movie("Monsters University",
        "2013",
        "https://upload.wikimedia.org/wikipedia/en/2/2a/Monsters_University_poster_3.jpg",
        "https://www.youtube.com/watch?v=xBzPioph8CI")

inside_out = media.Movie("Inside Out",
        "2015",
        "https://upload.wikimedia.org/wikipedia/en/0/0a/Inside_Out_%282015_film%29_poster.jpg",
        "https://www.youtube.com/watch?v=seMwpP0yeu4")

good_dinosaur = media.Movie("Good Dinosaur",
        "2015",
        "https://upload.wikimedia.org/wikipedia/en/8/80/The_Good_Dinosaur_poster.jpg",
        "https://www.youtube.com/watch?v=O-RgquKVTPE")

movies = [toy_story, bugs_life, toy_story_2, monsters_inc, finding_nemo,
        incredibles, cars, ratatouille, walle, up, toy_story_3, cars_2, brave,
        monsters_university, inside_out, good_dinosaur]
fresh_tomatoes.open_movies_page(movies)
