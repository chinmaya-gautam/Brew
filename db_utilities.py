#!/usr/bin/python

import sqlite3
import fetch_data

class database_ :
    
    tables = ["movies", "actors", "directors", "media", "sources"]

    def __init__(self):
        self.conn = sqlite3.connect('movies.db')
        self.cur = self.conn.cursor()

    def get_cursor(self):
        return self.cur

    def commit_changes(self):
        self.conn.commit()

    def check_tables_exist(self):
        cur = self.get_cursor()

        for table_name in self.tables:
            query = "SELECT count(*) FROM sqlite_master WHERE type='table' AND name='" + table_name + "'"
            cur.execute(query)
            result = cur.fetchall()[0][0]
            if result == 0:
                return False
        return True

    def create_tables(self):
        if self.check_tables_exist():
            return 

        cur = self.get_cursor()
        #sqlite creates a 'ROWID' primary key automatically, so no need to explicitly provide one
        cur.execute('''create table movies (
                       m_name varchar(80) primary key,
                       m_runningTime integer,
                       m_contentRating varchar(32),
                       m_imdbRating real,
                       m_description text
                       ) ''')
        cur.execute('''create table actors (
                       a_name varchar(80),
                       a_movie varchar(80),
                       foreign key (a_movie) references movies(m_name)
                       )''')
        cur.execute('''create table directors(
                       d_name varchar(80),
                       d_movie varchar(80),
                       foreign key (d_movie) references movies(m_name)
                       )''')
        cur.execute('''create table genre(
                       g_type varchar(32),
                       g_movie varchar(80),
                       foreign key (g_movie) references movies(m_name)
                       )''')
        cur.execute('''create table media(
                       md_type varchar(32) not null,
                       md_actor varchar(80),
                       md_director varchar(80),
                       md_movie varchar(80),
                       md_content blob,
                       foreign key (md_movie) references movies(m_name),
                       foreign key (md_actor) references actors(a_name),
                       foreign key (md_director) references director(d_name)
                       )''')
        cur.execute('''create table sources(
                        src_name varchar(32),
                        src_link text
                    )''')
    def store_movies_in_db(self, movies):
        cur = self.get_cursor()
        print "adding movie to databse"
        for movie in movies:
            print "adding 1 movie"
            query = "insert into movies values(?, ?, ?, ?, ?)"
            cur.execute(query, [movie.mName, movie.mRunningTime, movie.mContentRating, movie.mIMDBRating, movie.mDescription])
            
            query = "insert into directors values(?, ?)"
            cur.execute(query, [movie.mDirector, movie.mName])
            
            #get image
            image_file = open(movie.mPoster, 'rb')
            image_binary = image_file.read()
            query = "insert into media (md_type, md_movie, md_content) values(?, ?, ?)"
            cur.execute(query, ["image", movie.mName, buffer(image_binary)])
            
            for actor in movie.mActors:
                query = "insert into actors values (?, ?)"
                cur.execute(query, [actor, movie.mName])

            for gen in movie.mGenre:
                query = "insert into genre values (?, ?)"
                cur.execute(query, [gen, movie.mName])

        self.commit_changes()
        print "done adding movie"

#db = database_()
#flag = db.check_tables_exist()
#print flag

