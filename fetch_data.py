#!/usr/bin/python

import mechanize
import cookielib
import re
from bs4 import BeautifulSoup, Tag

#sources
'''This is a temporary list,
will be moved to a databse on further development
'''
#1 IMDB:
imdb_source = "http://www.imdb.com/chart/top"

#movie data
class movie:
    def __init__(self):
        self.mName = ""
        self.mRelDate = ""
        self.mIMDBRating = ""
        self.mIMDBLink = ""
        self.mPoster = ""
        self.mGenre = ""
        self.mRunningTime = ""
        self.mContentRating = ""
        self.mGenre = []
        self.mActors = []
        self.mDirector = ""
        self.description = ""

    def set_movie_name(self, name):
        self.mName = name
    def set_movie_rel_date(self,date):
        self.mRelDate = date
    def set_movie_imdb_rating(self,rating):
        self.mIMDBRating = rating
    def set_movie_imdb_link(self, link):
        self.mIMDBLink = link
    def set_movie_poster(self,link):
        self.mPoster = link
    def set_movie_running_time(self, rtime):
        self.mRunningTime = rtime
    def set_movie_content_rating(self, crating):
        self.mContentRating = crating;
    def set_movie_genre(self, gList):
        self.mGenre.extend(gList)
    def set_movie_actors(self, aList):
        self.mActors.extend(aList)
    def set_movie_director(self, director):
        self.mDirector = director
    def set_movie_description(self, description):
        self.mDescription = description

#setup browser
class browser:
    def __init__(self):
    #Browser
        self.br = mechanize.Browser()

    #Cookie Jar
        self.cj = cookielib.LWPCookieJar()
        self.br.set_cookiejar(self.cj)

    #Browser options
        self.br.set_handle_equiv(True)
        self.br.set_handle_gzip(True)
        self.br.set_handle_redirect(True)
        self.br.set_handle_referer(True)
        self.br.set_handle_robots(False)

    # Follows refresh 0 but not hangs on refresh > 0
        self.br.set_handle_refresh(mechanize._http.HTTPRefreshProcessor(), max_time=1)

    # Want debugging messages?
    #br.set_debug_http(True)
    #br.set_debug_redirects(True)
    #br.set_debug_responses(True)

    #User-Agent
        self.br.addheaders = [('User-agent', 'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.1) Gecko/2008071615 Fedora/3.0.1-1.fc9 Firefox/3.0.1')]
        print "initializing browser..."
    #return browser
    def get_browser(self):
        return self.br


#get data from sources and parse data
class source:
    def __init__(self):
        c_br = browser()
        self.browser = c_br.get_browser()
        self.imdb_base_url = "http://www.imdb.com"
        self.links = [] #temporarily store links from a site
        self.movies = []

    def get_sources(self):
        self.imdb_top_250 = "http://www.imdb.com/chart/top"
    
    def get_html(self, url):
        result = self.browser.open(url)
        return result
    
    def parse_imdb_top_250(self):
        result = self.get_html("http://www.imdb.com/chart/top")
        html = result.read()
        self.soup = BeautifulSoup(html, 'html.parser')
        for table in self.soup.find_all('td', class_="posterColumn"):
            #print "record>>", table
            link = self.imdb_base_url + table.find('a')['href'] + ""
            self.links.append(link)
        #print self.links

    def get_imdb_movie_details(self, output_mode):
        counter = 0
        for link in self.links:
            counter += 1
            print counter
            self.movies.append(movie())

            result = self.get_html(link)
            html = result.read()
            self.soup = BeautifulSoup(html, 'html.parser')
            self.soup.prettify()
            #name
            movie_name =  self.soup.find('span', class_='itemprop', itemprop='name').string
            movie_name = movie_name.replace("'", "''")
            self.movies[-1].set_movie_name(movie_name)
            
            #imdb rating
            movie_rating =  self.soup.find('span', itemprop='ratingValue').string
            self.movies[-1].set_movie_imdb_rating(movie_rating)

            #content Rating
            movie_content_rating =  self.soup.find('meta', itemprop='contentRating')['content']
            self.movies[-1].set_movie_content_rating(movie_content_rating)
            
            #running time
            running_time = "" +  self.soup.find('time', itemprop='duration').contents[0].string
            running_time = running_time.strip()
            running_time = running_time.split(' ')[0]
            self.movies[-1].set_movie_running_time(running_time)

            #genre
            g_list = []
            for genre in self.soup.find_all('span', class_='itemprop', itemprop='genre'):
                g_list.append(genre.string)
            #    print genre.string
            self.movies[-1].set_movie_genre(g_list)

            #release date
            release_date = self.soup.find('meta', itemprop='datePublished')['content']
            self.movies[-1].set_movie_rel_date(release_date)

            #Director
            director = self.soup.find('div', itemprop='director').contents[3].string
            director = director.replace("'", "''")
            self.movies[-1].set_movie_director(director)

            #Actors
            a_list = []
            for actor in  self.soup.find('div',itemprop='actors').find_all('span', class_='itemprop', itemprop='name'):
                actor = actor.string
                actor = actor.replace("'", "''")
                a_list.append(actor)
             #   print actor.string
            self.movies[-1].set_movie_actors(a_list)

            #Description
            description = self.soup.find('p', itemprop='description').contents
            str = ""
            for unit in description:
                if type(unit) is Tag:
                    str += unit.string
                else:
                    str += unit
            str = str.replace("'", "''")
            str = str.strip()
            self.movies[-1].set_movie_description(str)
            #print description

            #poster link
            poster =  self.soup.find('img', itemprop='image')['src']
            self.movies[-1].set_movie_poster(poster)

            if output_mode:
                print "--------------------------------------------------------------------------"
                print ""
                print "Movie: " + movie_name
                print "Rating: " + movie_rating
                print "Relase: " + release_date
                print "Director: " + director
            #break #debug statement
        return self.movies
#print html

#src = source()

#src.parse_imdb_top_250()
#movies = src.get_imdb_movie_details()
