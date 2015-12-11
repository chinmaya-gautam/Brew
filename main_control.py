#!/usr/bin/python

import db_utilities
import fetch_data

print "test"

db = db_utilities.database_()
src = fetch_data.source()

db.create_tables()
src.parse_imdb_top_250()
movies = src.get_imdb_movie_details(True)

db.store_movies_in_db(movies)
print "done storing movies!"
