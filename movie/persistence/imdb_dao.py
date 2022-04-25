import movie.model as model
from movie.persistence.dao import Dao
from sqlalchemy import create_engine, select, update
from sqlalchemy.orm import sessionmaker

class IMDBDao(Dao):

    def get_all(self):
        stm = select(model.IMDB)
        result = self.session.execute(stm).fetchall()
        return result

    def get_imdb_id(self):
        stm = select(model.IMDB.imdb_id)
        result = self.session.execute(stm).fetchall()
        return result

    def get_imdb_rating(self):
        stm = select(model.IMDB.imdb_rating)
        result = self.session.execute(stm).fetchall()
        return result

    def get_meta_score(self):
        stm = select(model.IMDB.meta_score)
        result = self.session.execute(stm).fetchall()
        return result

    def get_no_of_vote(self):
        stm = select(model.IMDB.no_of_vote)
        result = self.session.execute(stm).fetchall()
        return result

    def get_certificate(self):
        stm = select(model.IMDB.certificate)
        result = self.session.execute(stm).fetchall()
        return result

    def get_poster_link(self):
        stm = select(model.IMDB.poster_link)
        result = self.session.execute(stm).fetchall()
        return result

    def get_imdb_id_from_id(self, id):
        stm = select(model.IMDB.imdb_id).where(model.IMDB.imdb_id == id)
        result = self.session.execute(stm).fetchall()
        return result

    def get_imdb_rating_from_id(self, id):
        stm = select(model.IMDB.imdb_rating).where(model.IMDB.imdb_id == id)
        result = self.session.execute(stm).fetchall()
        return result

    def get_meta_score_from_id(self, id):
        stm = select(model.IMDB.meta_score).where(model.IMDB.imdb_id == id)
        result = self.session.execute(stm).fetchall()
        return result

    def get_no_of_vote_from_id(self, id):
        stm = select(model.IMDB.no_of_vote).where(model.IMDB.imdb_id == id)
        result = self.session.execute(stm).fetchall()
        return result

    def get_certificate_from_id(self, id):
        stm = select(model.IMDB.certificate).where(model.IMDB.imdb_id == id)
        result = self.session.execute(stm).fetchall()
        return result

    def get_poster_link_from_id(self, id):
        stm = select(model.IMDB.poster_link).where(model.IMDB.imdb_id == id)
        result = self.session.execute(stm).fetchall()
        return result

    def update_imdb(self, imdb_id, rate, score, vote, certificate, poster):
        id = imdb_id
        stm = update(model.IMDB).where(model.IMDB.imdb_id == id[0][0]).values(imdb_id=id[0][0], imdb_rating=rate, meta_score=score, no_of_vote=vote, certificate=certificate, poster_link=poster)
        self.session.execute(stm)

    def get_by_id(self, id):
        stm = select(model.IMDB).where(model.IMDB.imdb_id == id)
        result = self.session.execute(stm).fetchall()
        return result
    
    def get_by_rating(self, rate):
        stm = select(model.IMDB.imdb_rating).where(model.IMDB.imdb_rating >= float(rate))
        result = self.session.execute(stm).fetchall()
        return result