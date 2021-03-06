#! /usr/bin/env python
import os, sys, argparse, pprint
from imdb import IMDb


def searchperson(ia, person):
    for name in ia.search_person(person):
        print name.personID, name['name']

def searchmovie(ia, title):
    for name in ia.search_movie(title):
        print name.movieID, name['title']

def getmovie(ia, movieid):
    moviedata = ia.get_movie(movieid)
    print moviedata.summary()

def main():
    parser = argparse.ArgumentParser(description="test args")
    parser.add_argument('-t', '--title', help="movie title" )
    parser.add_argument('-p', '--person', help="person")
    parser.add_argument('-i', '--movieid', help="id")

    args = parser.parse_args()
    ia = IMDb()

    if args.person:
        args = args.person.lower()
        searchperson(ia, args)

    if args.title:
        args = args.title.lower()
        searchmovie(ia, args)

    if args.movieid:
        args = args.movieid.lower()
        getmovie(ia, args)


if __name__ == "__main__":
    main()
