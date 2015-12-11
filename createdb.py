#!/usr/bin/python

import sqlite3

class database_ :
    
    def __init__(self):
        self.conn = sqlite3.connect('movies.db')
        self.cur = self.conn.cursor()

    def get_cursor(self):
        return self.cur

    def create_tables(self):
        cur = self.get_cursor()
        
        cur.execute('''create table movies (
                       m_id integer primary key,
                       m_name varchar(80),
                       m_runningTime integer,
                       m_contentRating varchar(32),
                       m_imdbRating integer,
                       m_description text
                       ) ''')
        cur.execute('''create table actors (
                       a_id integer not null,
                       a_name varchar(80),
                       a_mid integer,
                       foreign key (a_mid) references movies(m_id)
                       )''')
        cur.execute('''create table directors(
                       d_id integer not null,
                       d_name varchar(80),
                       d_mid integer,
                       foreign key (d_mid) references movies(m_id)
                       )''')
        cur.execute('''create table genre(
                       g_id integer not null,
                       g_type varchar(32),
                       g_mid integer,
                       foreign key (g_mid) references movies(m_id)
                       )''')
        cur.execute('''create table media(
                       md_type varchar(32) not null,
                       md_mid integer,
                       md_aid integer, 
                       md_content blob,
                       foreign key (md_mid) references movies(m_id),
                       foreign key (md_aid) references actors(a_id)
                       )''')

        cur.close()

db = database_()
db.create_tables()
