import movie.model as model
from movie.persistence.dao import Dao
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker

class IMDBDao(Dao):

    def get_all(self):
        stm = select(model.IMDB)
        result = self.session.execute(stm).fetchall()
        return result

    def get_by_id(self, id):
        stm = select(model.IMDB).where(model.IMDB.imdb_id == id)
        result = self.session.execute(stm).fetchall()
        return result
    
    def get_by_rating(self, rate):
        stm = select(model.IMDB.imdb_rating).where(model.IMDB.imdb_rating >= float(rate))
        result = self.session.execute(stm).fetchall()
        return result