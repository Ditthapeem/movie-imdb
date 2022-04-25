from re import S
from sqlalchemy import create_engine,ForeignKey, Column, Integer, Float, String, or_, table, update
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

engine = create_engine("sqlite:///top_100_movie.db")
Session = sessionmaker(bind=engine)
session = Session()

Base = declarative_base()
class IMDB(Base):
    __tablename__ = 'IMDB'
    imdb_id = Column(Integer, primary_key=True)
    imdb_rating = Column(Float)
    meta_score = Column(Integer)
    no_of_vote = Column(Integer)
    certificate = Column(String(50))
    poster_link = Column(String(255))

    def __repr__(self):
        return f"IMDB ID = {self.imdb_id} IMDB rating = {self.imdb_rating} Meta score = {self.meta_score} Number of score = {self.no_of_vote} Certificate = {self.certificate} Poster Link = {self.poster_link}"


class Movie(Base):
    __tablename__ = 'movie'
    series_title = Column(String(100), primary_key=True)
    imdb_id = Column(Integer, ForeignKey('IMDB.imdb_id'))
    release_year = Column(Integer)
    runtime = Column(String(50))
    genre = Column(String(50))
    overview = Column(String(100))
    director = Column(String(50))
    star1 = Column(String(50))
    star2 = Column(String(50))
    star3 = Column(String(50))
    star4 = Column(String(50))
    gross = Column(String(50))

    def __repr__(self):
        return f"Series title = {self.series_title} IMDB ID = {self.imdb_id} Release year = {self.release_year} Runtime = {self.runtime} Genre = {self.genre} Overview = {self.overview} Director = {self.director} Star1 = {self.star1} Star2 = {self.star2} Star3 = {self.star3} Star4 = {self.star4} Gross = {self.gross}"


